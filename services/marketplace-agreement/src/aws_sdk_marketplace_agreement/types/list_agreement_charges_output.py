"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#ListAgreementChargesOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_marketplace_agreement.types.charges
    import aws_sdk_marketplace_agreement.types.next_token


class ListAgreementChargesOutput(TypedDict):
    items: NotRequired["aws_sdk_marketplace_agreement.types.charges.Charges"]
    """<p>A list of agreement charges.</p>"""
    next_token: NotRequired["aws_sdk_marketplace_agreement.types.next_token.NextToken"]
    """<p>The token used for pagination. The field is <code>null</code> if there are no more results.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListAgreementChargesOutput) -> dict:
    out: dict = {}
    if "items" in value:
        import aws_sdk_marketplace_agreement.types.charges

        out["items"] = (
            aws_sdk_marketplace_agreement.types.charges.serialize_aws_json_1_0(
                value["items"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListAgreementChargesOutput:
    out: ListAgreementChargesOutput = {}  # type: ignore[typeddict-item]
    if "items" in data:
        import aws_sdk_marketplace_agreement.types.charges

        out["items"] = (
            aws_sdk_marketplace_agreement.types.charges.deserialize_aws_json_1_0(
                data["items"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
