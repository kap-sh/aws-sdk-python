"""Generated from Smithy shape ``com.amazonaws.iot#RateIncreaseCriteria``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.number_of_things


class RateIncreaseCriteria(TypedDict):
    number_of_notified_things: NotRequired[
        "aws_sdk_iot.types.number_of_things.NumberOfThings"
    ]
    """<p>The threshold for number of notified things that will initiate the increase in rate of rollout.</p>"""
    number_of_succeeded_things: NotRequired[
        "aws_sdk_iot.types.number_of_things.NumberOfThings"
    ]
    """<p>The threshold for number of succeeded things that will initiate the increase in rate of rollout.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RateIncreaseCriteria) -> dict:
    out: dict = {}
    if "number_of_notified_things" in value:
        out["numberOfNotifiedThings"] = value["number_of_notified_things"]
    if "number_of_succeeded_things" in value:
        out["numberOfSucceededThings"] = value["number_of_succeeded_things"]
    return out


def deserialize_json(data: dict) -> RateIncreaseCriteria:
    out: RateIncreaseCriteria = {}  # type: ignore[typeddict-item]
    if "numberOfNotifiedThings" in data:
        out["number_of_notified_things"] = data["numberOfNotifiedThings"]
    if "numberOfSucceededThings" in data:
        out["number_of_succeeded_things"] = data["numberOfSucceededThings"]
    return out
