"""Generated from Smithy shape ``com.amazonaws.pricing#DescribeServicesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pricing.types.describe_services_max_results
    import capo_pricing.types.format_version
    import capo_pricing.types.string


class DescribeServicesRequest(TypedDict, closed=True):
    service_code: NotRequired["capo_pricing.types.string.String"]
    """<p>The code for the service whose information you want to retrieve, such as <code>AmazonEC2</code>. You can use the <code>ServiceCode</code> to filter the results in a <code>GetProducts</code> call. To retrieve a list of all services, leave this blank.</p>"""
    format_version: NotRequired["capo_pricing.types.format_version.FormatVersion"]
    """<p>The format version that you want the response to be in.</p> <p>Valid values are: <code>aws_v1</code> </p>"""
    next_token: NotRequired["capo_pricing.types.string.String"]
    """<p>The pagination token that indicates the next set of results that you want to retrieve.</p>"""
    max_results: NotRequired[
        "capo_pricing.types.describe_services_max_results.DescribeServicesMaxResults"
    ]
    """<p>The maximum number of results that you want returned in the response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeServicesRequest) -> dict:
    out: dict = {}
    if "service_code" in value:
        out["ServiceCode"] = value["service_code"]
    if "format_version" in value:
        out["FormatVersion"] = value["format_version"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeServicesRequest:
    out: DescribeServicesRequest = {}  # type: ignore[typeddict-item]
    if "ServiceCode" in data:
        out["service_code"] = data["ServiceCode"]
    if "FormatVersion" in data:
        out["format_version"] = data["FormatVersion"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
