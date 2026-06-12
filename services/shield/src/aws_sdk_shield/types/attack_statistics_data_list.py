"""Generated from Smithy shape ``com.amazonaws.shield#AttackStatisticsDataList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_shield.types.attack_statistics_data_item

AttackStatisticsDataList: TypeAlias = list[
    "aws_sdk_shield.types.attack_statistics_data_item.AttackStatisticsDataItem"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AttackStatisticsDataList) -> list:
    import aws_sdk_shield.types.attack_statistics_data_item

    out: list = []
    for item in value:
        out.append(
            aws_sdk_shield.types.attack_statistics_data_item.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AttackStatisticsDataList:
    import aws_sdk_shield.types.attack_statistics_data_item

    out: AttackStatisticsDataList = []
    for item in data:
        out.append(
            aws_sdk_shield.types.attack_statistics_data_item.deserialize_aws_json_1_1(
                item
            )
        )
    return out
