"""Generated from Smithy shape ``com.amazonaws.batch#ServiceJobPreemptionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_batch.types.integer


class ServiceJobPreemptionConfiguration(TypedDict, closed=True):
    preemption_retries_before_termination: NotRequired[
        "aws_sdk_batch.types.integer.Integer"
    ]
    """<p>The number of times a service job can be retried after it is preempted. A job will be terminated when preemption retries have been exhausted. If this field is unset, preempted jobs will be requeued an unlimited number of times. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceJobPreemptionConfiguration) -> dict:
    out: dict = {}
    if "preemption_retries_before_termination" in value:
        out["preemptionRetriesBeforeTermination"] = value[
            "preemption_retries_before_termination"
        ]
    return out


def deserialize_json(data: dict) -> ServiceJobPreemptionConfiguration:
    out: ServiceJobPreemptionConfiguration = {}  # type: ignore[typeddict-item]
    if "preemptionRetriesBeforeTermination" in data:
        out["preemption_retries_before_termination"] = data[
            "preemptionRetriesBeforeTermination"
        ]
    return out
