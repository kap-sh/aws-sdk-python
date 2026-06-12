"""Generated from Smithy shape ``com.amazonaws.securityhub#GetFindingStatisticsV2Response``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.group_by_results


class GetFindingStatisticsV2Response(TypedDict):
    group_by_results: NotRequired[
        "aws_sdk_securityhub.types.group_by_results.GroupByResults"
    ]
    """<p>Aggregated statistics about security findings based on specified grouping criteria.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetFindingStatisticsV2Response) -> dict:
    out: dict = {}
    if "group_by_results" in value:
        import aws_sdk_securityhub.types.group_by_results

        out["GroupByResults"] = (
            aws_sdk_securityhub.types.group_by_results.serialize_json(
                value["group_by_results"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetFindingStatisticsV2Response:
    out: GetFindingStatisticsV2Response = {}  # type: ignore[typeddict-item]
    if "GroupByResults" in data:
        import aws_sdk_securityhub.types.group_by_results

        out["group_by_results"] = (
            aws_sdk_securityhub.types.group_by_results.deserialize_json(
                data["GroupByResults"]
            )
        )
    return out
