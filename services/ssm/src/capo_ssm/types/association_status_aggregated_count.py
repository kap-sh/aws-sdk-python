"""Generated from Smithy shape ``com.amazonaws.ssm#AssociationStatusAggregatedCount``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.instance_count
    import capo_ssm.types.status_name

AssociationStatusAggregatedCount: TypeAlias = dict[
    "capo_ssm.types.status_name.StatusName",
    "capo_ssm.types.instance_count.InstanceCount",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    input_to_serialize: AssociationStatusAggregatedCount,
) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> AssociationStatusAggregatedCount:
    out: AssociationStatusAggregatedCount = {}
    for key, value in data.items():
        out[key] = value
    return out
