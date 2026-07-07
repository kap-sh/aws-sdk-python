"""Generated from Smithy shape ``com.amazonaws.glue#TransformSortCriteria``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.sort_direction_type
    import aws_sdk_glue.types.transform_sort_column_type


class TransformSortCriteria(TypedDict, closed=True):
    column: "aws_sdk_glue.types.transform_sort_column_type.TransformSortColumnType"
    """<p>The column to be used in the sorting criteria that are associated with the machine learning transform.</p>"""
    sort_direction: "aws_sdk_glue.types.sort_direction_type.SortDirectionType"
    """<p>The sort direction to be used in the sorting criteria that are associated with the machine learning transform.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TransformSortCriteria) -> dict:
    out: dict = {}
    import aws_sdk_glue.types.transform_sort_column_type

    out["Column"] = (
        aws_sdk_glue.types.transform_sort_column_type.serialize_aws_json_1_1(
            value["column"]
        )
    )
    import aws_sdk_glue.types.sort_direction_type

    out["SortDirection"] = (
        aws_sdk_glue.types.sort_direction_type.serialize_aws_json_1_1(
            value["sort_direction"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> TransformSortCriteria:
    out: TransformSortCriteria = {}  # type: ignore[typeddict-item]
    if "Column" in data:
        import aws_sdk_glue.types.transform_sort_column_type

        out["column"] = (
            aws_sdk_glue.types.transform_sort_column_type.deserialize_aws_json_1_1(
                data["Column"]
            )
        )
    else:
        raise DeserializationError("TransformSortCriteria.column required")
    if "SortDirection" in data:
        import aws_sdk_glue.types.sort_direction_type

        out["sort_direction"] = (
            aws_sdk_glue.types.sort_direction_type.deserialize_aws_json_1_1(
                data["SortDirection"]
            )
        )
    else:
        raise DeserializationError("TransformSortCriteria.sort_direction required")
    return out
