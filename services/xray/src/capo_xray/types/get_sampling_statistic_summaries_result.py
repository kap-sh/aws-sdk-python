"""Generated from Smithy shape ``com.amazonaws.xray#GetSamplingStatisticSummariesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_xray.types.sampling_statistic_summary_list
    import capo_xray.types.string


class GetSamplingStatisticSummariesResult(TypedDict, closed=True):
    sampling_statistic_summaries: NotRequired[
        "capo_xray.types.sampling_statistic_summary_list.SamplingStatisticSummaryList"
    ]
    """<p>Information about the number of requests instrumented for each sampling rule.</p>"""
    next_token: NotRequired["capo_xray.types.string.String"]
    """<p>Pagination token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSamplingStatisticSummariesResult) -> dict:
    out: dict = {}
    if "sampling_statistic_summaries" in value:
        import capo_xray.types.sampling_statistic_summary_list

        out["SamplingStatisticSummaries"] = (
            capo_xray.types.sampling_statistic_summary_list.serialize_json(
                value["sampling_statistic_summaries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetSamplingStatisticSummariesResult:
    out: GetSamplingStatisticSummariesResult = {}  # type: ignore[typeddict-item]
    if "SamplingStatisticSummaries" in data:
        import capo_xray.types.sampling_statistic_summary_list

        out["sampling_statistic_summaries"] = (
            capo_xray.types.sampling_statistic_summary_list.deserialize_json(
                data["SamplingStatisticSummaries"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
