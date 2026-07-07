"""Generated from Smithy shape ``com.amazonaws.lightsail#GetDistributionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.resource_name
    import aws_sdk_lightsail.types.string


class GetDistributionsRequest(TypedDict, closed=True):
    distribution_name: NotRequired["aws_sdk_lightsail.types.resource_name.ResourceName"]
    """<p>The name of the distribution for which to return information.</p> <p>When omitted, the response includes all of your distributions in the Amazon Web Services Region where the request is made.</p>"""
    page_token: NotRequired["aws_sdk_lightsail.types.string.string"]
    """<p>The token to advance to the next page of results from your request.</p> <p>To get a page token, perform an initial <code>GetDistributions</code> request. If your results are paginated, the response will return a next page token that you can specify as the page token in a subsequent request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDistributionsRequest) -> dict:
    out: dict = {}
    if "distribution_name" in value:
        out["distributionName"] = value["distribution_name"]
    if "page_token" in value:
        out["pageToken"] = value["page_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDistributionsRequest:
    out: GetDistributionsRequest = {}  # type: ignore[typeddict-item]
    if "distributionName" in data:
        out["distribution_name"] = data["distributionName"]
    if "pageToken" in data:
        out["page_token"] = data["pageToken"]
    return out
