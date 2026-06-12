"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#RDSInstanceFindingReasonCodes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.rds_instance_finding_reason_code

RDSInstanceFindingReasonCodes: TypeAlias = list[
    "aws_sdk_compute_optimizer.types.rds_instance_finding_reason_code.RDSInstanceFindingReasonCode"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RDSInstanceFindingReasonCodes) -> list:
    import aws_sdk_compute_optimizer.types.rds_instance_finding_reason_code

    out: list = []
    for item in value:
        out.append(
            aws_sdk_compute_optimizer.types.rds_instance_finding_reason_code.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> RDSInstanceFindingReasonCodes:
    import aws_sdk_compute_optimizer.types.rds_instance_finding_reason_code

    out: RDSInstanceFindingReasonCodes = []
    for item in data:
        out.append(
            aws_sdk_compute_optimizer.types.rds_instance_finding_reason_code.deserialize_aws_json_1_0(
                item
            )
        )
    return out
