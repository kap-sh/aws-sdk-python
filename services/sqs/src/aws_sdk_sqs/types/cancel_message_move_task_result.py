"""Generated from Smithy shape ``com.amazonaws.sqs#CancelMessageMoveTaskResult``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_sqs.types.long


class CancelMessageMoveTaskResult(TypedDict, closed=True):
    approximate_number_of_messages_moved: "aws_sdk_sqs.types.long.Long"
    """<p>The approximate number of messages already moved to the destination queue.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CancelMessageMoveTaskResult) -> dict:
    out: dict = {}
    out["ApproximateNumberOfMessagesMoved"] = value.get(
        "approximate_number_of_messages_moved", 0
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> CancelMessageMoveTaskResult:
    out: CancelMessageMoveTaskResult = {}  # type: ignore[typeddict-item]
    if "ApproximateNumberOfMessagesMoved" in data:
        out["approximate_number_of_messages_moved"] = data[
            "ApproximateNumberOfMessagesMoved"
        ]
    else:
        out["approximate_number_of_messages_moved"] = 0
    return out
