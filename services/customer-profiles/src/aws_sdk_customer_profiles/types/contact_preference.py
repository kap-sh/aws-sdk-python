"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ContactPreference``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.contact_type
    import aws_sdk_customer_profiles.types.name
    import aws_sdk_customer_profiles.types.string1_to255
    import aws_sdk_customer_profiles.types.uuid


class ContactPreference(TypedDict):
    key_name: NotRequired["aws_sdk_customer_profiles.types.name.name"]
    """<p>A searchable, unique identifier of a customer profile.</p>"""
    key_value: NotRequired["aws_sdk_customer_profiles.types.string1_to255.string1To255"]
    """<p>The key value used to look up profile based off the keyName.</p>"""
    profile_id: NotRequired["aws_sdk_customer_profiles.types.uuid.uuid"]
    """<p>The unique identifier of a customer profile.</p>"""
    contact_type: NotRequired[
        "aws_sdk_customer_profiles.types.contact_type.ContactType"
    ]
    """<p>The contact type used for engagement. For example: HomePhoneNumber, PersonalEmailAddress.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContactPreference) -> dict:
    out: dict = {}
    if "key_name" in value:
        out["KeyName"] = value["key_name"]
    if "key_value" in value:
        out["KeyValue"] = value["key_value"]
    if "profile_id" in value:
        out["ProfileId"] = value["profile_id"]
    if "contact_type" in value:
        import aws_sdk_customer_profiles.types.contact_type

        out["ContactType"] = (
            aws_sdk_customer_profiles.types.contact_type.serialize_json(
                value["contact_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> ContactPreference:
    out: ContactPreference = {}  # type: ignore[typeddict-item]
    if "KeyName" in data:
        out["key_name"] = data["KeyName"]
    if "KeyValue" in data:
        out["key_value"] = data["KeyValue"]
    if "ProfileId" in data:
        out["profile_id"] = data["ProfileId"]
    if "ContactType" in data:
        import aws_sdk_customer_profiles.types.contact_type

        out["contact_type"] = (
            aws_sdk_customer_profiles.types.contact_type.deserialize_json(
                data["ContactType"]
            )
        )
    return out
