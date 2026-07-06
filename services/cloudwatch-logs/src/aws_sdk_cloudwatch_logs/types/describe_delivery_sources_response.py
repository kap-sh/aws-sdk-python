"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#DescribeDeliverySourcesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.delivery_sources
    import aws_sdk_cloudwatch_logs.types.next_token


class DescribeDeliverySourcesResponse(TypedDict, closed=True):
    delivery_sources: NotRequired[
        "aws_sdk_cloudwatch_logs.types.delivery_sources.DeliverySources"
    ]
    """<p>An array of structures. Each structure contains information about one delivery source in the account.</p>"""
    next_token: NotRequired["aws_sdk_cloudwatch_logs.types.next_token.NextToken"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeDeliverySourcesResponse) -> dict:
    out: dict = {}
    if "delivery_sources" in value:
        import aws_sdk_cloudwatch_logs.types.delivery_sources

        out["deliverySources"] = (
            aws_sdk_cloudwatch_logs.types.delivery_sources.serialize_aws_json_1_1(
                value["delivery_sources"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeDeliverySourcesResponse:
    out: DescribeDeliverySourcesResponse = {}  # type: ignore[typeddict-item]
    if "deliverySources" in data:
        import aws_sdk_cloudwatch_logs.types.delivery_sources

        out["delivery_sources"] = (
            aws_sdk_cloudwatch_logs.types.delivery_sources.deserialize_aws_json_1_1(
                data["deliverySources"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
