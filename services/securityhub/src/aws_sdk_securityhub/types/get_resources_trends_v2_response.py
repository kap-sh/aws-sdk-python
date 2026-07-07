"""Generated from Smithy shape ``com.amazonaws.securityhub#GetResourcesTrendsV2Response``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.granularity_field
    import aws_sdk_securityhub.types.next_token
    import aws_sdk_securityhub.types.resources_trends_metrics


class GetResourcesTrendsV2Response(TypedDict, closed=True):
    granularity: NotRequired[
        "aws_sdk_securityhub.types.granularity_field.GranularityField"
    ]
    """<p>The time interval granularity for the returned trend data (such as DAILY or WEEKLY).</p>"""
    trends_metrics: NotRequired[
        "aws_sdk_securityhub.types.resources_trends_metrics.ResourcesTrendsMetrics"
    ]
    """<p>The collection of time-series trend metrics, including counts of resources across the specified time period.</p>"""
    next_token: NotRequired["aws_sdk_securityhub.types.next_token.NextToken"]
    """<p>The token to use for retrieving the next page of results, if more trend data is available.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetResourcesTrendsV2Response) -> dict:
    out: dict = {}
    if "granularity" in value:
        import aws_sdk_securityhub.types.granularity_field

        out["Granularity"] = aws_sdk_securityhub.types.granularity_field.serialize_json(
            value["granularity"]
        )
    if "trends_metrics" in value:
        import aws_sdk_securityhub.types.resources_trends_metrics

        out["TrendsMetrics"] = (
            aws_sdk_securityhub.types.resources_trends_metrics.serialize_json(
                value["trends_metrics"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetResourcesTrendsV2Response:
    out: GetResourcesTrendsV2Response = {}  # type: ignore[typeddict-item]
    if "Granularity" in data:
        import aws_sdk_securityhub.types.granularity_field

        out["granularity"] = (
            aws_sdk_securityhub.types.granularity_field.deserialize_json(
                data["Granularity"]
            )
        )
    if "TrendsMetrics" in data:
        import aws_sdk_securityhub.types.resources_trends_metrics

        out["trends_metrics"] = (
            aws_sdk_securityhub.types.resources_trends_metrics.deserialize_json(
                data["TrendsMetrics"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
