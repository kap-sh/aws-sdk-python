"""Generated from Smithy shape ``com.amazonaws.freetier#FreeTierUsages``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_freetier.types.free_tier_usage

FreeTierUsages: TypeAlias = list["aws_sdk_freetier.types.free_tier_usage.FreeTierUsage"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: FreeTierUsages) -> list:
    import aws_sdk_freetier.types.free_tier_usage
    out: list = []
    for item in value:
        out.append(aws_sdk_freetier.types.free_tier_usage.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> FreeTierUsages:
    import aws_sdk_freetier.types.free_tier_usage
    out: FreeTierUsages = []
    for item in data:
        out.append(aws_sdk_freetier.types.free_tier_usage.deserialize_aws_json_1_0(item))
    return out