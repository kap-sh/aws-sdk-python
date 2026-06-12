"""Generated from Smithy shape ``com.amazonaws.configservice#EvaluationModes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_config_service.types.evaluation_mode_configuration

EvaluationModes: TypeAlias = list[
    "aws_sdk_config_service.types.evaluation_mode_configuration.EvaluationModeConfiguration"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EvaluationModes) -> list:
    import aws_sdk_config_service.types.evaluation_mode_configuration

    out: list = []
    for item in value:
        out.append(
            aws_sdk_config_service.types.evaluation_mode_configuration.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> EvaluationModes:
    import aws_sdk_config_service.types.evaluation_mode_configuration

    out: EvaluationModes = []
    for item in data:
        out.append(
            aws_sdk_config_service.types.evaluation_mode_configuration.deserialize_aws_json_1_1(
                item
            )
        )
    return out
