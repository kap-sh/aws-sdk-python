"""Generated from Smithy shape ``com.amazonaws.customerprofiles#SortAttribute``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_customer_profiles.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.field_name
    import aws_sdk_customer_profiles.types.segment_sort_data_type
    import aws_sdk_customer_profiles.types.segment_sort_order
    import aws_sdk_customer_profiles.types.sort_attribute_type


class SortAttribute(TypedDict, closed=True):
    name: "aws_sdk_customer_profiles.types.field_name.fieldName"
    """<p>The name of the attribute to sort by.</p>"""
    data_type: NotRequired[
        "aws_sdk_customer_profiles.types.segment_sort_data_type.SegmentSortDataType"
    ]
    """<p>The data type of the sort attribute (e.g., string, number, date).</p>"""
    order: "aws_sdk_customer_profiles.types.segment_sort_order.SegmentSortOrder"
    """<p>The sort order for the attribute (ascending or descending).</p>"""
    type: "aws_sdk_customer_profiles.types.sort_attribute_type.SortAttributeType"
    """<p>The type of attribute (e.g., profile, calculated).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SortAttribute) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "data_type" in value:
        import aws_sdk_customer_profiles.types.segment_sort_data_type

        out["DataType"] = (
            aws_sdk_customer_profiles.types.segment_sort_data_type.serialize_json(
                value["data_type"]
            )
        )
    import aws_sdk_customer_profiles.types.segment_sort_order

    out["Order"] = aws_sdk_customer_profiles.types.segment_sort_order.serialize_json(
        value["order"]
    )
    import aws_sdk_customer_profiles.types.sort_attribute_type

    out["Type"] = aws_sdk_customer_profiles.types.sort_attribute_type.serialize_json(
        value.get("type", "PROFILE")
    )
    return out


def deserialize_json(data: dict) -> SortAttribute:
    out: SortAttribute = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("SortAttribute.name required")
    if "DataType" in data:
        import aws_sdk_customer_profiles.types.segment_sort_data_type

        out["data_type"] = (
            aws_sdk_customer_profiles.types.segment_sort_data_type.deserialize_json(
                data["DataType"]
            )
        )
    if "Order" in data:
        import aws_sdk_customer_profiles.types.segment_sort_order

        out["order"] = (
            aws_sdk_customer_profiles.types.segment_sort_order.deserialize_json(
                data["Order"]
            )
        )
    else:
        raise DeserializationError("SortAttribute.order required")
    if "Type" in data:
        import aws_sdk_customer_profiles.types.sort_attribute_type

        out["type"] = (
            aws_sdk_customer_profiles.types.sort_attribute_type.deserialize_json(
                data["Type"]
            )
        )
    else:
        out["type"] = "PROFILE"
    return out
