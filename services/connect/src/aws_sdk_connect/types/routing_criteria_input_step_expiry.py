"""Generated from Smithy shape ``com.amazonaws.connect#RoutingCriteriaInputStepExpiry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.duration_in_seconds


class RoutingCriteriaInputStepExpiry(TypedDict, closed=True):
    duration_in_seconds: NotRequired[
        "aws_sdk_connect.types.duration_in_seconds.DurationInSeconds"
    ]
    """<p>The number of seconds that the contact will be routed only to agents matching this routing step, if expiry was configured for this routing step.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RoutingCriteriaInputStepExpiry) -> dict:
    out: dict = {}
    if "duration_in_seconds" in value:
        out["DurationInSeconds"] = value["duration_in_seconds"]
    return out


def deserialize_json(data: dict) -> RoutingCriteriaInputStepExpiry:
    out: RoutingCriteriaInputStepExpiry = {}  # type: ignore[typeddict-item]
    if "DurationInSeconds" in data:
        out["duration_in_seconds"] = data["DurationInSeconds"]
    return out
