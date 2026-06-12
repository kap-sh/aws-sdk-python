"""Generated from Smithy shape ``com.amazonaws.costexplorer#GetAnomalyMonitorsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cost_explorer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.anomaly_monitors
    import aws_sdk_cost_explorer.types.next_page_token


class GetAnomalyMonitorsResponse(TypedDict):
    anomaly_monitors: "aws_sdk_cost_explorer.types.anomaly_monitors.AnomalyMonitors"
    """<p>A list of cost anomaly monitors that includes the detailed metadata for each monitor. </p>"""
    next_page_token: NotRequired[
        "aws_sdk_cost_explorer.types.next_page_token.NextPageToken"
    ]
    """<p>The token to retrieve the next set of results. Amazon Web Services provides the token when the response from a previous call has more results than the maximum page size. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetAnomalyMonitorsResponse) -> dict:
    out: dict = {}
    import aws_sdk_cost_explorer.types.anomaly_monitors

    out["AnomalyMonitors"] = (
        aws_sdk_cost_explorer.types.anomaly_monitors.serialize_aws_json_1_1(
            value["anomaly_monitors"]
        )
    )
    if "next_page_token" in value:
        out["NextPageToken"] = value["next_page_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetAnomalyMonitorsResponse:
    out: GetAnomalyMonitorsResponse = {}  # type: ignore[typeddict-item]
    if "AnomalyMonitors" in data:
        import aws_sdk_cost_explorer.types.anomaly_monitors

        out["anomaly_monitors"] = (
            aws_sdk_cost_explorer.types.anomaly_monitors.deserialize_aws_json_1_1(
                data["AnomalyMonitors"]
            )
        )
    else:
        raise DeserializationError(
            "GetAnomalyMonitorsResponse.anomaly_monitors required"
        )
    if "NextPageToken" in data:
        out["next_page_token"] = data["NextPageToken"]
    return out
