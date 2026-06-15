"""Generated from Smithy shape ``com.amazonaws.guardduty#GetCoverageStatisticsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.coverage_filter_criteria
    import aws_sdk_guardduty.types.coverage_statistics_type_list
    import aws_sdk_guardduty.types.detector_id


class GetCoverageStatisticsRequest(TypedDict):
    detector_id: "aws_sdk_guardduty.types.detector_id.DetectorId"
    r"""<p>The unique ID of the GuardDuty detector.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href=\"https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html\">ListDetectors</a> API.</p>"""
    filter_criteria: NotRequired[
        "aws_sdk_guardduty.types.coverage_filter_criteria.CoverageFilterCriteria"
    ]
    """<p>Represents the criteria used to filter the coverage statistics.</p>"""
    statistics_type: NotRequired[
        "aws_sdk_guardduty.types.coverage_statistics_type_list.CoverageStatisticsTypeList"
    ]
    """<p>Represents the statistics type used to aggregate the coverage details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCoverageStatisticsRequest) -> dict:
    out: dict = {}
    if "filter_criteria" in value:
        import aws_sdk_guardduty.types.coverage_filter_criteria

        out["filterCriteria"] = (
            aws_sdk_guardduty.types.coverage_filter_criteria.serialize_json(
                value["filter_criteria"]
            )
        )
    if "statistics_type" in value:
        import aws_sdk_guardduty.types.coverage_statistics_type_list

        out["statisticsType"] = (
            aws_sdk_guardduty.types.coverage_statistics_type_list.serialize_json(
                value["statistics_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetCoverageStatisticsRequest:
    out: GetCoverageStatisticsRequest = {}  # type: ignore[typeddict-item]
    if "filterCriteria" in data:
        import aws_sdk_guardduty.types.coverage_filter_criteria

        out["filter_criteria"] = (
            aws_sdk_guardduty.types.coverage_filter_criteria.deserialize_json(
                data["filterCriteria"]
            )
        )
    if "statisticsType" in data:
        import aws_sdk_guardduty.types.coverage_statistics_type_list

        out["statistics_type"] = (
            aws_sdk_guardduty.types.coverage_statistics_type_list.deserialize_json(
                data["statisticsType"]
            )
        )
    return out
