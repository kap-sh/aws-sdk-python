"""Generated from Smithy shape ``com.amazonaws.rum#ListRumMetricsDestinationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rum.types.metric_destination_summary_list


class ListRumMetricsDestinationsResponse(TypedDict, closed=True):
    destinations: NotRequired[
        "capo_rum.types.metric_destination_summary_list.MetricDestinationSummaryList"
    ]
    """<p>The list of CloudWatch RUM extended metrics destinations associated with the app monitor that you specified.</p>"""
    next_token: NotRequired["str"]
    """<p>A token that you can use in a subsequent operation to retrieve the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRumMetricsDestinationsResponse) -> dict:
    out: dict = {}
    if "destinations" in value:
        import capo_rum.types.metric_destination_summary_list

        out["Destinations"] = (
            capo_rum.types.metric_destination_summary_list.serialize_json(
                value["destinations"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListRumMetricsDestinationsResponse:
    out: ListRumMetricsDestinationsResponse = {}  # type: ignore[typeddict-item]
    if "Destinations" in data:
        import capo_rum.types.metric_destination_summary_list

        out["destinations"] = (
            capo_rum.types.metric_destination_summary_list.deserialize_json(
                data["Destinations"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
