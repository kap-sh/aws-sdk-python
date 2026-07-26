"""Generated from Smithy shape ``com.amazonaws.securityhub#GetResourcesStatisticsV2Response``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.group_by_results


class GetResourcesStatisticsV2Response(TypedDict, closed=True):
    group_by_results: NotRequired[
        "capo_securityhub.types.group_by_results.GroupByResults"
    ]
    """<p>The aggregated statistics about resources based on the specified grouping rule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetResourcesStatisticsV2Response) -> dict:
    out: dict = {}
    if "group_by_results" in value:
        import capo_securityhub.types.group_by_results

        out["GroupByResults"] = capo_securityhub.types.group_by_results.serialize_json(
            value["group_by_results"]
        )
    return out


def deserialize_json(data: dict) -> GetResourcesStatisticsV2Response:
    out: GetResourcesStatisticsV2Response = {}  # type: ignore[typeddict-item]
    if "GroupByResults" in data:
        import capo_securityhub.types.group_by_results

        out["group_by_results"] = (
            capo_securityhub.types.group_by_results.deserialize_json(
                data["GroupByResults"]
            )
        )
    return out
