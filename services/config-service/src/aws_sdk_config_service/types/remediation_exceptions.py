"""Generated from Smithy shape ``com.amazonaws.configservice#RemediationExceptions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_config_service.types.remediation_exception

RemediationExceptions: TypeAlias = list[
    "aws_sdk_config_service.types.remediation_exception.RemediationException"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RemediationExceptions) -> list:
    import aws_sdk_config_service.types.remediation_exception

    out: list = []
    for item in value:
        out.append(
            aws_sdk_config_service.types.remediation_exception.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> RemediationExceptions:
    import aws_sdk_config_service.types.remediation_exception

    out: RemediationExceptions = []
    for item in data:
        out.append(
            aws_sdk_config_service.types.remediation_exception.deserialize_aws_json_1_1(
                item
            )
        )
    return out
