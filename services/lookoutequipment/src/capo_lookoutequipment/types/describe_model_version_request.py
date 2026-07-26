"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#DescribeModelVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_lookoutequipment.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lookoutequipment.types.model_name
    import capo_lookoutequipment.types.model_version


class DescribeModelVersionRequest(TypedDict, closed=True):
    model_name: "capo_lookoutequipment.types.model_name.ModelName"
    """<p>The name of the machine learning model that this version belongs to.</p>"""
    model_version: "capo_lookoutequipment.types.model_version.ModelVersion"
    """<p>The version of the machine learning model.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeModelVersionRequest) -> dict:
    out: dict = {}
    out["ModelName"] = value["model_name"]
    out["ModelVersion"] = value["model_version"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeModelVersionRequest:
    out: DescribeModelVersionRequest = {}  # type: ignore[typeddict-item]
    if "ModelName" in data:
        out["model_name"] = data["ModelName"]
    else:
        raise DeserializationError("DescribeModelVersionRequest.model_name required")
    if "ModelVersion" in data:
        out["model_version"] = data["ModelVersion"]
    else:
        raise DeserializationError("DescribeModelVersionRequest.model_version required")
    return out
