"""Generated from Smithy shape ``com.amazonaws.glue#IcebergSortOrder``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.iceberg_sort_order_field_list
    import aws_sdk_glue.types.integer


class IcebergSortOrder(TypedDict):
    order_id: "aws_sdk_glue.types.integer.Integer"
    """<p>The unique identifier for this sort order specification within the Iceberg table's metadata.</p>"""
    fields: "aws_sdk_glue.types.iceberg_sort_order_field_list.IcebergSortOrderFieldList"
    """<p>The list of fields and their sort directions that define the ordering criteria for the Iceberg table data.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IcebergSortOrder) -> dict:
    out: dict = {}
    out["OrderId"] = value.get("order_id", 0)
    import aws_sdk_glue.types.iceberg_sort_order_field_list

    out["Fields"] = (
        aws_sdk_glue.types.iceberg_sort_order_field_list.serialize_aws_json_1_1(
            value["fields"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> IcebergSortOrder:
    out: IcebergSortOrder = {}  # type: ignore[typeddict-item]
    if "OrderId" in data:
        out["order_id"] = data["OrderId"]
    else:
        out["order_id"] = 0
    if "Fields" in data:
        import aws_sdk_glue.types.iceberg_sort_order_field_list

        out["fields"] = (
            aws_sdk_glue.types.iceberg_sort_order_field_list.deserialize_aws_json_1_1(
                data["Fields"]
            )
        )
    else:
        raise DeserializationError("IcebergSortOrder.fields required")
    return out
