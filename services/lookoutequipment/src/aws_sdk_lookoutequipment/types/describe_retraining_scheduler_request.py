"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#DescribeRetrainingSchedulerRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_lookoutequipment.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lookoutequipment.types.model_name


class DescribeRetrainingSchedulerRequest(TypedDict):
    model_name: "aws_sdk_lookoutequipment.types.model_name.ModelName"
    """<p>The name of the model that the retraining scheduler is attached to. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeRetrainingSchedulerRequest) -> dict:
    out: dict = {}
    out["ModelName"] = value["model_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeRetrainingSchedulerRequest:
    out: DescribeRetrainingSchedulerRequest = {}  # type: ignore[typeddict-item]
    if "ModelName" in data:
        out["model_name"] = data["ModelName"]
    else:
        raise DeserializationError(
            "DescribeRetrainingSchedulerRequest.model_name required"
        )
    return out
