"""Generated from Smithy shape ``com.amazonaws.freetier#FreeTierUsages``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_freetier.types.free_tier_usage

FreeTierUsages: TypeAlias = list["capo_freetier.types.free_tier_usage.FreeTierUsage"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: FreeTierUsages) -> list:
    import capo_freetier.types.free_tier_usage

    out: list = []
    for item in value:
        out.append(capo_freetier.types.free_tier_usage.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> FreeTierUsages:
    import capo_freetier.types.free_tier_usage

    out: FreeTierUsages = []
    for item in data:
        out.append(capo_freetier.types.free_tier_usage.deserialize_aws_json_1_0(item))
    return out
