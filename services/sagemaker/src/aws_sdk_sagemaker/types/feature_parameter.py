"""Generated from Smithy shape ``com.amazonaws.sagemaker#FeatureParameter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.feature_parameter_key
    import aws_sdk_sagemaker.types.feature_parameter_value


class FeatureParameter(TypedDict):
    key: NotRequired[
        "aws_sdk_sagemaker.types.feature_parameter_key.FeatureParameterKey"
    ]
    """<p>A key that must contain a value to describe the feature.</p>"""
    value: NotRequired[
        "aws_sdk_sagemaker.types.feature_parameter_value.FeatureParameterValue"
    ]
    """<p>The value that belongs to a key.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FeatureParameter) -> dict:
    out: dict = {}
    if "key" in value:
        out["Key"] = value["key"]
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> FeatureParameter:
    out: FeatureParameter = {}  # type: ignore[typeddict-item]
    if "Key" in data:
        out["key"] = data["Key"]
    if "Value" in data:
        out["value"] = data["Value"]
    return out
