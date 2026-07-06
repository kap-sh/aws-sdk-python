"""Generated from Smithy shape ``com.amazonaws.gamelift#StopGameSessionPlacementInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.id_string_model


class StopGameSessionPlacementInput(TypedDict, closed=True):
    placement_id: NotRequired["aws_sdk_gamelift.types.id_string_model.IdStringModel"]
    """<p>A unique identifier for a game session placement to stop.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopGameSessionPlacementInput) -> dict:
    out: dict = {}
    if "placement_id" in value:
        out["PlacementId"] = value["placement_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StopGameSessionPlacementInput:
    out: StopGameSessionPlacementInput = {}  # type: ignore[typeddict-item]
    if "PlacementId" in data:
        out["placement_id"] = data["PlacementId"]
    return out
