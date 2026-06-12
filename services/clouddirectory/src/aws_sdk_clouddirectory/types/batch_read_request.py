"""Generated from Smithy shape ``com.amazonaws.clouddirectory#BatchReadRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_clouddirectory.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.arn
    import aws_sdk_clouddirectory.types.batch_read_operation_list
    import aws_sdk_clouddirectory.types.consistency_level


class BatchReadRequest(TypedDict):
    directory_arn: "aws_sdk_clouddirectory.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) that is associated with the <a>Directory</a>. For more information, see <a>arns</a>.</p>"""
    operations: (
        "aws_sdk_clouddirectory.types.batch_read_operation_list.BatchReadOperationList"
    )
    """<p>A list of operations that are part of the batch.</p>"""
    consistency_level: NotRequired[
        "aws_sdk_clouddirectory.types.consistency_level.ConsistencyLevel"
    ]
    """<p>Represents the manner and timing in which the successful write or update of an object is reflected in a subsequent read operation of that same object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchReadRequest) -> dict:
    out: dict = {}
    import aws_sdk_clouddirectory.types.batch_read_operation_list

    out["Operations"] = (
        aws_sdk_clouddirectory.types.batch_read_operation_list.serialize_json(
            value["operations"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchReadRequest:
    out: BatchReadRequest = {}  # type: ignore[typeddict-item]
    if "Operations" in data:
        import aws_sdk_clouddirectory.types.batch_read_operation_list

        out["operations"] = (
            aws_sdk_clouddirectory.types.batch_read_operation_list.deserialize_json(
                data["Operations"]
            )
        )
    else:
        raise DeserializationError("BatchReadRequest.operations required")
    return out
