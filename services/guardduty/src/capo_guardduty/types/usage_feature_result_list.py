"""Generated from Smithy shape ``com.amazonaws.guardduty#UsageFeatureResultList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.usage_feature_result

UsageFeatureResultList: TypeAlias = list[
    "capo_guardduty.types.usage_feature_result.UsageFeatureResult"
]


# --- restJson1 ser/de ---
def serialize_json(value: UsageFeatureResultList) -> list:
    import capo_guardduty.types.usage_feature_result

    out: list = []
    for item in value:
        out.append(capo_guardduty.types.usage_feature_result.serialize_json(item))
    return out


def deserialize_json(data: list) -> UsageFeatureResultList:
    import capo_guardduty.types.usage_feature_result

    out: UsageFeatureResultList = []
    for item in data:
        out.append(capo_guardduty.types.usage_feature_result.deserialize_json(item))
    return out
