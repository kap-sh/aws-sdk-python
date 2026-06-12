"""Generated from Smithy shape ``com.amazonaws.shield#DescribeAttackStatisticsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_shield.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_shield.types.attack_statistics_data_list
    import aws_sdk_shield.types.time_range


class DescribeAttackStatisticsResponse(TypedDict):
    time_range: "aws_sdk_shield.types.time_range.TimeRange"
    """<p>The time range of the attack.</p>"""
    data_items: (
        "aws_sdk_shield.types.attack_statistics_data_list.AttackStatisticsDataList"
    )
    """<p>The data that describes the attacks detected during the time period.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeAttackStatisticsResponse) -> dict:
    out: dict = {}
    import aws_sdk_shield.types.time_range

    out["TimeRange"] = aws_sdk_shield.types.time_range.serialize_aws_json_1_1(
        value["time_range"]
    )
    import aws_sdk_shield.types.attack_statistics_data_list

    out["DataItems"] = (
        aws_sdk_shield.types.attack_statistics_data_list.serialize_aws_json_1_1(
            value["data_items"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeAttackStatisticsResponse:
    out: DescribeAttackStatisticsResponse = {}  # type: ignore[typeddict-item]
    if "TimeRange" in data:
        import aws_sdk_shield.types.time_range

        out["time_range"] = aws_sdk_shield.types.time_range.deserialize_aws_json_1_1(
            data["TimeRange"]
        )
    else:
        raise DeserializationError(
            "DescribeAttackStatisticsResponse.time_range required"
        )
    if "DataItems" in data:
        import aws_sdk_shield.types.attack_statistics_data_list

        out["data_items"] = (
            aws_sdk_shield.types.attack_statistics_data_list.deserialize_aws_json_1_1(
                data["DataItems"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeAttackStatisticsResponse.data_items required"
        )
    return out
