"""Generated from Smithy shape ``com.amazonaws.lightsail#UpdateDistributionBundleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.resource_name
    import capo_lightsail.types.string


class UpdateDistributionBundleRequest(TypedDict, closed=True):
    distribution_name: NotRequired["capo_lightsail.types.resource_name.ResourceName"]
    """<p>The name of the distribution for which to update the bundle.</p> <p>Use the <code>GetDistributions</code> action to get a list of distribution names that you can specify.</p>"""
    bundle_id: NotRequired["capo_lightsail.types.string.string"]
    """<p>The bundle ID of the new bundle to apply to your distribution.</p> <p>Use the <code>GetDistributionBundles</code> action to get a list of distribution bundle IDs that you can specify.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateDistributionBundleRequest) -> dict:
    out: dict = {}
    if "distribution_name" in value:
        out["distributionName"] = value["distribution_name"]
    if "bundle_id" in value:
        out["bundleId"] = value["bundle_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateDistributionBundleRequest:
    out: UpdateDistributionBundleRequest = {}  # type: ignore[typeddict-item]
    if "distributionName" in data:
        out["distribution_name"] = data["distributionName"]
    if "bundleId" in data:
        out["bundle_id"] = data["bundleId"]
    return out
