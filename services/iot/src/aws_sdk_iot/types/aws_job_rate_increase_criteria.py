"""Generated from Smithy shape ``com.amazonaws.iot#AwsJobRateIncreaseCriteria``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.aws_job_rate_increase_criteria_number_of_things


class AwsJobRateIncreaseCriteria(TypedDict, closed=True):
    number_of_notified_things: NotRequired[
        "aws_sdk_iot.types.aws_job_rate_increase_criteria_number_of_things.AwsJobRateIncreaseCriteriaNumberOfThings"
    ]
    """<p>When this number of things have been notified, it will initiate an increase in the rollout rate.</p>"""
    number_of_succeeded_things: NotRequired[
        "aws_sdk_iot.types.aws_job_rate_increase_criteria_number_of_things.AwsJobRateIncreaseCriteriaNumberOfThings"
    ]
    """<p>When this number of things have succeeded in their job execution, it will initiate an increase in the rollout rate.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsJobRateIncreaseCriteria) -> dict:
    out: dict = {}
    if "number_of_notified_things" in value:
        out["numberOfNotifiedThings"] = value["number_of_notified_things"]
    if "number_of_succeeded_things" in value:
        out["numberOfSucceededThings"] = value["number_of_succeeded_things"]
    return out


def deserialize_json(data: dict) -> AwsJobRateIncreaseCriteria:
    out: AwsJobRateIncreaseCriteria = {}  # type: ignore[typeddict-item]
    if "numberOfNotifiedThings" in data:
        out["number_of_notified_things"] = data["numberOfNotifiedThings"]
    if "numberOfSucceededThings" in data:
        out["number_of_succeeded_things"] = data["numberOfSucceededThings"]
    return out
