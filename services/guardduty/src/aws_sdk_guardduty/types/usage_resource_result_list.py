"""Generated from Smithy shape ``com.amazonaws.guardduty#UsageResourceResultList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.usage_resource_result

UsageResourceResultList: TypeAlias = list[
    "aws_sdk_guardduty.types.usage_resource_result.UsageResourceResult"
]


# --- restJson1 ser/de ---
def serialize_json(value: UsageResourceResultList) -> list:
    import aws_sdk_guardduty.types.usage_resource_result

    out: list = []
    for item in value:
        out.append(aws_sdk_guardduty.types.usage_resource_result.serialize_json(item))
    return out


def deserialize_json(data: list) -> UsageResourceResultList:
    import aws_sdk_guardduty.types.usage_resource_result

    out: UsageResourceResultList = []
    for item in data:
        out.append(aws_sdk_guardduty.types.usage_resource_result.deserialize_json(item))
    return out
