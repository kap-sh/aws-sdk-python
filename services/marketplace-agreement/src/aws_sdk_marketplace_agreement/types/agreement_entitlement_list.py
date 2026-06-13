"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#AgreementEntitlementList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_marketplace_agreement.types.agreement_entitlement

AgreementEntitlementList: TypeAlias = list[
    "aws_sdk_marketplace_agreement.types.agreement_entitlement.AgreementEntitlement"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AgreementEntitlementList) -> list:
    import aws_sdk_marketplace_agreement.types.agreement_entitlement

    out: list = []
    for item in value:
        out.append(
            aws_sdk_marketplace_agreement.types.agreement_entitlement.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> AgreementEntitlementList:
    import aws_sdk_marketplace_agreement.types.agreement_entitlement

    out: AgreementEntitlementList = []
    for item in data:
        out.append(
            aws_sdk_marketplace_agreement.types.agreement_entitlement.deserialize_aws_json_1_0(
                item
            )
        )
    return out
