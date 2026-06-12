"""Generated from Smithy shape ``com.amazonaws.guardduty#UsageFeatureResultList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.usage_feature_result

UsageFeatureResultList: TypeAlias = list[
    "aws_sdk_guardduty.types.usage_feature_result.UsageFeatureResult"
]


# --- restJson1 ser/de ---
def serialize_json(value: UsageFeatureResultList) -> list:
    import aws_sdk_guardduty.types.usage_feature_result

    out: list = []
    for item in value:
        out.append(aws_sdk_guardduty.types.usage_feature_result.serialize_json(item))
    return out


def deserialize_json(data: list) -> UsageFeatureResultList:
    import aws_sdk_guardduty.types.usage_feature_result

    out: UsageFeatureResultList = []
    for item in data:
        out.append(aws_sdk_guardduty.types.usage_feature_result.deserialize_json(item))
    return out
