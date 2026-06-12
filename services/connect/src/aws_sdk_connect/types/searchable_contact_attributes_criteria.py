"""Generated from Smithy shape ``com.amazonaws.connect#SearchableContactAttributesCriteria``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.searchable_contact_attribute_key
    import aws_sdk_connect.types.searchable_contact_attribute_value_list


class SearchableContactAttributesCriteria(TypedDict):
    key: "aws_sdk_connect.types.searchable_contact_attribute_key.SearchableContactAttributeKey"
    """<p>The key containing a searchable user-defined contact attribute.</p>"""
    values: "aws_sdk_connect.types.searchable_contact_attribute_value_list.SearchableContactAttributeValueList"
    """<p>The list of values to search for within a user-defined contact attribute.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchableContactAttributesCriteria) -> dict:
    out: dict = {}
    out["Key"] = value["key"]
    import aws_sdk_connect.types.searchable_contact_attribute_value_list

    out["Values"] = (
        aws_sdk_connect.types.searchable_contact_attribute_value_list.serialize_json(
            value["values"]
        )
    )
    return out


def deserialize_json(data: dict) -> SearchableContactAttributesCriteria:
    out: SearchableContactAttributesCriteria = {}  # type: ignore[typeddict-item]
    if "Key" in data:
        out["key"] = data["Key"]
    else:
        raise DeserializationError("SearchableContactAttributesCriteria.key required")
    if "Values" in data:
        import aws_sdk_connect.types.searchable_contact_attribute_value_list

        out["values"] = (
            aws_sdk_connect.types.searchable_contact_attribute_value_list.deserialize_json(
                data["Values"]
            )
        )
    else:
        raise DeserializationError(
            "SearchableContactAttributesCriteria.values required"
        )
    return out
