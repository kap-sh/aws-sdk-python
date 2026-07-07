"""Generated from Smithy shape ``com.amazonaws.health#EventDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_health.types.event_description2


class EventDescription(TypedDict, closed=True):
    latest_description: NotRequired[
        "aws_sdk_health.types.event_description2.EventDescription2"
    ]
    """<p>The most recent description of the event.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EventDescription) -> dict:
    out: dict = {}
    if "latest_description" in value:
        out["latestDescription"] = value["latest_description"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EventDescription:
    out: EventDescription = {}  # type: ignore[typeddict-item]
    if "latestDescription" in data:
        out["latest_description"] = data["latestDescription"]
    return out
