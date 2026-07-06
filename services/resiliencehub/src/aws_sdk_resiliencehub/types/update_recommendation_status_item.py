"""Generated from Smithy shape ``com.amazonaws.resiliencehub#UpdateRecommendationStatusItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_resiliencehub.types.aws_region
    import aws_sdk_resiliencehub.types.customer_id
    import aws_sdk_resiliencehub.types.string500


class UpdateRecommendationStatusItem(TypedDict, closed=True):
    resource_id: NotRequired["aws_sdk_resiliencehub.types.string500.String500"]
    """<p>Resource identifier of the operational recommendation item.</p>"""
    target_account_id: NotRequired["aws_sdk_resiliencehub.types.customer_id.CustomerId"]
    """<p>Identifier of the target Amazon Web Services account.</p>"""
    target_region: NotRequired["aws_sdk_resiliencehub.types.aws_region.AwsRegion"]
    """<p>Identifier of the target Amazon Web Services Region.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRecommendationStatusItem) -> dict:
    out: dict = {}
    if "resource_id" in value:
        out["resourceId"] = value["resource_id"]
    if "target_account_id" in value:
        out["targetAccountId"] = value["target_account_id"]
    if "target_region" in value:
        out["targetRegion"] = value["target_region"]
    return out


def deserialize_json(data: dict) -> UpdateRecommendationStatusItem:
    out: UpdateRecommendationStatusItem = {}  # type: ignore[typeddict-item]
    if "resourceId" in data:
        out["resource_id"] = data["resourceId"]
    if "targetAccountId" in data:
        out["target_account_id"] = data["targetAccountId"]
    if "targetRegion" in data:
        out["target_region"] = data["targetRegion"]
    return out
