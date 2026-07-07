"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeModelInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.model_name


class DescribeModelInput(TypedDict, closed=True):
    model_name: NotRequired["aws_sdk_sagemaker.types.model_name.ModelName"]
    """<p>The name of the model.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeModelInput) -> dict:
    out: dict = {}
    if "model_name" in value:
        out["ModelName"] = value["model_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeModelInput:
    out: DescribeModelInput = {}  # type: ignore[typeddict-item]
    if "ModelName" in data:
        out["model_name"] = data["ModelName"]
    return out
