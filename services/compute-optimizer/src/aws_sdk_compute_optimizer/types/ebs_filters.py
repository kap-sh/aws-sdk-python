"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#EBSFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.ebs_filter

EBSFilters: TypeAlias = list["aws_sdk_compute_optimizer.types.ebs_filter.EBSFilter"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EBSFilters) -> list:
    import aws_sdk_compute_optimizer.types.ebs_filter

    out: list = []
    for item in value:
        out.append(
            aws_sdk_compute_optimizer.types.ebs_filter.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> EBSFilters:
    import aws_sdk_compute_optimizer.types.ebs_filter

    out: EBSFilters = []
    for item in data:
        out.append(
            aws_sdk_compute_optimizer.types.ebs_filter.deserialize_aws_json_1_0(item)
        )
    return out
