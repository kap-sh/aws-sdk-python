"""Generated from Smithy shape ``com.amazonaws.sagemaker#OnStartDeepHealthChecks``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.deep_health_check_type

OnStartDeepHealthChecks: TypeAlias = list[
    "aws_sdk_sagemaker.types.deep_health_check_type.DeepHealthCheckType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OnStartDeepHealthChecks) -> list:
    import aws_sdk_sagemaker.types.deep_health_check_type

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sagemaker.types.deep_health_check_type.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> OnStartDeepHealthChecks:
    import aws_sdk_sagemaker.types.deep_health_check_type

    out: OnStartDeepHealthChecks = []
    for item in data:
        out.append(
            aws_sdk_sagemaker.types.deep_health_check_type.deserialize_aws_json_1_1(
                item
            )
        )
    return out
