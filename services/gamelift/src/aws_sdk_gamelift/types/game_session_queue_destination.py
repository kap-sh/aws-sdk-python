"""Generated from Smithy shape ``com.amazonaws.gamelift#GameSessionQueueDestination``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.arn_string_model


class GameSessionQueueDestination(TypedDict, closed=True):
    destination_arn: NotRequired[
        "aws_sdk_gamelift.types.arn_string_model.ArnStringModel"
    ]
    """<p>The Amazon Resource Name (ARN) that is assigned to fleet or fleet alias. ARNs, which include a fleet ID or alias ID and a Region name, provide a unique identifier across all Regions.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GameSessionQueueDestination) -> dict:
    out: dict = {}
    if "destination_arn" in value:
        out["DestinationArn"] = value["destination_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GameSessionQueueDestination:
    out: GameSessionQueueDestination = {}  # type: ignore[typeddict-item]
    if "DestinationArn" in data:
        out["destination_arn"] = data["DestinationArn"]
    return out
