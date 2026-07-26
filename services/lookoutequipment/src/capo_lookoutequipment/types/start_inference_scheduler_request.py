"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#StartInferenceSchedulerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_lookoutequipment.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lookoutequipment.types.inference_scheduler_identifier


class StartInferenceSchedulerRequest(TypedDict, closed=True):
    inference_scheduler_name: "capo_lookoutequipment.types.inference_scheduler_identifier.InferenceSchedulerIdentifier"
    """<p>The name of the inference scheduler to be started. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StartInferenceSchedulerRequest) -> dict:
    out: dict = {}
    out["InferenceSchedulerName"] = value["inference_scheduler_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> StartInferenceSchedulerRequest:
    out: StartInferenceSchedulerRequest = {}  # type: ignore[typeddict-item]
    if "InferenceSchedulerName" in data:
        out["inference_scheduler_name"] = data["InferenceSchedulerName"]
    else:
        raise DeserializationError(
            "StartInferenceSchedulerRequest.inference_scheduler_name required"
        )
    return out
