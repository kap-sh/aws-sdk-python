"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#EntitlementList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_marketplace_agreement.types.entitlement

EntitlementList: TypeAlias = list[
    "aws_sdk_marketplace_agreement.types.entitlement.Entitlement"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EntitlementList) -> list:
    import aws_sdk_marketplace_agreement.types.entitlement

    out: list = []
    for item in value:
        out.append(
            aws_sdk_marketplace_agreement.types.entitlement.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> EntitlementList:
    import aws_sdk_marketplace_agreement.types.entitlement

    out: EntitlementList = []
    for item in data:
        out.append(
            aws_sdk_marketplace_agreement.types.entitlement.deserialize_aws_json_1_0(
                item
            )
        )
    return out
