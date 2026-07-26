"""Generated from Smithy shape ``com.amazonaws.lightsail#DistributionBundle``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.boolean
    import capo_lightsail.types.float
    import capo_lightsail.types.integer
    import capo_lightsail.types.string


class DistributionBundle(TypedDict, closed=True):
    bundle_id: NotRequired["capo_lightsail.types.string.string"]
    """<p>The ID of the bundle.</p>"""
    name: NotRequired["capo_lightsail.types.string.string"]
    """<p>The name of the distribution bundle.</p>"""
    price: NotRequired["capo_lightsail.types.float.float"]
    """<p>The monthly price, in US dollars, of the bundle.</p>"""
    transfer_per_month_in_gb: NotRequired["capo_lightsail.types.integer.integer"]
    """<p>The monthly network transfer quota of the bundle.</p>"""
    is_active: NotRequired["capo_lightsail.types.boolean.boolean"]
    """<p>Indicates whether the bundle is active, and can be specified for a new or existing distribution.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DistributionBundle) -> dict:
    out: dict = {}
    if "bundle_id" in value:
        out["bundleId"] = value["bundle_id"]
    if "name" in value:
        out["name"] = value["name"]
    if "price" in value:
        out["price"] = value["price"]
    if "transfer_per_month_in_gb" in value:
        out["transferPerMonthInGb"] = value["transfer_per_month_in_gb"]
    if "is_active" in value:
        out["isActive"] = value["is_active"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DistributionBundle:
    out: DistributionBundle = {}  # type: ignore[typeddict-item]
    if "bundleId" in data:
        out["bundle_id"] = data["bundleId"]
    if "name" in data:
        out["name"] = data["name"]
    if "price" in data:
        out["price"] = data["price"]
    if "transferPerMonthInGb" in data:
        out["transfer_per_month_in_gb"] = data["transferPerMonthInGb"]
    if "isActive" in data:
        out["is_active"] = data["isActive"]
    return out
