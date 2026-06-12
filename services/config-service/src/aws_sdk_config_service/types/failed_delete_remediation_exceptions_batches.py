"""Generated from Smithy shape ``com.amazonaws.configservice#FailedDeleteRemediationExceptionsBatches``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_config_service.types.failed_delete_remediation_exceptions_batch

FailedDeleteRemediationExceptionsBatches: TypeAlias = list[
    "aws_sdk_config_service.types.failed_delete_remediation_exceptions_batch.FailedDeleteRemediationExceptionsBatch"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FailedDeleteRemediationExceptionsBatches) -> list:
    import aws_sdk_config_service.types.failed_delete_remediation_exceptions_batch

    out: list = []
    for item in value:
        out.append(
            aws_sdk_config_service.types.failed_delete_remediation_exceptions_batch.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> FailedDeleteRemediationExceptionsBatches:
    import aws_sdk_config_service.types.failed_delete_remediation_exceptions_batch

    out: FailedDeleteRemediationExceptionsBatches = []
    for item in data:
        out.append(
            aws_sdk_config_service.types.failed_delete_remediation_exceptions_batch.deserialize_aws_json_1_1(
                item
            )
        )
    return out
