"""Generated from Smithy shape ``com.amazonaws.configservice#RemediationExceptionResourceKeys``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_config_service.types.remediation_exception_resource_key

RemediationExceptionResourceKeys: TypeAlias = list[
    "capo_config_service.types.remediation_exception_resource_key.RemediationExceptionResourceKey"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RemediationExceptionResourceKeys) -> list:
    import capo_config_service.types.remediation_exception_resource_key

    out: list = []
    for item in value:
        out.append(
            capo_config_service.types.remediation_exception_resource_key.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> RemediationExceptionResourceKeys:
    import capo_config_service.types.remediation_exception_resource_key

    out: RemediationExceptionResourceKeys = []
    for item in data:
        out.append(
            capo_config_service.types.remediation_exception_resource_key.deserialize_aws_json_1_1(
                item
            )
        )
    return out
