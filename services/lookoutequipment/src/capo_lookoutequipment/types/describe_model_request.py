"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#DescribeModelRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_lookoutequipment.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lookoutequipment.types.model_name


class DescribeModelRequest(TypedDict, closed=True):
    model_name: "capo_lookoutequipment.types.model_name.ModelName"
    """<p>The name of the machine learning model to be described. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeModelRequest) -> dict:
    out: dict = {}
    out["ModelName"] = value["model_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeModelRequest:
    out: DescribeModelRequest = {}  # type: ignore[typeddict-item]
    if "ModelName" in data:
        out["model_name"] = data["ModelName"]
    else:
        raise DeserializationError("DescribeModelRequest.model_name required")
    return out
