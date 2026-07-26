"""Generated from Smithy shape ``com.amazonaws.configservice#FailedRemediationExceptionBatches``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_config_service.types.failed_remediation_exception_batch

FailedRemediationExceptionBatches: TypeAlias = list[
    "capo_config_service.types.failed_remediation_exception_batch.FailedRemediationExceptionBatch"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FailedRemediationExceptionBatches) -> list:
    import capo_config_service.types.failed_remediation_exception_batch

    out: list = []
    for item in value:
        out.append(
            capo_config_service.types.failed_remediation_exception_batch.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> FailedRemediationExceptionBatches:
    import capo_config_service.types.failed_remediation_exception_batch

    out: FailedRemediationExceptionBatches = []
    for item in data:
        out.append(
            capo_config_service.types.failed_remediation_exception_batch.deserialize_aws_json_1_1(
                item
            )
        )
    return out
