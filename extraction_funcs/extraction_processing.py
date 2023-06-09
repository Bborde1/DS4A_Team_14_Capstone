"""

This file contains any functions that are used to do any data processing PRIOR to writing to S3.
The goal is to maintain a lower storage footprint, and reduce extraction and load times.

"""
import pandas as pd

# import geo_id generation function
from extraction_funcs.get_geo_id import generate_geo_id


def update_general_payments(general_df):
    # filter out observations with missing first name and last name
    general_df = general_df[general_df['Covered_Recipient_First_Name'].notnull()]
    general_df = general_df[general_df['Covered_Recipient_Last_Name'].notnull()]
    general_df = general_df[general_df['Recipient_Primary_Business_Street_Address_Line1'].notnull()]
    general_df['Recipient_Primary_Business_Street_Address_Line2'] = general_df[
        'Recipient_Primary_Business_Street_Address_Line2'].fillna("")
    general_df['Recipient_Primary_Business_Street_Address_Line2'] = general_df[
        'Recipient_Primary_Business_Street_Address_Line2'].astype(str)

    # concatenate addresses into one address
    # note: corrects for any recipients at the same address, but in different suites
    general_df['Recipient_Primary_Business_Street_Address'] = general_df['Recipient_Primary_Business_Street_Address_Line1'] + \
        general_df['Recipient_Primary_Business_Street_Address_Line2']

    # generate unique geographic id
    general_df['geo_id'] = general_df['Recipient_Primary_Business_Street_Address'].map(
        generate_geo_id)

    return general_df


def update_general_payments_sample(general_df):
    # filter out observations with missing first name and last name
    general_df = general_df[general_df['covered_recipient_first_name'].notnull()]
    general_df = general_df[general_df['covered_recipient_last_name'].notnull()]
    general_df = general_df[general_df['recipient_primary_business_street_address_line1'].notnull()]
    general_df['recipient_primary_business_street_address_line2'] = general_df[
        'recipient_primary_business_street_address_line2'].fillna("")
    general_df['recipient_primary_business_street_address_line2'] = general_df[
        'recipient_primary_business_street_address_line2'].astype(str)

    # concatenate addresses into one address
    # note: corrects for any recipients at the same address, but in different suites
    general_df['recipient_primary_business_street_address'] = general_df['recipient_primary_business_street_address_line1'] + \
        general_df['recipient_primary_business_street_address_line2']

    # generate unique geographic id
    general_df['geo_id'] = general_df['recipient_primary_business_street_address'].map(
        generate_geo_id)

    return general_df
