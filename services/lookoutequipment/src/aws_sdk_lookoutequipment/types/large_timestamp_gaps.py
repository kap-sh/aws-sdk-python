"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#LargeTimestampGaps``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_lookoutequipment.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lookoutequipment.types.integer
    import aws_sdk_lookoutequipment.types.statistical_issue_status


class LargeTimestampGaps(TypedDict, closed=True):
    status: (
        "aws_sdk_lookoutequipment.types.statistical_issue_status.StatisticalIssueStatus"
    )
    """<p> Indicates whether there is a potential data issue related to large gaps in timestamps. </p>"""
    number_of_large_timestamp_gaps: NotRequired[
        "aws_sdk_lookoutequipment.types.integer.Integer"
    ]
    """<p> Indicates the number of large timestamp gaps, if there are any. </p>"""
    max_timestamp_gap_in_days: NotRequired[
        "aws_sdk_lookoutequipment.types.integer.Integer"
    ]
    """<p> Indicates the size of the largest timestamp gap, in days. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LargeTimestampGaps) -> dict:
    out: dict = {}
    import aws_sdk_lookoutequipment.types.statistical_issue_status

    out["Status"] = (
        aws_sdk_lookoutequipment.types.statistical_issue_status.serialize_aws_json_1_0(
            value["status"]
        )
    )
    if "number_of_large_timestamp_gaps" in value:
        out["NumberOfLargeTimestampGaps"] = value["number_of_large_timestamp_gaps"]
    if "max_timestamp_gap_in_days" in value:
        out["MaxTimestampGapInDays"] = value["max_timestamp_gap_in_days"]
    return out


def deserialize_aws_json_1_0(data: dict) -> LargeTimestampGaps:
    out: LargeTimestampGaps = {}  # type: ignore[typeddict-item]
    if "Status" in data:
        import aws_sdk_lookoutequipment.types.statistical_issue_status

        out["status"] = (
            aws_sdk_lookoutequipment.types.statistical_issue_status.deserialize_aws_json_1_0(
                data["Status"]
            )
        )
    else:
        raise DeserializationError("LargeTimestampGaps.status required")
    if "NumberOfLargeTimestampGaps" in data:
        out["number_of_large_timestamp_gaps"] = data["NumberOfLargeTimestampGaps"]
    if "MaxTimestampGapInDays" in data:
        out["max_timestamp_gap_in_days"] = data["MaxTimestampGapInDays"]
    return out
