"""Generated from Smithy shape ``com.amazonaws.clouddirectory#BatchWriteRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_clouddirectory.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.arn
    import aws_sdk_clouddirectory.types.batch_write_operation_list


class BatchWriteRequest(TypedDict, closed=True):
    directory_arn: "aws_sdk_clouddirectory.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) that is associated with the <a>Directory</a>. For more information, see <a>arns</a>.</p>"""
    operations: "aws_sdk_clouddirectory.types.batch_write_operation_list.BatchWriteOperationList"
    """<p>A list of operations that are part of the batch.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchWriteRequest) -> dict:
    out: dict = {}
    import aws_sdk_clouddirectory.types.batch_write_operation_list

    out["Operations"] = (
        aws_sdk_clouddirectory.types.batch_write_operation_list.serialize_json(
            value["operations"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchWriteRequest:
    out: BatchWriteRequest = {}  # type: ignore[typeddict-item]
    if "Operations" in data:
        import aws_sdk_clouddirectory.types.batch_write_operation_list

        out["operations"] = (
            aws_sdk_clouddirectory.types.batch_write_operation_list.deserialize_json(
                data["Operations"]
            )
        )
    else:
        raise DeserializationError("BatchWriteRequest.operations required")
    return out
