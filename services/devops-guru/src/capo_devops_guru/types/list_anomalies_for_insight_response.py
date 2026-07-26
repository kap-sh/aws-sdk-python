"""Generated from Smithy shape ``com.amazonaws.devopsguru#ListAnomaliesForInsightResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_devops_guru.types.proactive_anomalies
    import capo_devops_guru.types.reactive_anomalies
    import capo_devops_guru.types.uuid_next_token


class ListAnomaliesForInsightResponse(TypedDict, closed=True):
    proactive_anomalies: NotRequired[
        "capo_devops_guru.types.proactive_anomalies.ProactiveAnomalies"
    ]
    """<p> An array of <code>ProactiveAnomalySummary</code> objects that represent the requested anomalies </p>"""
    reactive_anomalies: NotRequired[
        "capo_devops_guru.types.reactive_anomalies.ReactiveAnomalies"
    ]
    """<p> An array of <code>ReactiveAnomalySummary</code> objects that represent the requested anomalies </p>"""
    next_token: NotRequired["capo_devops_guru.types.uuid_next_token.UuidNextToken"]
    """<p>The pagination token to use to retrieve the next page of results for this operation. If there are no more pages, this value is null.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAnomaliesForInsightResponse) -> dict:
    out: dict = {}
    if "proactive_anomalies" in value:
        import capo_devops_guru.types.proactive_anomalies

        out["ProactiveAnomalies"] = (
            capo_devops_guru.types.proactive_anomalies.serialize_json(
                value["proactive_anomalies"]
            )
        )
    if "reactive_anomalies" in value:
        import capo_devops_guru.types.reactive_anomalies

        out["ReactiveAnomalies"] = (
            capo_devops_guru.types.reactive_anomalies.serialize_json(
                value["reactive_anomalies"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAnomaliesForInsightResponse:
    out: ListAnomaliesForInsightResponse = {}  # type: ignore[typeddict-item]
    if "ProactiveAnomalies" in data:
        import capo_devops_guru.types.proactive_anomalies

        out["proactive_anomalies"] = (
            capo_devops_guru.types.proactive_anomalies.deserialize_json(
                data["ProactiveAnomalies"]
            )
        )
    if "ReactiveAnomalies" in data:
        import capo_devops_guru.types.reactive_anomalies

        out["reactive_anomalies"] = (
            capo_devops_guru.types.reactive_anomalies.deserialize_json(
                data["ReactiveAnomalies"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
