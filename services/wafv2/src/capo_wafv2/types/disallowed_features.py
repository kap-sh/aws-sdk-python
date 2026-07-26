"""Generated from Smithy shape ``com.amazonaws.wafv2#DisallowedFeatures``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wafv2.types.disallowed_feature

DisallowedFeatures: TypeAlias = list[
    "capo_wafv2.types.disallowed_feature.DisallowedFeature"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DisallowedFeatures) -> list:
    import capo_wafv2.types.disallowed_feature

    out: list = []
    for item in value:
        out.append(capo_wafv2.types.disallowed_feature.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> DisallowedFeatures:
    import capo_wafv2.types.disallowed_feature

    out: DisallowedFeatures = []
    for item in data:
        out.append(capo_wafv2.types.disallowed_feature.deserialize_aws_json_1_1(item))
    return out
