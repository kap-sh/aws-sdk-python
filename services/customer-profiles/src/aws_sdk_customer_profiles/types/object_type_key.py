"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ObjectTypeKey``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.field_name_list
    import aws_sdk_customer_profiles.types.standard_identifier_list


class ObjectTypeKey(TypedDict, closed=True):
    standard_identifiers: NotRequired[
        "aws_sdk_customer_profiles.types.standard_identifier_list.StandardIdentifierList"
    ]
    """<p>The types of keys that a ProfileObject can have. Each ProfileObject can have only 1 UNIQUE key but multiple PROFILE keys. PROFILE, ASSET, CASE, or ORDER means that this key can be used to tie an object to a PROFILE, ASSET, CASE, or ORDER respectively. UNIQUE means that it can be used to uniquely identify an object. If a key a is marked as SECONDARY, it will be used to search for profiles after all other PROFILE keys have been searched. A LOOKUP_ONLY key is only used to match a profile but is not persisted to be used for searching of the profile. A NEW_ONLY key is only used if the profile does not already exist before the object is ingested, otherwise it is only used for matching objects to profiles.</p>"""
    field_names: NotRequired[
        "aws_sdk_customer_profiles.types.field_name_list.FieldNameList"
    ]
    """<p>The reference for the key name of the fields map.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ObjectTypeKey) -> dict:
    out: dict = {}
    if "standard_identifiers" in value:
        import aws_sdk_customer_profiles.types.standard_identifier_list

        out["StandardIdentifiers"] = (
            aws_sdk_customer_profiles.types.standard_identifier_list.serialize_json(
                value["standard_identifiers"]
            )
        )
    if "field_names" in value:
        import aws_sdk_customer_profiles.types.field_name_list

        out["FieldNames"] = (
            aws_sdk_customer_profiles.types.field_name_list.serialize_json(
                value["field_names"]
            )
        )
    return out


def deserialize_json(data: dict) -> ObjectTypeKey:
    out: ObjectTypeKey = {}  # type: ignore[typeddict-item]
    if "StandardIdentifiers" in data:
        import aws_sdk_customer_profiles.types.standard_identifier_list

        out["standard_identifiers"] = (
            aws_sdk_customer_profiles.types.standard_identifier_list.deserialize_json(
                data["StandardIdentifiers"]
            )
        )
    if "FieldNames" in data:
        import aws_sdk_customer_profiles.types.field_name_list

        out["field_names"] = (
            aws_sdk_customer_profiles.types.field_name_list.deserialize_json(
                data["FieldNames"]
            )
        )
    return out
