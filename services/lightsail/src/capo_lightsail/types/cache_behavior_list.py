"""Generated from Smithy shape ``com.amazonaws.lightsail#CacheBehaviorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lightsail.types.cache_behavior_per_path

CacheBehaviorList: TypeAlias = list[
    "capo_lightsail.types.cache_behavior_per_path.CacheBehaviorPerPath"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CacheBehaviorList) -> list:
    import capo_lightsail.types.cache_behavior_per_path

    out: list = []
    for item in value:
        out.append(
            capo_lightsail.types.cache_behavior_per_path.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> CacheBehaviorList:
    import capo_lightsail.types.cache_behavior_per_path

    out: CacheBehaviorList = []
    for item in data:
        out.append(
            capo_lightsail.types.cache_behavior_per_path.deserialize_aws_json_1_1(item)
        )
    return out
