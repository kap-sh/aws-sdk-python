"""Generated from Smithy shape ``com.amazonaws.appstream#DescribeAppLicenseUsageRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_appstream.types.integer
    import aws_sdk_appstream.types.string


class DescribeAppLicenseUsageRequest(TypedDict, closed=True):
    billing_period: NotRequired["aws_sdk_appstream.types.string.String"]
    """<p>Billing period for the usage record.</p> <p>Specify the value in <i>yyyy-mm</i> format. For example, for August 2025, use <i>2025-08</i>.</p>"""
    max_results: NotRequired["aws_sdk_appstream.types.integer.Integer"]
    """<p>The maximum number of results to return.</p>"""
    next_token: NotRequired["aws_sdk_appstream.types.string.String"]
    """<p>Token for pagination of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeAppLicenseUsageRequest) -> dict:
    out: dict = {}
    if "billing_period" in value:
        out["BillingPeriod"] = value["billing_period"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeAppLicenseUsageRequest:
    out: DescribeAppLicenseUsageRequest = {}  # type: ignore[typeddict-item]
    if "BillingPeriod" in data:
        out["billing_period"] = data["BillingPeriod"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
