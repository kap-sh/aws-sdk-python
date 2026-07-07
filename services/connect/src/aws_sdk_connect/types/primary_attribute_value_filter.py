"""Generated from Smithy shape ``com.amazonaws.connect#PrimaryAttributeValueFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.data_table_name
    import aws_sdk_connect.types.value_list


class PrimaryAttributeValueFilter(TypedDict, closed=True):
    attribute_name: "aws_sdk_connect.types.data_table_name.DataTableName"
    """<p>The filter's attribute name.</p>"""
    values: "aws_sdk_connect.types.value_list.ValueList"
    """<p>The filter's values.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PrimaryAttributeValueFilter) -> dict:
    out: dict = {}
    out["AttributeName"] = value["attribute_name"]
    import aws_sdk_connect.types.value_list

    out["Values"] = aws_sdk_connect.types.value_list.serialize_json(value["values"])
    return out


def deserialize_json(data: dict) -> PrimaryAttributeValueFilter:
    out: PrimaryAttributeValueFilter = {}  # type: ignore[typeddict-item]
    if "AttributeName" in data:
        out["attribute_name"] = data["AttributeName"]
    else:
        raise DeserializationError(
            "PrimaryAttributeValueFilter.attribute_name required"
        )
    if "Values" in data:
        import aws_sdk_connect.types.value_list

        out["values"] = aws_sdk_connect.types.value_list.deserialize_json(
            data["Values"]
        )
    else:
        raise DeserializationError("PrimaryAttributeValueFilter.values required")
    return out
