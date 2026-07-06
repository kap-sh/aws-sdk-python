"""Generated from Smithy shape ``com.amazonaws.gamelift#DeleteGameSessionQueueInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.game_session_queue_name_or_arn


class DeleteGameSessionQueueInput(TypedDict, closed=True):
    name: NotRequired[
        "aws_sdk_gamelift.types.game_session_queue_name_or_arn.GameSessionQueueNameOrArn"
    ]
    """<p>A descriptive label that is associated with game session queue. Queue names must be unique within each Region. You can use either the queue ID or ARN value. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteGameSessionQueueInput) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteGameSessionQueueInput:
    out: DeleteGameSessionQueueInput = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    return out
