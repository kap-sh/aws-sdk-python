"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#ListAnomaliesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.anomalies
    import aws_sdk_cloudwatch_logs.types.next_token


class ListAnomaliesResponse(TypedDict, closed=True):
    anomalies: NotRequired["aws_sdk_cloudwatch_logs.types.anomalies.Anomalies"]
    """<p>An array of structures, where each structure contains information about one anomaly that a log anomaly detector has found.</p>"""
    next_token: NotRequired["aws_sdk_cloudwatch_logs.types.next_token.NextToken"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListAnomaliesResponse) -> dict:
    out: dict = {}
    if "anomalies" in value:
        import aws_sdk_cloudwatch_logs.types.anomalies

        out["anomalies"] = (
            aws_sdk_cloudwatch_logs.types.anomalies.serialize_aws_json_1_1(
                value["anomalies"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListAnomaliesResponse:
    out: ListAnomaliesResponse = {}  # type: ignore[typeddict-item]
    if "anomalies" in data:
        import aws_sdk_cloudwatch_logs.types.anomalies

        out["anomalies"] = (
            aws_sdk_cloudwatch_logs.types.anomalies.deserialize_aws_json_1_1(
                data["anomalies"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
