"""Generated from Smithy shape ``com.amazonaws.glue#BatchDeletePartitionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.partition_errors


class BatchDeletePartitionResponse(TypedDict, closed=True):
    errors: NotRequired["aws_sdk_glue.types.partition_errors.PartitionErrors"]
    """<p>The errors encountered when trying to delete the requested partitions.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchDeletePartitionResponse) -> dict:
    out: dict = {}
    if "errors" in value:
        import aws_sdk_glue.types.partition_errors

        out["Errors"] = aws_sdk_glue.types.partition_errors.serialize_aws_json_1_1(
            value["errors"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchDeletePartitionResponse:
    out: BatchDeletePartitionResponse = {}  # type: ignore[typeddict-item]
    if "Errors" in data:
        import aws_sdk_glue.types.partition_errors

        out["errors"] = aws_sdk_glue.types.partition_errors.deserialize_aws_json_1_1(
            data["Errors"]
        )
    return out
