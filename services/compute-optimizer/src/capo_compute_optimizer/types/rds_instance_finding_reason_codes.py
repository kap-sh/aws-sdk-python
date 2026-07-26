"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#RDSInstanceFindingReasonCodes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_compute_optimizer.types.rds_instance_finding_reason_code

RDSInstanceFindingReasonCodes: TypeAlias = list[
    "capo_compute_optimizer.types.rds_instance_finding_reason_code.RDSInstanceFindingReasonCode"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RDSInstanceFindingReasonCodes) -> list:
    import capo_compute_optimizer.types.rds_instance_finding_reason_code

    out: list = []
    for item in value:
        out.append(
            capo_compute_optimizer.types.rds_instance_finding_reason_code.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> RDSInstanceFindingReasonCodes:
    import capo_compute_optimizer.types.rds_instance_finding_reason_code

    out: RDSInstanceFindingReasonCodes = []
    for item in data:
        out.append(
            capo_compute_optimizer.types.rds_instance_finding_reason_code.deserialize_aws_json_1_0(
                item
            )
        )
    return out
