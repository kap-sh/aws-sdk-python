"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#GrantList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_marketplace_agreement.types.grant_item

GrantList: TypeAlias = list["aws_sdk_marketplace_agreement.types.grant_item.GrantItem"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GrantList) -> list:
    import aws_sdk_marketplace_agreement.types.grant_item

    out: list = []
    for item in value:
        out.append(
            aws_sdk_marketplace_agreement.types.grant_item.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> GrantList:
    import aws_sdk_marketplace_agreement.types.grant_item

    out: GrantList = []
    for item in data:
        out.append(
            aws_sdk_marketplace_agreement.types.grant_item.deserialize_aws_json_1_0(
                item
            )
        )
    return out
