"""Generated from Smithy shape ``com.amazonaws.frauddetector#GetEventResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_frauddetector.types.event


class GetEventResult(TypedDict, closed=True):
    event: NotRequired["capo_frauddetector.types.event.Event"]
    """<p>The details of the event.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetEventResult) -> dict:
    out: dict = {}
    if "event" in value:
        import capo_frauddetector.types.event

        out["event"] = capo_frauddetector.types.event.serialize_aws_json_1_1(
            value["event"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetEventResult:
    out: GetEventResult = {}  # type: ignore[typeddict-item]
    if "event" in data:
        import capo_frauddetector.types.event

        out["event"] = capo_frauddetector.types.event.deserialize_aws_json_1_1(
            data["event"]
        )
    return out
