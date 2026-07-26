"""Generated from Smithy shape ``com.amazonaws.connect#PrimaryAttributeValue``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.access_type
    import capo_connect.types.primary_attribute_context_key_name
    import capo_connect.types.primary_value_list


class PrimaryAttributeValue(TypedDict, closed=True):
    access_type: NotRequired["capo_connect.types.access_type.AccessType"]
    """<p>The value's access type.</p>"""
    attribute_name: NotRequired[
        "capo_connect.types.primary_attribute_context_key_name.PrimaryAttributeContextKeyName"
    ]
    """<p>The value's attribute name.</p>"""
    values: NotRequired["capo_connect.types.primary_value_list.PrimaryValueList"]
    """<p>The value's values.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PrimaryAttributeValue) -> dict:
    out: dict = {}
    if "access_type" in value:
        import capo_connect.types.access_type

        out["AccessType"] = capo_connect.types.access_type.serialize_json(
            value["access_type"]
        )
    if "attribute_name" in value:
        out["AttributeName"] = value["attribute_name"]
    if "values" in value:
        import capo_connect.types.primary_value_list

        out["Values"] = capo_connect.types.primary_value_list.serialize_json(
            value["values"]
        )
    return out


def deserialize_json(data: dict) -> PrimaryAttributeValue:
    out: PrimaryAttributeValue = {}  # type: ignore[typeddict-item]
    if "AccessType" in data:
        import capo_connect.types.access_type

        out["access_type"] = capo_connect.types.access_type.deserialize_json(
            data["AccessType"]
        )
    if "AttributeName" in data:
        out["attribute_name"] = data["AttributeName"]
    if "Values" in data:
        import capo_connect.types.primary_value_list

        out["values"] = capo_connect.types.primary_value_list.deserialize_json(
            data["Values"]
        )
    return out
