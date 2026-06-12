"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#DeleteInferenceSchedulerRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_lookoutequipment.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lookoutequipment.types.inference_scheduler_identifier


class DeleteInferenceSchedulerRequest(TypedDict):
    inference_scheduler_name: "aws_sdk_lookoutequipment.types.inference_scheduler_identifier.InferenceSchedulerIdentifier"
    """<p>The name of the inference scheduler to be deleted. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteInferenceSchedulerRequest) -> dict:
    out: dict = {}
    out["InferenceSchedulerName"] = value["inference_scheduler_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteInferenceSchedulerRequest:
    out: DeleteInferenceSchedulerRequest = {}  # type: ignore[typeddict-item]
    if "InferenceSchedulerName" in data:
        out["inference_scheduler_name"] = data["InferenceSchedulerName"]
    else:
        raise DeserializationError(
            "DeleteInferenceSchedulerRequest.inference_scheduler_name required"
        )
    return out
