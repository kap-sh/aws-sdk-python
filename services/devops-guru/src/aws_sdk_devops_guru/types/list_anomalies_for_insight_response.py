"""Generated from Smithy shape ``com.amazonaws.devopsguru#ListAnomaliesForInsightResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_devops_guru.types.proactive_anomalies
    import aws_sdk_devops_guru.types.reactive_anomalies
    import aws_sdk_devops_guru.types.uuid_next_token


class ListAnomaliesForInsightResponse(TypedDict):
    proactive_anomalies: NotRequired[
        "aws_sdk_devops_guru.types.proactive_anomalies.ProactiveAnomalies"
    ]
    """<p> An array of <code>ProactiveAnomalySummary</code> objects that represent the requested anomalies </p>"""
    reactive_anomalies: NotRequired[
        "aws_sdk_devops_guru.types.reactive_anomalies.ReactiveAnomalies"
    ]
    """<p> An array of <code>ReactiveAnomalySummary</code> objects that represent the requested anomalies </p>"""
    next_token: NotRequired["aws_sdk_devops_guru.types.uuid_next_token.UuidNextToken"]
    """<p>The pagination token to use to retrieve the next page of results for this operation. If there are no more pages, this value is null.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAnomaliesForInsightResponse) -> dict:
    out: dict = {}
    if "proactive_anomalies" in value:
        import aws_sdk_devops_guru.types.proactive_anomalies

        out["ProactiveAnomalies"] = (
            aws_sdk_devops_guru.types.proactive_anomalies.serialize_json(
                value["proactive_anomalies"]
            )
        )
    if "reactive_anomalies" in value:
        import aws_sdk_devops_guru.types.reactive_anomalies

        out["ReactiveAnomalies"] = (
            aws_sdk_devops_guru.types.reactive_anomalies.serialize_json(
                value["reactive_anomalies"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAnomaliesForInsightResponse:
    out: ListAnomaliesForInsightResponse = {}  # type: ignore[typeddict-item]
    if "ProactiveAnomalies" in data:
        import aws_sdk_devops_guru.types.proactive_anomalies

        out["proactive_anomalies"] = (
            aws_sdk_devops_guru.types.proactive_anomalies.deserialize_json(
                data["ProactiveAnomalies"]
            )
        )
    if "ReactiveAnomalies" in data:
        import aws_sdk_devops_guru.types.reactive_anomalies

        out["reactive_anomalies"] = (
            aws_sdk_devops_guru.types.reactive_anomalies.deserialize_json(
                data["ReactiveAnomalies"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
