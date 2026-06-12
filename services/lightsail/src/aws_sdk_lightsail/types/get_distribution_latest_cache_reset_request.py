"""Generated from Smithy shape ``com.amazonaws.lightsail#GetDistributionLatestCacheResetRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.resource_name


class GetDistributionLatestCacheResetRequest(TypedDict):
    distribution_name: NotRequired["aws_sdk_lightsail.types.resource_name.ResourceName"]
    """<p>The name of the distribution for which to return the timestamp of the last cache reset.</p> <p>Use the <code>GetDistributions</code> action to get a list of distribution names that you can specify.</p> <p>When omitted, the response includes the latest cache reset timestamp of all your distributions.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDistributionLatestCacheResetRequest) -> dict:
    out: dict = {}
    if "distribution_name" in value:
        out["distributionName"] = value["distribution_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDistributionLatestCacheResetRequest:
    out: GetDistributionLatestCacheResetRequest = {}  # type: ignore[typeddict-item]
    if "distributionName" in data:
        out["distribution_name"] = data["distributionName"]
    return out
