"""Generated from Smithy shape ``com.amazonaws.guardduty#GetCoverageStatisticsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.coverage_statistics


class GetCoverageStatisticsResponse(TypedDict):
    coverage_statistics: NotRequired[
        "aws_sdk_guardduty.types.coverage_statistics.CoverageStatistics"
    ]
    """<p>Represents the count aggregated by the <code>statusCode</code> and <code>resourceType</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCoverageStatisticsResponse) -> dict:
    out: dict = {}
    if "coverage_statistics" in value:
        import aws_sdk_guardduty.types.coverage_statistics

        out["coverageStatistics"] = (
            aws_sdk_guardduty.types.coverage_statistics.serialize_json(
                value["coverage_statistics"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetCoverageStatisticsResponse:
    out: GetCoverageStatisticsResponse = {}  # type: ignore[typeddict-item]
    if "coverageStatistics" in data:
        import aws_sdk_guardduty.types.coverage_statistics

        out["coverage_statistics"] = (
            aws_sdk_guardduty.types.coverage_statistics.deserialize_json(
                data["coverageStatistics"]
            )
        )
    return out
