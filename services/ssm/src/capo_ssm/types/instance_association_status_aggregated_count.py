"""Generated from Smithy shape ``com.amazonaws.ssm#InstanceAssociationStatusAggregatedCount``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.instance_count
    import capo_ssm.types.status_name

InstanceAssociationStatusAggregatedCount: TypeAlias = dict[
    "capo_ssm.types.status_name.StatusName",
    "capo_ssm.types.instance_count.InstanceCount",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    input_to_serialize: InstanceAssociationStatusAggregatedCount,
) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> InstanceAssociationStatusAggregatedCount:
    out: InstanceAssociationStatusAggregatedCount = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out
