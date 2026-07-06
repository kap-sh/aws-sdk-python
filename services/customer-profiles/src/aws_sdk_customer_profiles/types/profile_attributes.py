"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ProfileAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.address_dimension
    import aws_sdk_customer_profiles.types.custom_attributes
    import aws_sdk_customer_profiles.types.date_dimension
    import aws_sdk_customer_profiles.types.extra_length_value_profile_dimension
    import aws_sdk_customer_profiles.types.profile_dimension
    import aws_sdk_customer_profiles.types.profile_type_dimension


class ProfileAttributes(TypedDict, closed=True):
    account_number: NotRequired[
        "aws_sdk_customer_profiles.types.profile_dimension.ProfileDimension"
    ]
    """<p>A field to describe values to segment on within account number.</p>"""
    additional_information: NotRequired[
        "aws_sdk_customer_profiles.types.extra_length_value_profile_dimension.ExtraLengthValueProfileDimension"
    ]
    """<p>A field to describe values to segment on within additional information.</p>"""
    first_name: NotRequired[
        "aws_sdk_customer_profiles.types.profile_dimension.ProfileDimension"
    ]
    """<p>A field to describe values to segment on within first name.</p>"""
    last_name: NotRequired[
        "aws_sdk_customer_profiles.types.profile_dimension.ProfileDimension"
    ]
    """<p>A field to describe values to segment on within last name.</p>"""
    middle_name: NotRequired[
        "aws_sdk_customer_profiles.types.profile_dimension.ProfileDimension"
    ]
    """<p>A field to describe values to segment on within middle name.</p>"""
    gender_string: NotRequired[
        "aws_sdk_customer_profiles.types.profile_dimension.ProfileDimension"
    ]
    """<p>A field to describe values to segment on within genderString.</p>"""
    party_type_string: NotRequired[
        "aws_sdk_customer_profiles.types.profile_dimension.ProfileDimension"
    ]
    """<p>A field to describe values to segment on within partyTypeString.</p>"""
    birth_date: NotRequired[
        "aws_sdk_customer_profiles.types.date_dimension.DateDimension"
    ]
    """<p>A field to describe values to segment on within birthDate.</p>"""
    phone_number: NotRequired[
        "aws_sdk_customer_profiles.types.profile_dimension.ProfileDimension"
    ]
    """<p>A field to describe values to segment on within phone number.</p>"""
    business_name: NotRequired[
        "aws_sdk_customer_profiles.types.profile_dimension.ProfileDimension"
    ]
    """<p>A field to describe values to segment on within business name.</p>"""
    business_phone_number: NotRequired[
        "aws_sdk_customer_profiles.types.profile_dimension.ProfileDimension"
    ]
    """<p>A field to describe values to segment on within business phone number.</p>"""
    home_phone_number: NotRequired[
        "aws_sdk_customer_profiles.types.profile_dimension.ProfileDimension"
    ]
    """<p>A field to describe values to segment on within home phone number.</p>"""
    mobile_phone_number: NotRequired[
        "aws_sdk_customer_profiles.types.profile_dimension.ProfileDimension"
    ]
    """<p>A field to describe values to segment on within mobile phone number.</p>"""
    email_address: NotRequired[
        "aws_sdk_customer_profiles.types.profile_dimension.ProfileDimension"
    ]
    """<p>A field to describe values to segment on within email address.</p>"""
    personal_email_address: NotRequired[
        "aws_sdk_customer_profiles.types.profile_dimension.ProfileDimension"
    ]
    """<p>A field to describe values to segment on within personal email address.</p>"""
    business_email_address: NotRequired[
        "aws_sdk_customer_profiles.types.profile_dimension.ProfileDimension"
    ]
    """<p>A field to describe values to segment on within business email address.</p>"""
    address: NotRequired[
        "aws_sdk_customer_profiles.types.address_dimension.AddressDimension"
    ]
    """<p>A field to describe values to segment on within address.</p>"""
    shipping_address: NotRequired[
        "aws_sdk_customer_profiles.types.address_dimension.AddressDimension"
    ]
    """<p>A field to describe values to segment on within shipping address.</p>"""
    mailing_address: NotRequired[
        "aws_sdk_customer_profiles.types.address_dimension.AddressDimension"
    ]
    """<p>A field to describe values to segment on within mailing address.</p>"""
    billing_address: NotRequired[
        "aws_sdk_customer_profiles.types.address_dimension.AddressDimension"
    ]
    """<p>A field to describe values to segment on within billing address.</p>"""
    attributes: NotRequired[
        "aws_sdk_customer_profiles.types.custom_attributes.CustomAttributes"
    ]
    """<p>A field to describe values to segment on within attributes.</p>"""
    profile_type: NotRequired[
        "aws_sdk_customer_profiles.types.profile_type_dimension.ProfileTypeDimension"
    ]
    """<p>A field to describe values to segment on within profile type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProfileAttributes) -> dict:
    out: dict = {}
    if "account_number" in value:
        import aws_sdk_customer_profiles.types.profile_dimension

        out["AccountNumber"] = (
            aws_sdk_customer_profiles.types.profile_dimension.serialize_json(
                value["account_number"]
            )
        )
    if "additional_information" in value:
        import aws_sdk_customer_profiles.types.extra_length_value_profile_dimension

        out["AdditionalInformation"] = (
            aws_sdk_customer_profiles.types.extra_length_value_profile_dimension.serialize_json(
                value["additional_information"]
            )
        )
    if "first_name" in value:
        import aws_sdk_customer_profiles.types.profile_dimension

        out["FirstName"] = (
            aws_sdk_customer_profiles.types.profile_dimension.serialize_json(
                value["first_name"]
            )
        )
    if "last_name" in value:
        import aws_sdk_customer_profiles.types.profile_dimension

        out["LastName"] = (
            aws_sdk_customer_profiles.types.profile_dimension.serialize_json(
                value["last_name"]
            )
        )
    if "middle_name" in value:
        import aws_sdk_customer_profiles.types.profile_dimension

        out["MiddleName"] = (
            aws_sdk_customer_profiles.types.profile_dimension.serialize_json(
                value["middle_name"]
            )
        )
    if "gender_string" in value:
        import aws_sdk_customer_profiles.types.profile_dimension

        out["GenderString"] = (
            aws_sdk_customer_profiles.types.profile_dimension.serialize_json(
                value["gender_string"]
            )
        )
    if "party_type_string" in value:
        import aws_sdk_customer_profiles.types.profile_dimension

        out["PartyTypeString"] = (
            aws_sdk_customer_profiles.types.profile_dimension.serialize_json(
                value["party_type_string"]
            )
        )
    if "birth_date" in value:
        import aws_sdk_customer_profiles.types.date_dimension

        out["BirthDate"] = (
            aws_sdk_customer_profiles.types.date_dimension.serialize_json(
                value["birth_date"]
            )
        )
    if "phone_number" in value:
        import aws_sdk_customer_profiles.types.profile_dimension

        out["PhoneNumber"] = (
            aws_sdk_customer_profiles.types.profile_dimension.serialize_json(
                value["phone_number"]
            )
        )
    if "business_name" in value:
        import aws_sdk_customer_profiles.types.profile_dimension

        out["BusinessName"] = (
            aws_sdk_customer_profiles.types.profile_dimension.serialize_json(
                value["business_name"]
            )
        )
    if "business_phone_number" in value:
        import aws_sdk_customer_profiles.types.profile_dimension

        out["BusinessPhoneNumber"] = (
            aws_sdk_customer_profiles.types.profile_dimension.serialize_json(
                value["business_phone_number"]
            )
        )
    if "home_phone_number" in value:
        import aws_sdk_customer_profiles.types.profile_dimension

        out["HomePhoneNumber"] = (
            aws_sdk_customer_profiles.types.profile_dimension.serialize_json(
                value["home_phone_number"]
            )
        )
    if "mobile_phone_number" in value:
        import aws_sdk_customer_profiles.types.profile_dimension

        out["MobilePhoneNumber"] = (
            aws_sdk_customer_profiles.types.profile_dimension.serialize_json(
                value["mobile_phone_number"]
            )
        )
    if "email_address" in value:
        import aws_sdk_customer_profiles.types.profile_dimension

        out["EmailAddress"] = (
            aws_sdk_customer_profiles.types.profile_dimension.serialize_json(
                value["email_address"]
            )
        )
    if "personal_email_address" in value:
        import aws_sdk_customer_profiles.types.profile_dimension

        out["PersonalEmailAddress"] = (
            aws_sdk_customer_profiles.types.profile_dimension.serialize_json(
                value["personal_email_address"]
            )
        )
    if "business_email_address" in value:
        import aws_sdk_customer_profiles.types.profile_dimension

        out["BusinessEmailAddress"] = (
            aws_sdk_customer_profiles.types.profile_dimension.serialize_json(
                value["business_email_address"]
            )
        )
    if "address" in value:
        import aws_sdk_customer_profiles.types.address_dimension

        out["Address"] = (
            aws_sdk_customer_profiles.types.address_dimension.serialize_json(
                value["address"]
            )
        )
    if "shipping_address" in value:
        import aws_sdk_customer_profiles.types.address_dimension

        out["ShippingAddress"] = (
            aws_sdk_customer_profiles.types.address_dimension.serialize_json(
                value["shipping_address"]
            )
        )
    if "mailing_address" in value:
        import aws_sdk_customer_profiles.types.address_dimension

        out["MailingAddress"] = (
            aws_sdk_customer_profiles.types.address_dimension.serialize_json(
                value["mailing_address"]
            )
        )
    if "billing_address" in value:
        import aws_sdk_customer_profiles.types.address_dimension

        out["BillingAddress"] = (
            aws_sdk_customer_profiles.types.address_dimension.serialize_json(
                value["billing_address"]
            )
        )
    if "attributes" in value:
        import aws_sdk_customer_profiles.types.custom_attributes

        out["Attributes"] = (
            aws_sdk_customer_profiles.types.custom_attributes.serialize_json(
                value["attributes"]
            )
        )
    if "profile_type" in value:
        import aws_sdk_customer_profiles.types.profile_type_dimension

        out["ProfileType"] = (
            aws_sdk_customer_profiles.types.profile_type_dimension.serialize_json(
                value["profile_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> ProfileAttributes:
    out: ProfileAttributes = {}  # type: ignore[typeddict-item]
    if "AccountNumber" in data:
        import aws_sdk_customer_profiles.types.profile_dimension

        out["account_number"] = (
            aws_sdk_customer_profiles.types.profile_dimension.deserialize_json(
                data["AccountNumber"]
            )
        )
    if "AdditionalInformation" in data:
        import aws_sdk_customer_profiles.types.extra_length_value_profile_dimension

        out["additional_information"] = (
            aws_sdk_customer_profiles.types.extra_length_value_profile_dimension.deserialize_json(
                data["AdditionalInformation"]
            )
        )
    if "FirstName" in data:
        import aws_sdk_customer_profiles.types.profile_dimension

        out["first_name"] = (
            aws_sdk_customer_profiles.types.profile_dimension.deserialize_json(
                data["FirstName"]
            )
        )
    if "LastName" in data:
        import aws_sdk_customer_profiles.types.profile_dimension

        out["last_name"] = (
            aws_sdk_customer_profiles.types.profile_dimension.deserialize_json(
                data["LastName"]
            )
        )
    if "MiddleName" in data:
        import aws_sdk_customer_profiles.types.profile_dimension

        out["middle_name"] = (
            aws_sdk_customer_profiles.types.profile_dimension.deserialize_json(
                data["MiddleName"]
            )
        )
    if "GenderString" in data:
        import aws_sdk_customer_profiles.types.profile_dimension

        out["gender_string"] = (
            aws_sdk_customer_profiles.types.profile_dimension.deserialize_json(
                data["GenderString"]
            )
        )
    if "PartyTypeString" in data:
        import aws_sdk_customer_profiles.types.profile_dimension

        out["party_type_string"] = (
            aws_sdk_customer_profiles.types.profile_dimension.deserialize_json(
                data["PartyTypeString"]
            )
        )
    if "BirthDate" in data:
        import aws_sdk_customer_profiles.types.date_dimension

        out["birth_date"] = (
            aws_sdk_customer_profiles.types.date_dimension.deserialize_json(
                data["BirthDate"]
            )
        )
    if "PhoneNumber" in data:
        import aws_sdk_customer_profiles.types.profile_dimension

        out["phone_number"] = (
            aws_sdk_customer_profiles.types.profile_dimension.deserialize_json(
                data["PhoneNumber"]
            )
        )
    if "BusinessName" in data:
        import aws_sdk_customer_profiles.types.profile_dimension

        out["business_name"] = (
            aws_sdk_customer_profiles.types.profile_dimension.deserialize_json(
                data["BusinessName"]
            )
        )
    if "BusinessPhoneNumber" in data:
        import aws_sdk_customer_profiles.types.profile_dimension

        out["business_phone_number"] = (
            aws_sdk_customer_profiles.types.profile_dimension.deserialize_json(
                data["BusinessPhoneNumber"]
            )
        )
    if "HomePhoneNumber" in data:
        import aws_sdk_customer_profiles.types.profile_dimension

        out["home_phone_number"] = (
            aws_sdk_customer_profiles.types.profile_dimension.deserialize_json(
                data["HomePhoneNumber"]
            )
        )
    if "MobilePhoneNumber" in data:
        import aws_sdk_customer_profiles.types.profile_dimension

        out["mobile_phone_number"] = (
            aws_sdk_customer_profiles.types.profile_dimension.deserialize_json(
                data["MobilePhoneNumber"]
            )
        )
    if "EmailAddress" in data:
        import aws_sdk_customer_profiles.types.profile_dimension

        out["email_address"] = (
            aws_sdk_customer_profiles.types.profile_dimension.deserialize_json(
                data["EmailAddress"]
            )
        )
    if "PersonalEmailAddress" in data:
        import aws_sdk_customer_profiles.types.profile_dimension

        out["personal_email_address"] = (
            aws_sdk_customer_profiles.types.profile_dimension.deserialize_json(
                data["PersonalEmailAddress"]
            )
        )
    if "BusinessEmailAddress" in data:
        import aws_sdk_customer_profiles.types.profile_dimension

        out["business_email_address"] = (
            aws_sdk_customer_profiles.types.profile_dimension.deserialize_json(
                data["BusinessEmailAddress"]
            )
        )
    if "Address" in data:
        import aws_sdk_customer_profiles.types.address_dimension

        out["address"] = (
            aws_sdk_customer_profiles.types.address_dimension.deserialize_json(
                data["Address"]
            )
        )
    if "ShippingAddress" in data:
        import aws_sdk_customer_profiles.types.address_dimension

        out["shipping_address"] = (
            aws_sdk_customer_profiles.types.address_dimension.deserialize_json(
                data["ShippingAddress"]
            )
        )
    if "MailingAddress" in data:
        import aws_sdk_customer_profiles.types.address_dimension

        out["mailing_address"] = (
            aws_sdk_customer_profiles.types.address_dimension.deserialize_json(
                data["MailingAddress"]
            )
        )
    if "BillingAddress" in data:
        import aws_sdk_customer_profiles.types.address_dimension

        out["billing_address"] = (
            aws_sdk_customer_profiles.types.address_dimension.deserialize_json(
                data["BillingAddress"]
            )
        )
    if "Attributes" in data:
        import aws_sdk_customer_profiles.types.custom_attributes

        out["attributes"] = (
            aws_sdk_customer_profiles.types.custom_attributes.deserialize_json(
                data["Attributes"]
            )
        )
    if "ProfileType" in data:
        import aws_sdk_customer_profiles.types.profile_type_dimension

        out["profile_type"] = (
            aws_sdk_customer_profiles.types.profile_type_dimension.deserialize_json(
                data["ProfileType"]
            )
        )
    return out
