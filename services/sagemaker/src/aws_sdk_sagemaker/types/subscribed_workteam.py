"""Generated from Smithy shape ``com.amazonaws.sagemaker#SubscribedWorkteam``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.string
    import aws_sdk_sagemaker.types.string200
    import aws_sdk_sagemaker.types.workteam_arn


class SubscribedWorkteam(TypedDict):
    workteam_arn: NotRequired["aws_sdk_sagemaker.types.workteam_arn.WorkteamArn"]
    """<p>The Amazon Resource Name (ARN) of the vendor that you have subscribed.</p>"""
    marketplace_title: NotRequired["aws_sdk_sagemaker.types.string200.String200"]
    """<p>The title of the service provided by the vendor in the Amazon Marketplace.</p>"""
    seller_name: NotRequired["aws_sdk_sagemaker.types.string.String"]
    """<p>The name of the vendor in the Amazon Marketplace.</p>"""
    marketplace_description: NotRequired["aws_sdk_sagemaker.types.string200.String200"]
    """<p>The description of the vendor from the Amazon Marketplace.</p>"""
    listing_id: NotRequired["aws_sdk_sagemaker.types.string.String"]
    """<p>Marketplace product listing ID.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SubscribedWorkteam) -> dict:
    out: dict = {}
    if "workteam_arn" in value:
        out["WorkteamArn"] = value["workteam_arn"]
    if "marketplace_title" in value:
        out["MarketplaceTitle"] = value["marketplace_title"]
    if "seller_name" in value:
        out["SellerName"] = value["seller_name"]
    if "marketplace_description" in value:
        out["MarketplaceDescription"] = value["marketplace_description"]
    if "listing_id" in value:
        out["ListingId"] = value["listing_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SubscribedWorkteam:
    out: SubscribedWorkteam = {}  # type: ignore[typeddict-item]
    if "WorkteamArn" in data:
        out["workteam_arn"] = data["WorkteamArn"]
    if "MarketplaceTitle" in data:
        out["marketplace_title"] = data["MarketplaceTitle"]
    if "SellerName" in data:
        out["seller_name"] = data["SellerName"]
    if "MarketplaceDescription" in data:
        out["marketplace_description"] = data["MarketplaceDescription"]
    if "ListingId" in data:
        out["listing_id"] = data["ListingId"]
    return out
