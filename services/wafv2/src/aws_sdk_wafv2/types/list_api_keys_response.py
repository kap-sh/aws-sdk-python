"""Generated from Smithy shape ``com.amazonaws.wafv2#ListAPIKeysResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_wafv2.types.api_key_summaries
    import aws_sdk_wafv2.types.next_marker
    import aws_sdk_wafv2.types.output_url


class ListAPIKeysResponse(TypedDict):
    next_marker: NotRequired["aws_sdk_wafv2.types.next_marker.NextMarker"]
    """<p>When you request a list of objects with a <code>Limit</code> setting, if the number of objects that are still available for retrieval exceeds the limit, WAF returns a <code>NextMarker</code> value in the response. To retrieve the next batch of objects, provide the marker from the prior call in your next request.</p>"""
    api_key_summaries: NotRequired[
        "aws_sdk_wafv2.types.api_key_summaries.APIKeySummaries"
    ]
    """<p>The array of key summaries. If you specified a <code>Limit</code> in your request, this might not be the full list. </p>"""
    application_integration_url: NotRequired["aws_sdk_wafv2.types.output_url.OutputUrl"]
    """<p>The CAPTCHA application integration URL, for use in your JavaScript implementation. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListAPIKeysResponse) -> dict:
    out: dict = {}
    if "next_marker" in value:
        out["NextMarker"] = value["next_marker"]
    if "api_key_summaries" in value:
        import aws_sdk_wafv2.types.api_key_summaries

        out["APIKeySummaries"] = (
            aws_sdk_wafv2.types.api_key_summaries.serialize_aws_json_1_1(
                value["api_key_summaries"]
            )
        )
    if "application_integration_url" in value:
        out["ApplicationIntegrationURL"] = value["application_integration_url"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListAPIKeysResponse:
    out: ListAPIKeysResponse = {}  # type: ignore[typeddict-item]
    if "NextMarker" in data:
        out["next_marker"] = data["NextMarker"]
    if "APIKeySummaries" in data:
        import aws_sdk_wafv2.types.api_key_summaries

        out["api_key_summaries"] = (
            aws_sdk_wafv2.types.api_key_summaries.deserialize_aws_json_1_1(
                data["APIKeySummaries"]
            )
        )
    if "ApplicationIntegrationURL" in data:
        out["application_integration_url"] = data["ApplicationIntegrationURL"]
    return out
