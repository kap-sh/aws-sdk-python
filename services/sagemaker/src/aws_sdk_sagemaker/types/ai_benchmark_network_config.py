"""Generated from Smithy shape ``com.amazonaws.sagemaker#AIBenchmarkNetworkConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.vpc_config


class AIBenchmarkNetworkConfig(TypedDict):
    vpc_config: NotRequired["aws_sdk_sagemaker.types.vpc_config.VpcConfig"]
    """<p>The VPC configuration, including security group IDs and subnet IDs.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AIBenchmarkNetworkConfig) -> dict:
    out: dict = {}
    if "vpc_config" in value:
        import aws_sdk_sagemaker.types.vpc_config

        out["VpcConfig"] = aws_sdk_sagemaker.types.vpc_config.serialize_aws_json_1_1(
            value["vpc_config"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AIBenchmarkNetworkConfig:
    out: AIBenchmarkNetworkConfig = {}  # type: ignore[typeddict-item]
    if "VpcConfig" in data:
        import aws_sdk_sagemaker.types.vpc_config

        out["vpc_config"] = aws_sdk_sagemaker.types.vpc_config.deserialize_aws_json_1_1(
            data["VpcConfig"]
        )
    return out
