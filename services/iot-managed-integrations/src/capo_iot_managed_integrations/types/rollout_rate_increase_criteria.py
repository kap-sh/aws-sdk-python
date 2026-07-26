"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#RolloutRateIncreaseCriteria``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.number_of_notified_things
    import capo_iot_managed_integrations.types.number_of_succeeded_things


class RolloutRateIncreaseCriteria(TypedDict, closed=True):
    number_of_notified_things: NotRequired[
        "capo_iot_managed_integrations.types.number_of_notified_things.NumberOfNotifiedThings"
    ]
    """<p>The threshold for number of notified things that will initiate the increase in rate of rollout.</p>"""
    number_of_succeeded_things: NotRequired[
        "capo_iot_managed_integrations.types.number_of_succeeded_things.NumberOfSucceededThings"
    ]
    """<p>The threshold for number of succeeded things that will initiate the increase in rate of rollout.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RolloutRateIncreaseCriteria) -> dict:
    out: dict = {}
    if "number_of_notified_things" in value:
        out["numberOfNotifiedThings"] = value["number_of_notified_things"]
    if "number_of_succeeded_things" in value:
        out["numberOfSucceededThings"] = value["number_of_succeeded_things"]
    return out


def deserialize_json(data: dict) -> RolloutRateIncreaseCriteria:
    out: RolloutRateIncreaseCriteria = {}  # type: ignore[typeddict-item]
    if "numberOfNotifiedThings" in data:
        out["number_of_notified_things"] = data["numberOfNotifiedThings"]
    if "numberOfSucceededThings" in data:
        out["number_of_succeeded_things"] = data["numberOfSucceededThings"]
    return out
