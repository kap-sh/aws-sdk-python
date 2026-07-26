"""Generated from Smithy shape ``com.amazonaws.glue#IcebergSortField``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_glue.errors import DeserializationError

if TYPE_CHECKING:
    import capo_glue.types.iceberg_null_order
    import capo_glue.types.iceberg_sort_direction
    import capo_glue.types.iceberg_transform_string
    import capo_glue.types.integer


class IcebergSortField(TypedDict, closed=True):
    source_id: "capo_glue.types.integer.Integer"
    """<p>The identifier of the source field from the table schema that this sort field is based on.</p>"""
    transform: "capo_glue.types.iceberg_transform_string.IcebergTransformString"
    """<p>The transformation function applied to the source field before sorting, such as identity, bucket, or truncate.</p>"""
    direction: "capo_glue.types.iceberg_sort_direction.IcebergSortDirection"
    """<p>The sort direction for this field, either ascending or descending.</p>"""
    null_order: "capo_glue.types.iceberg_null_order.IcebergNullOrder"
    """<p>The ordering behavior for null values in this field, specifying whether nulls should appear first or last in the sort order.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IcebergSortField) -> dict:
    out: dict = {}
    out["SourceId"] = value.get("source_id", 0)
    out["Transform"] = value["transform"]
    import capo_glue.types.iceberg_sort_direction

    out["Direction"] = capo_glue.types.iceberg_sort_direction.serialize_aws_json_1_1(
        value["direction"]
    )
    import capo_glue.types.iceberg_null_order

    out["NullOrder"] = capo_glue.types.iceberg_null_order.serialize_aws_json_1_1(
        value["null_order"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> IcebergSortField:
    out: IcebergSortField = {}  # type: ignore[typeddict-item]
    if "SourceId" in data:
        out["source_id"] = data["SourceId"]
    else:
        out["source_id"] = 0
    if "Transform" in data:
        out["transform"] = data["Transform"]
    else:
        raise DeserializationError("IcebergSortField.transform required")
    if "Direction" in data:
        import capo_glue.types.iceberg_sort_direction

        out["direction"] = (
            capo_glue.types.iceberg_sort_direction.deserialize_aws_json_1_1(
                data["Direction"]
            )
        )
    else:
        raise DeserializationError("IcebergSortField.direction required")
    if "NullOrder" in data:
        import capo_glue.types.iceberg_null_order

        out["null_order"] = capo_glue.types.iceberg_null_order.deserialize_aws_json_1_1(
            data["NullOrder"]
        )
    else:
        raise DeserializationError("IcebergSortField.null_order required")
    return out
