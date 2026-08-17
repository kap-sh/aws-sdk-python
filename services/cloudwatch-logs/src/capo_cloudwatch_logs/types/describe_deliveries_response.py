"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#DescribeDeliveriesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.deliveries
    import capo_cloudwatch_logs.types.next_token


class DescribeDeliveriesResponse(TypedDict, closed=True):
    deliveries: NotRequired["capo_cloudwatch_logs.types.deliveries.Deliveries"]
    """<p>An array of structures. Each structure contains information about one delivery in the account.</p>"""
    next_token: NotRequired["capo_cloudwatch_logs.types.next_token.NextToken"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeDeliveriesResponse) -> dict:
    out: dict = {}
    if "deliveries" in value:
        import capo_cloudwatch_logs.types.deliveries

        out["deliveries"] = (
            capo_cloudwatch_logs.types.deliveries.serialize_aws_json_1_1(
                value["deliveries"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeDeliveriesResponse:
    out: DescribeDeliveriesResponse = {}  # type: ignore[typeddict-item]
    if data.get("deliveries") is not None:
        import capo_cloudwatch_logs.types.deliveries

        out["deliveries"] = (
            capo_cloudwatch_logs.types.deliveries.deserialize_aws_json_1_1(
                data["deliveries"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
