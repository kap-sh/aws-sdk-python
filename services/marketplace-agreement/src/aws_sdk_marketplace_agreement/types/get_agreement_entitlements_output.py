"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#GetAgreementEntitlementsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_marketplace_agreement.types.agreement_entitlement_list
    import aws_sdk_marketplace_agreement.types.next_token


class GetAgreementEntitlementsOutput(TypedDict, closed=True):
    agreement_entitlements: NotRequired[
        "aws_sdk_marketplace_agreement.types.agreement_entitlement_list.AgreementEntitlementList"
    ]
    """<p>A list of agreement entitlements which are part of the latest agreement.</p>"""
    next_token: NotRequired["aws_sdk_marketplace_agreement.types.next_token.NextToken"]
    """<p>The token used for pagination. The field is <code>null</code> if there are no more results.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetAgreementEntitlementsOutput) -> dict:
    out: dict = {}
    if "agreement_entitlements" in value:
        import aws_sdk_marketplace_agreement.types.agreement_entitlement_list

        out["agreementEntitlements"] = (
            aws_sdk_marketplace_agreement.types.agreement_entitlement_list.serialize_aws_json_1_0(
                value["agreement_entitlements"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetAgreementEntitlementsOutput:
    out: GetAgreementEntitlementsOutput = {}  # type: ignore[typeddict-item]
    if "agreementEntitlements" in data:
        import aws_sdk_marketplace_agreement.types.agreement_entitlement_list

        out["agreement_entitlements"] = (
            aws_sdk_marketplace_agreement.types.agreement_entitlement_list.deserialize_aws_json_1_0(
                data["agreementEntitlements"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
