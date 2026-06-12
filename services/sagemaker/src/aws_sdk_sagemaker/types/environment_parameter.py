"""Generated from Smithy shape ``com.amazonaws.sagemaker#EnvironmentParameter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.string


class EnvironmentParameter(TypedDict):
    key: NotRequired["aws_sdk_sagemaker.types.string.String"]
    """<p>The environment key suggested by the Amazon SageMaker Inference Recommender.</p>"""
    value_type: NotRequired["aws_sdk_sagemaker.types.string.String"]
    """<p>The value type suggested by the Amazon SageMaker Inference Recommender.</p>"""
    value: NotRequired["aws_sdk_sagemaker.types.string.String"]
    """<p>The value suggested by the Amazon SageMaker Inference Recommender.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EnvironmentParameter) -> dict:
    out: dict = {}
    if "key" in value:
        out["Key"] = value["key"]
    if "value_type" in value:
        out["ValueType"] = value["value_type"]
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EnvironmentParameter:
    out: EnvironmentParameter = {}  # type: ignore[typeddict-item]
    if "Key" in data:
        out["key"] = data["Key"]
    if "ValueType" in data:
        out["value_type"] = data["ValueType"]
    if "Value" in data:
        out["value"] = data["Value"]
    return out
