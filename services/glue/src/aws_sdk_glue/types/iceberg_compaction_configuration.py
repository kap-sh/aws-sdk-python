"""Generated from Smithy shape ``com.amazonaws.glue#IcebergCompactionConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.compaction_strategy
    import aws_sdk_glue.types.nullable_integer


class IcebergCompactionConfiguration(TypedDict):
    strategy: NotRequired["aws_sdk_glue.types.compaction_strategy.CompactionStrategy"]
    """<p>The strategy to use for compaction. Valid values are:</p> <ul> <li> <p> <code>binpack</code>: Combines small files into larger files, typically targeting sizes over 100MB, while applying any pending deletes. This is the recommended compaction strategy for most use cases. </p> </li> <li> <p> <code>sort</code>: Organizes data based on specified columns which are sorted hierarchically during compaction, improving query performance for filtered operations. This strategy is recommended when your queries frequently filter on specific columns. To use this strategy, you must first define a sort order in your Iceberg table properties using the <code>sort_order</code> table property.</p> </li> <li> <p> <code>z-order</code>: Optimizes data organization by blending multiple attributes into a single scalar value that can be used for sorting, allowing efficient querying across multiple dimensions. This strategy is recommended when you need to query data across multiple dimensions simultaneously. To use this strategy, you must first define a sort order in your Iceberg table properties using the <code>sort_order</code> table property. </p> </li> </ul> <p>If an input is not provided, the default value 'binpack' will be used.</p>"""
    min_input_files: NotRequired["aws_sdk_glue.types.nullable_integer.NullableInteger"]
    """<p>The minimum number of data files that must be present in a partition before compaction will actually compact files. This parameter helps control when compaction is triggered, preventing unnecessary compaction operations on partitions with few files. If an input is not provided, the default value 100 will be used.</p>"""
    delete_file_threshold: NotRequired[
        "aws_sdk_glue.types.nullable_integer.NullableInteger"
    ]
    """<p>The minimum number of deletes that must be present in a data file to make it eligible for compaction. This parameter helps optimize compaction by focusing on files that contain a significant number of delete operations, which can improve query performance by removing deleted records. If an input is not provided, the default value 1 will be used.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IcebergCompactionConfiguration) -> dict:
    out: dict = {}
    if "strategy" in value:
        import aws_sdk_glue.types.compaction_strategy

        out["strategy"] = aws_sdk_glue.types.compaction_strategy.serialize_aws_json_1_1(
            value["strategy"]
        )
    if "min_input_files" in value:
        out["minInputFiles"] = value["min_input_files"]
    if "delete_file_threshold" in value:
        out["deleteFileThreshold"] = value["delete_file_threshold"]
    return out


def deserialize_aws_json_1_1(data: dict) -> IcebergCompactionConfiguration:
    out: IcebergCompactionConfiguration = {}  # type: ignore[typeddict-item]
    if "strategy" in data:
        import aws_sdk_glue.types.compaction_strategy

        out["strategy"] = (
            aws_sdk_glue.types.compaction_strategy.deserialize_aws_json_1_1(
                data["strategy"]
            )
        )
    if "minInputFiles" in data:
        out["min_input_files"] = data["minInputFiles"]
    if "deleteFileThreshold" in data:
        out["delete_file_threshold"] = data["deleteFileThreshold"]
    return out
