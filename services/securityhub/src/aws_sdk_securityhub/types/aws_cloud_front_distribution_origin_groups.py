"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsCloudFrontDistributionOriginGroups``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_cloud_front_distribution_origin_groups_item_list


class AwsCloudFrontDistributionOriginGroups(TypedDict, closed=True):
    items: NotRequired[
        "aws_sdk_securityhub.types.aws_cloud_front_distribution_origin_groups_item_list.AwsCloudFrontDistributionOriginGroupsItemList"
    ]
    """<p>The list of origin groups.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsCloudFrontDistributionOriginGroups) -> dict:
    out: dict = {}
    if "items" in value:
        import aws_sdk_securityhub.types.aws_cloud_front_distribution_origin_groups_item_list

        out["Items"] = (
            aws_sdk_securityhub.types.aws_cloud_front_distribution_origin_groups_item_list.serialize_json(
                value["items"]
            )
        )
    return out


def deserialize_json(data: dict) -> AwsCloudFrontDistributionOriginGroups:
    out: AwsCloudFrontDistributionOriginGroups = {}  # type: ignore[typeddict-item]
    if "Items" in data:
        import aws_sdk_securityhub.types.aws_cloud_front_distribution_origin_groups_item_list

        out["items"] = (
            aws_sdk_securityhub.types.aws_cloud_front_distribution_origin_groups_item_list.deserialize_json(
                data["Items"]
            )
        )
    return out
