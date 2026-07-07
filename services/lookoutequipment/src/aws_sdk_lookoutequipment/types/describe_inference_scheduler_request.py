"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#DescribeInferenceSchedulerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_lookoutequipment.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lookoutequipment.types.inference_scheduler_identifier


class DescribeInferenceSchedulerRequest(TypedDict, closed=True):
    inference_scheduler_name: "aws_sdk_lookoutequipment.types.inference_scheduler_identifier.InferenceSchedulerIdentifier"
    """<p>The name of the inference scheduler being described. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeInferenceSchedulerRequest) -> dict:
    out: dict = {}
    out["InferenceSchedulerName"] = value["inference_scheduler_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeInferenceSchedulerRequest:
    out: DescribeInferenceSchedulerRequest = {}  # type: ignore[typeddict-item]
    if "InferenceSchedulerName" in data:
        out["inference_scheduler_name"] = data["InferenceSchedulerName"]
    else:
        raise DeserializationError(
            "DescribeInferenceSchedulerRequest.inference_scheduler_name required"
        )
    return out
