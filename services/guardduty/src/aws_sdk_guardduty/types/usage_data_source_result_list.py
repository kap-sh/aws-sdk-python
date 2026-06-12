"""Generated from Smithy shape ``com.amazonaws.guardduty#UsageDataSourceResultList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.usage_data_source_result

UsageDataSourceResultList: TypeAlias = list[
    "aws_sdk_guardduty.types.usage_data_source_result.UsageDataSourceResult"
]


# --- restJson1 ser/de ---
def serialize_json(value: UsageDataSourceResultList) -> list:
    import aws_sdk_guardduty.types.usage_data_source_result

    out: list = []
    for item in value:
        out.append(
            aws_sdk_guardduty.types.usage_data_source_result.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> UsageDataSourceResultList:
    import aws_sdk_guardduty.types.usage_data_source_result

    out: UsageDataSourceResultList = []
    for item in data:
        out.append(
            aws_sdk_guardduty.types.usage_data_source_result.deserialize_json(item)
        )
    return out
