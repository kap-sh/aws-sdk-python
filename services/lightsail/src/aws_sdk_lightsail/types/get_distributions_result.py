"""Generated from Smithy shape ``com.amazonaws.lightsail#GetDistributionsResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.distribution_list
    import aws_sdk_lightsail.types.string


class GetDistributionsResult(TypedDict):
    distributions: NotRequired[
        "aws_sdk_lightsail.types.distribution_list.DistributionList"
    ]
    """<p>An array of objects that describe your distributions.</p>"""
    next_page_token: NotRequired["aws_sdk_lightsail.types.string.string"]
    """<p>The token to advance to the next page of results from your request.</p> <p>A next page token is not returned if there are no more results to display.</p> <p>To get the next page of results, perform another <code>GetDistributions</code> request and specify the next page token using the <code>pageToken</code> parameter.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDistributionsResult) -> dict:
    out: dict = {}
    if "distributions" in value:
        import aws_sdk_lightsail.types.distribution_list

        out["distributions"] = (
            aws_sdk_lightsail.types.distribution_list.serialize_aws_json_1_1(
                value["distributions"]
            )
        )
    if "next_page_token" in value:
        out["nextPageToken"] = value["next_page_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDistributionsResult:
    out: GetDistributionsResult = {}  # type: ignore[typeddict-item]
    if "distributions" in data:
        import aws_sdk_lightsail.types.distribution_list

        out["distributions"] = (
            aws_sdk_lightsail.types.distribution_list.deserialize_aws_json_1_1(
                data["distributions"]
            )
        )
    if "nextPageToken" in data:
        out["next_page_token"] = data["nextPageToken"]
    return out
