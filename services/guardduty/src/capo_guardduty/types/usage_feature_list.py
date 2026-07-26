"""Generated from Smithy shape ``com.amazonaws.guardduty#UsageFeatureList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.usage_feature

UsageFeatureList: TypeAlias = list["capo_guardduty.types.usage_feature.UsageFeature"]


# --- restJson1 ser/de ---
def serialize_json(value: UsageFeatureList) -> list:
    import capo_guardduty.types.usage_feature

    out: list = []
    for item in value:
        out.append(capo_guardduty.types.usage_feature.serialize_json(item))
    return out


def deserialize_json(data: list) -> UsageFeatureList:
    import capo_guardduty.types.usage_feature

    out: UsageFeatureList = []
    for item in data:
        out.append(capo_guardduty.types.usage_feature.deserialize_json(item))
    return out
