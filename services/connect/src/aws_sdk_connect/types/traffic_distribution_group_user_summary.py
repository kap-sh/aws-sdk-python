"""Generated from Smithy shape ``com.amazonaws.connect#TrafficDistributionGroupUserSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.user_id


class TrafficDistributionGroupUserSummary(TypedDict, closed=True):
    user_id: NotRequired["aws_sdk_connect.types.user_id.UserId"]
    """<p>The identifier for the user. This can be the ID or the ARN of the user.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TrafficDistributionGroupUserSummary) -> dict:
    out: dict = {}
    if "user_id" in value:
        out["UserId"] = value["user_id"]
    return out


def deserialize_json(data: dict) -> TrafficDistributionGroupUserSummary:
    out: TrafficDistributionGroupUserSummary = {}  # type: ignore[typeddict-item]
    if "UserId" in data:
        out["user_id"] = data["UserId"]
    return out
