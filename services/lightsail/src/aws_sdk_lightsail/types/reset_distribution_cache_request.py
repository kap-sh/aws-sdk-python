"""Generated from Smithy shape ``com.amazonaws.lightsail#ResetDistributionCacheRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.resource_name


class ResetDistributionCacheRequest(TypedDict):
    distribution_name: NotRequired["aws_sdk_lightsail.types.resource_name.ResourceName"]
    """<p>The name of the distribution for which to reset cache.</p> <p>Use the <code>GetDistributions</code> action to get a list of distribution names that you can specify.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResetDistributionCacheRequest) -> dict:
    out: dict = {}
    if "distribution_name" in value:
        out["distributionName"] = value["distribution_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ResetDistributionCacheRequest:
    out: ResetDistributionCacheRequest = {}  # type: ignore[typeddict-item]
    if "distributionName" in data:
        out["distribution_name"] = data["distributionName"]
    return out
