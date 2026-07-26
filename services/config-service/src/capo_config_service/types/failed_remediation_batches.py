"""Generated from Smithy shape ``com.amazonaws.configservice#FailedRemediationBatches``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_config_service.types.failed_remediation_batch

FailedRemediationBatches: TypeAlias = list[
    "capo_config_service.types.failed_remediation_batch.FailedRemediationBatch"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FailedRemediationBatches) -> list:
    import capo_config_service.types.failed_remediation_batch

    out: list = []
    for item in value:
        out.append(
            capo_config_service.types.failed_remediation_batch.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> FailedRemediationBatches:
    import capo_config_service.types.failed_remediation_batch

    out: FailedRemediationBatches = []
    for item in data:
        out.append(
            capo_config_service.types.failed_remediation_batch.deserialize_aws_json_1_1(
                item
            )
        )
    return out
