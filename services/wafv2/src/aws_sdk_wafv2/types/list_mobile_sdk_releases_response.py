"""Generated from Smithy shape ``com.amazonaws.wafv2#ListMobileSdkReleasesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_wafv2.types.next_marker
    import aws_sdk_wafv2.types.release_summaries


class ListMobileSdkReleasesResponse(TypedDict, closed=True):
    release_summaries: NotRequired[
        "aws_sdk_wafv2.types.release_summaries.ReleaseSummaries"
    ]
    """<p>The high level information for the available SDK releases. If you specified a <code>Limit</code> in your request, this might not be the full list. </p>"""
    next_marker: NotRequired["aws_sdk_wafv2.types.next_marker.NextMarker"]
    """<p>When you request a list of objects with a <code>Limit</code> setting, if the number of objects that are still available for retrieval exceeds the limit, WAF returns a <code>NextMarker</code> value in the response. To retrieve the next batch of objects, provide the marker from the prior call in your next request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListMobileSdkReleasesResponse) -> dict:
    out: dict = {}
    if "release_summaries" in value:
        import aws_sdk_wafv2.types.release_summaries

        out["ReleaseSummaries"] = (
            aws_sdk_wafv2.types.release_summaries.serialize_aws_json_1_1(
                value["release_summaries"]
            )
        )
    if "next_marker" in value:
        out["NextMarker"] = value["next_marker"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListMobileSdkReleasesResponse:
    out: ListMobileSdkReleasesResponse = {}  # type: ignore[typeddict-item]
    if "ReleaseSummaries" in data:
        import aws_sdk_wafv2.types.release_summaries

        out["release_summaries"] = (
            aws_sdk_wafv2.types.release_summaries.deserialize_aws_json_1_1(
                data["ReleaseSummaries"]
            )
        )
    if "NextMarker" in data:
        out["next_marker"] = data["NextMarker"]
    return out
