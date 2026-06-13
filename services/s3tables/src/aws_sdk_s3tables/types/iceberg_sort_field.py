"""Generated from Smithy shape ``com.amazonaws.s3tables#IcebergSortField``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_s3tables.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_s3tables.types.iceberg_null_order
    import aws_sdk_s3tables.types.iceberg_sort_direction


class IcebergSortField(TypedDict):
    source_id: "int"
    """<p>The ID of the source schema field to sort by. This must reference a valid field ID from the table schema.</p>"""
    transform: "str"
    """<p>The transform to apply to the source field before sorting. Use <code>identity</code> to sort by the field value directly, or specify other transforms as needed.</p>"""
    direction: "aws_sdk_s3tables.types.iceberg_sort_direction.IcebergSortDirection"
    """<p>The sort direction. Valid values are <code>asc</code> for ascending order or <code>desc</code> for descending order.</p>"""
    null_order: "aws_sdk_s3tables.types.iceberg_null_order.IcebergNullOrder"
    """<p>Specifies how null values are ordered. Valid values are <code>nulls-first</code> to place nulls before non-null values, or <code>nulls-last</code> to place nulls after non-null values.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IcebergSortField) -> dict:
    out: dict = {}
    out["source-id"] = value["source_id"]
    out["transform"] = value["transform"]
    import aws_sdk_s3tables.types.iceberg_sort_direction

    out["direction"] = aws_sdk_s3tables.types.iceberg_sort_direction.serialize_json(
        value["direction"]
    )
    import aws_sdk_s3tables.types.iceberg_null_order

    out["null-order"] = aws_sdk_s3tables.types.iceberg_null_order.serialize_json(
        value["null_order"]
    )
    return out


def deserialize_json(data: dict) -> IcebergSortField:
    out: IcebergSortField = {}  # type: ignore[typeddict-item]
    if "source-id" in data:
        out["source_id"] = data["source-id"]
    else:
        raise DeserializationError("IcebergSortField.source_id required")
    if "transform" in data:
        out["transform"] = data["transform"]
    else:
        raise DeserializationError("IcebergSortField.transform required")
    if "direction" in data:
        import aws_sdk_s3tables.types.iceberg_sort_direction

        out["direction"] = (
            aws_sdk_s3tables.types.iceberg_sort_direction.deserialize_json(
                data["direction"]
            )
        )
    else:
        raise DeserializationError("IcebergSortField.direction required")
    if "null-order" in data:
        import aws_sdk_s3tables.types.iceberg_null_order

        out["null_order"] = aws_sdk_s3tables.types.iceberg_null_order.deserialize_json(
            data["null-order"]
        )
    else:
        raise DeserializationError("IcebergSortField.null_order required")
    return out
