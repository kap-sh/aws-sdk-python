"""Generated from Smithy shape ``com.amazonaws.customerprofiles#CreateProfileRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.address
    import aws_sdk_customer_profiles.types.attributes
    import aws_sdk_customer_profiles.types.engagement_preferences
    import aws_sdk_customer_profiles.types.gender
    import aws_sdk_customer_profiles.types.name
    import aws_sdk_customer_profiles.types.party_type
    import aws_sdk_customer_profiles.types.profile_type
    import aws_sdk_customer_profiles.types.sensitive_string1_to255
    import aws_sdk_customer_profiles.types.sensitive_string1_to1000


class CreateProfileRequest(TypedDict):
    domain_name: "aws_sdk_customer_profiles.types.name.name"
    """<p>The unique name of the domain.</p>"""
    account_number: NotRequired[
        "aws_sdk_customer_profiles.types.sensitive_string1_to255.sensitiveString1To255"
    ]
    """<p>An account number that you have assigned to the customer.</p>"""
    additional_information: NotRequired[
        "aws_sdk_customer_profiles.types.sensitive_string1_to1000.sensitiveString1To1000"
    ]
    """<p>Any additional information relevant to the customer’s profile.</p>"""
    party_type: NotRequired["aws_sdk_customer_profiles.types.party_type.PartyType"]
    """<p>The type of profile used to describe the customer.</p>"""
    business_name: NotRequired[
        "aws_sdk_customer_profiles.types.sensitive_string1_to255.sensitiveString1To255"
    ]
    """<p>The name of the customer’s business.</p>"""
    first_name: NotRequired[
        "aws_sdk_customer_profiles.types.sensitive_string1_to255.sensitiveString1To255"
    ]
    """<p>The customer’s first name.</p>"""
    middle_name: NotRequired[
        "aws_sdk_customer_profiles.types.sensitive_string1_to255.sensitiveString1To255"
    ]
    """<p>The customer’s middle name.</p>"""
    last_name: NotRequired[
        "aws_sdk_customer_profiles.types.sensitive_string1_to255.sensitiveString1To255"
    ]
    """<p>The customer’s last name.</p>"""
    birth_date: NotRequired[
        "aws_sdk_customer_profiles.types.sensitive_string1_to255.sensitiveString1To255"
    ]
    """<p>The customer’s birth date. </p>"""
    gender: NotRequired["aws_sdk_customer_profiles.types.gender.Gender"]
    """<p>The gender with which the customer identifies. </p>"""
    phone_number: NotRequired[
        "aws_sdk_customer_profiles.types.sensitive_string1_to255.sensitiveString1To255"
    ]
    """<p>The customer’s phone number, which has not been specified as a mobile, home, or business number. </p>"""
    mobile_phone_number: NotRequired[
        "aws_sdk_customer_profiles.types.sensitive_string1_to255.sensitiveString1To255"
    ]
    """<p>The customer’s mobile phone number.</p>"""
    home_phone_number: NotRequired[
        "aws_sdk_customer_profiles.types.sensitive_string1_to255.sensitiveString1To255"
    ]
    """<p>The customer’s home phone number.</p>"""
    business_phone_number: NotRequired[
        "aws_sdk_customer_profiles.types.sensitive_string1_to255.sensitiveString1To255"
    ]
    """<p>The customer’s business phone number.</p>"""
    email_address: NotRequired[
        "aws_sdk_customer_profiles.types.sensitive_string1_to255.sensitiveString1To255"
    ]
    """<p>The customer’s email address, which has not been specified as a personal or business address. </p>"""
    personal_email_address: NotRequired[
        "aws_sdk_customer_profiles.types.sensitive_string1_to255.sensitiveString1To255"
    ]
    """<p>The customer’s personal email address.</p>"""
    business_email_address: NotRequired[
        "aws_sdk_customer_profiles.types.sensitive_string1_to255.sensitiveString1To255"
    ]
    """<p>The customer’s business email address.</p>"""
    address: NotRequired["aws_sdk_customer_profiles.types.address.Address"]
    """<p>A generic address associated with the customer that is not mailing, shipping, or billing.</p>"""
    shipping_address: NotRequired["aws_sdk_customer_profiles.types.address.Address"]
    """<p>The customer’s shipping address.</p>"""
    mailing_address: NotRequired["aws_sdk_customer_profiles.types.address.Address"]
    """<p>The customer’s mailing address.</p>"""
    billing_address: NotRequired["aws_sdk_customer_profiles.types.address.Address"]
    """<p>The customer’s billing address.</p>"""
    attributes: NotRequired["aws_sdk_customer_profiles.types.attributes.Attributes"]
    """<p>A key value pair of attributes of a customer profile.</p>"""
    party_type_string: NotRequired[
        "aws_sdk_customer_profiles.types.sensitive_string1_to255.sensitiveString1To255"
    ]
    """<p>An alternative to <code>PartyType</code> which accepts any string as input.</p>"""
    gender_string: NotRequired[
        "aws_sdk_customer_profiles.types.sensitive_string1_to255.sensitiveString1To255"
    ]
    """<p>An alternative to <code>Gender</code> which accepts any string as input.</p>"""
    profile_type: NotRequired[
        "aws_sdk_customer_profiles.types.profile_type.ProfileType"
    ]
    """<p>The type of the profile.</p>"""
    engagement_preferences: NotRequired[
        "aws_sdk_customer_profiles.types.engagement_preferences.EngagementPreferences"
    ]
    """<p>Object that defines the preferred methods of engagement, per channel.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateProfileRequest) -> dict:
    out: dict = {}
    if "account_number" in value:
        out["AccountNumber"] = value["account_number"]
    if "additional_information" in value:
        out["AdditionalInformation"] = value["additional_information"]
    if "party_type" in value:
        import aws_sdk_customer_profiles.types.party_type

        out["PartyType"] = aws_sdk_customer_profiles.types.party_type.serialize_json(
            value["party_type"]
        )
    if "business_name" in value:
        out["BusinessName"] = value["business_name"]
    if "first_name" in value:
        out["FirstName"] = value["first_name"]
    if "middle_name" in value:
        out["MiddleName"] = value["middle_name"]
    if "last_name" in value:
        out["LastName"] = value["last_name"]
    if "birth_date" in value:
        out["BirthDate"] = value["birth_date"]
    if "gender" in value:
        import aws_sdk_customer_profiles.types.gender

        out["Gender"] = aws_sdk_customer_profiles.types.gender.serialize_json(
            value["gender"]
        )
    if "phone_number" in value:
        out["PhoneNumber"] = value["phone_number"]
    if "mobile_phone_number" in value:
        out["MobilePhoneNumber"] = value["mobile_phone_number"]
    if "home_phone_number" in value:
        out["HomePhoneNumber"] = value["home_phone_number"]
    if "business_phone_number" in value:
        out["BusinessPhoneNumber"] = value["business_phone_number"]
    if "email_address" in value:
        out["EmailAddress"] = value["email_address"]
    if "personal_email_address" in value:
        out["PersonalEmailAddress"] = value["personal_email_address"]
    if "business_email_address" in value:
        out["BusinessEmailAddress"] = value["business_email_address"]
    if "address" in value:
        import aws_sdk_customer_profiles.types.address

        out["Address"] = aws_sdk_customer_profiles.types.address.serialize_json(
            value["address"]
        )
    if "shipping_address" in value:
        import aws_sdk_customer_profiles.types.address

        out["ShippingAddress"] = aws_sdk_customer_profiles.types.address.serialize_json(
            value["shipping_address"]
        )
    if "mailing_address" in value:
        import aws_sdk_customer_profiles.types.address

        out["MailingAddress"] = aws_sdk_customer_profiles.types.address.serialize_json(
            value["mailing_address"]
        )
    if "billing_address" in value:
        import aws_sdk_customer_profiles.types.address

        out["BillingAddress"] = aws_sdk_customer_profiles.types.address.serialize_json(
            value["billing_address"]
        )
    if "attributes" in value:
        import aws_sdk_customer_profiles.types.attributes

        out["Attributes"] = aws_sdk_customer_profiles.types.attributes.serialize_json(
            value["attributes"]
        )
    if "party_type_string" in value:
        out["PartyTypeString"] = value["party_type_string"]
    if "gender_string" in value:
        out["GenderString"] = value["gender_string"]
    if "profile_type" in value:
        import aws_sdk_customer_profiles.types.profile_type

        out["ProfileType"] = (
            aws_sdk_customer_profiles.types.profile_type.serialize_json(
                value["profile_type"]
            )
        )
    if "engagement_preferences" in value:
        import aws_sdk_customer_profiles.types.engagement_preferences

        out["EngagementPreferences"] = (
            aws_sdk_customer_profiles.types.engagement_preferences.serialize_json(
                value["engagement_preferences"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateProfileRequest:
    out: CreateProfileRequest = {}  # type: ignore[typeddict-item]
    if "AccountNumber" in data:
        out["account_number"] = data["AccountNumber"]
    if "AdditionalInformation" in data:
        out["additional_information"] = data["AdditionalInformation"]
    if "PartyType" in data:
        import aws_sdk_customer_profiles.types.party_type

        out["party_type"] = aws_sdk_customer_profiles.types.party_type.deserialize_json(
            data["PartyType"]
        )
    if "BusinessName" in data:
        out["business_name"] = data["BusinessName"]
    if "FirstName" in data:
        out["first_name"] = data["FirstName"]
    if "MiddleName" in data:
        out["middle_name"] = data["MiddleName"]
    if "LastName" in data:
        out["last_name"] = data["LastName"]
    if "BirthDate" in data:
        out["birth_date"] = data["BirthDate"]
    if "Gender" in data:
        import aws_sdk_customer_profiles.types.gender

        out["gender"] = aws_sdk_customer_profiles.types.gender.deserialize_json(
            data["Gender"]
        )
    if "PhoneNumber" in data:
        out["phone_number"] = data["PhoneNumber"]
    if "MobilePhoneNumber" in data:
        out["mobile_phone_number"] = data["MobilePhoneNumber"]
    if "HomePhoneNumber" in data:
        out["home_phone_number"] = data["HomePhoneNumber"]
    if "BusinessPhoneNumber" in data:
        out["business_phone_number"] = data["BusinessPhoneNumber"]
    if "EmailAddress" in data:
        out["email_address"] = data["EmailAddress"]
    if "PersonalEmailAddress" in data:
        out["personal_email_address"] = data["PersonalEmailAddress"]
    if "BusinessEmailAddress" in data:
        out["business_email_address"] = data["BusinessEmailAddress"]
    if "Address" in data:
        import aws_sdk_customer_profiles.types.address

        out["address"] = aws_sdk_customer_profiles.types.address.deserialize_json(
            data["Address"]
        )
    if "ShippingAddress" in data:
        import aws_sdk_customer_profiles.types.address

        out["shipping_address"] = (
            aws_sdk_customer_profiles.types.address.deserialize_json(
                data["ShippingAddress"]
            )
        )
    if "MailingAddress" in data:
        import aws_sdk_customer_profiles.types.address

        out["mailing_address"] = (
            aws_sdk_customer_profiles.types.address.deserialize_json(
                data["MailingAddress"]
            )
        )
    if "BillingAddress" in data:
        import aws_sdk_customer_profiles.types.address

        out["billing_address"] = (
            aws_sdk_customer_profiles.types.address.deserialize_json(
                data["BillingAddress"]
            )
        )
    if "Attributes" in data:
        import aws_sdk_customer_profiles.types.attributes

        out["attributes"] = aws_sdk_customer_profiles.types.attributes.deserialize_json(
            data["Attributes"]
        )
    if "PartyTypeString" in data:
        out["party_type_string"] = data["PartyTypeString"]
    if "GenderString" in data:
        out["gender_string"] = data["GenderString"]
    if "ProfileType" in data:
        import aws_sdk_customer_profiles.types.profile_type

        out["profile_type"] = (
            aws_sdk_customer_profiles.types.profile_type.deserialize_json(
                data["ProfileType"]
            )
        )
    if "EngagementPreferences" in data:
        import aws_sdk_customer_profiles.types.engagement_preferences

        out["engagement_preferences"] = (
            aws_sdk_customer_profiles.types.engagement_preferences.deserialize_json(
                data["EngagementPreferences"]
            )
        )
    return out
