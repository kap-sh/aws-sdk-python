"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsCloudFrontDistributionOriginGroupFailoverStatusCodes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.aws_cloud_front_distribution_origin_group_failover_status_codes_item_list
    import capo_securityhub.types.integer


class AwsCloudFrontDistributionOriginGroupFailoverStatusCodes(TypedDict, closed=True):
    items: NotRequired[
        "capo_securityhub.types.aws_cloud_front_distribution_origin_group_failover_status_codes_item_list.AwsCloudFrontDistributionOriginGroupFailoverStatusCodesItemList"
    ]
    """<p>The list of status code values that can cause a failover to the next origin.</p>"""
    quantity: NotRequired["capo_securityhub.types.integer.Integer"]
    """<p>The number of status codes that can cause a failover.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsCloudFrontDistributionOriginGroupFailoverStatusCodes,
) -> dict:
    out: dict = {}
    if "items" in value:
        import capo_securityhub.types.aws_cloud_front_distribution_origin_group_failover_status_codes_item_list

        out["Items"] = (
            capo_securityhub.types.aws_cloud_front_distribution_origin_group_failover_status_codes_item_list.serialize_json(
                value["items"]
            )
        )
    if "quantity" in value:
        out["Quantity"] = value["quantity"]
    return out


def deserialize_json(
    data: dict,
) -> AwsCloudFrontDistributionOriginGroupFailoverStatusCodes:
    out: AwsCloudFrontDistributionOriginGroupFailoverStatusCodes = {}  # type: ignore[typeddict-item]
    if "Items" in data:
        import capo_securityhub.types.aws_cloud_front_distribution_origin_group_failover_status_codes_item_list

        out["items"] = (
            capo_securityhub.types.aws_cloud_front_distribution_origin_group_failover_status_codes_item_list.deserialize_json(
                data["Items"]
            )
        )
    if "Quantity" in data:
        out["quantity"] = data["Quantity"]
    return out
