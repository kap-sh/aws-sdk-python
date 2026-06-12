"""Generated from Smithy shape ``com.amazonaws.guardduty#UsageFeatureList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.usage_feature

UsageFeatureList: TypeAlias = list["aws_sdk_guardduty.types.usage_feature.UsageFeature"]


# --- restJson1 ser/de ---
def serialize_json(value: UsageFeatureList) -> list:
    import aws_sdk_guardduty.types.usage_feature

    out: list = []
    for item in value:
        out.append(aws_sdk_guardduty.types.usage_feature.serialize_json(item))
    return out


def deserialize_json(data: list) -> UsageFeatureList:
    import aws_sdk_guardduty.types.usage_feature

    out: UsageFeatureList = []
    for item in data:
        out.append(aws_sdk_guardduty.types.usage_feature.deserialize_json(item))
    return out
