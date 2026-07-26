"""Generated from Smithy shape ``com.amazonaws.greengrassv2#IoTJobRateIncreaseCriteria``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_greengrassv2.types.io_t_job_number_of_things


class IoTJobRateIncreaseCriteria(TypedDict, closed=True):
    number_of_notified_things: NotRequired[
        "capo_greengrassv2.types.io_t_job_number_of_things.IoTJobNumberOfThings"
    ]
    """<p>The number of devices to receive the job notification before the rollout rate increases.</p>"""
    number_of_succeeded_things: NotRequired[
        "capo_greengrassv2.types.io_t_job_number_of_things.IoTJobNumberOfThings"
    ]
    """<p>The number of devices to successfully run the configuration job before the rollout rate increases.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IoTJobRateIncreaseCriteria) -> dict:
    out: dict = {}
    if "number_of_notified_things" in value:
        out["numberOfNotifiedThings"] = value["number_of_notified_things"]
    if "number_of_succeeded_things" in value:
        out["numberOfSucceededThings"] = value["number_of_succeeded_things"]
    return out


def deserialize_json(data: dict) -> IoTJobRateIncreaseCriteria:
    out: IoTJobRateIncreaseCriteria = {}  # type: ignore[typeddict-item]
    if "numberOfNotifiedThings" in data:
        out["number_of_notified_things"] = data["numberOfNotifiedThings"]
    if "numberOfSucceededThings" in data:
        out["number_of_succeeded_things"] = data["numberOfSucceededThings"]
    return out
