"""Generated from Smithy shape ``com.amazonaws.lightsail#BucketBundle``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.boolean
    import aws_sdk_lightsail.types.float
    import aws_sdk_lightsail.types.integer
    import aws_sdk_lightsail.types.non_empty_string


class BucketBundle(TypedDict, closed=True):
    bundle_id: NotRequired["aws_sdk_lightsail.types.non_empty_string.NonEmptyString"]
    """<p>The ID of the bundle.</p>"""
    name: NotRequired["aws_sdk_lightsail.types.non_empty_string.NonEmptyString"]
    """<p>The name of the bundle.</p>"""
    price: NotRequired["aws_sdk_lightsail.types.float.float"]
    """<p>The monthly price of the bundle, in US dollars.</p>"""
    storage_per_month_in_gb: NotRequired["aws_sdk_lightsail.types.integer.integer"]
    """<p>The storage size of the bundle, in GB.</p>"""
    transfer_per_month_in_gb: NotRequired["aws_sdk_lightsail.types.integer.integer"]
    """<p>The monthly network transfer quota of the bundle.</p>"""
    is_active: NotRequired["aws_sdk_lightsail.types.boolean.boolean"]
    """<p>Indicates whether the bundle is active. Use for a new or existing bucket.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BucketBundle) -> dict:
    out: dict = {}
    if "bundle_id" in value:
        out["bundleId"] = value["bundle_id"]
    if "name" in value:
        out["name"] = value["name"]
    if "price" in value:
        out["price"] = value["price"]
    if "storage_per_month_in_gb" in value:
        out["storagePerMonthInGb"] = value["storage_per_month_in_gb"]
    if "transfer_per_month_in_gb" in value:
        out["transferPerMonthInGb"] = value["transfer_per_month_in_gb"]
    if "is_active" in value:
        out["isActive"] = value["is_active"]
    return out


def deserialize_aws_json_1_1(data: dict) -> BucketBundle:
    out: BucketBundle = {}  # type: ignore[typeddict-item]
    if "bundleId" in data:
        out["bundle_id"] = data["bundleId"]
    if "name" in data:
        out["name"] = data["name"]
    if "price" in data:
        out["price"] = data["price"]
    if "storagePerMonthInGb" in data:
        out["storage_per_month_in_gb"] = data["storagePerMonthInGb"]
    if "transferPerMonthInGb" in data:
        out["transfer_per_month_in_gb"] = data["transferPerMonthInGb"]
    if "isActive" in data:
        out["is_active"] = data["isActive"]
    return out
