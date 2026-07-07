"""Generated from Smithy shape ``com.amazonaws.billing#DisassociateSourceViewsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_billing.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_billing.types.billing_view_arn
    import aws_sdk_billing.types.billing_view_source_views_list


class DisassociateSourceViewsRequest(TypedDict, closed=True):
    arn: "aws_sdk_billing.types.billing_view_arn.BillingViewArn"
    """<p> The Amazon Resource Name (ARN) of the billing view to disassociate source views from. </p>"""
    source_views: "aws_sdk_billing.types.billing_view_source_views_list.BillingViewSourceViewsList"
    """<p> A list of ARNs of the source billing views to disassociate. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DisassociateSourceViewsRequest) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    import aws_sdk_billing.types.billing_view_source_views_list

    out["sourceViews"] = (
        aws_sdk_billing.types.billing_view_source_views_list.serialize_aws_json_1_0(
            value["source_views"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> DisassociateSourceViewsRequest:
    out: DisassociateSourceViewsRequest = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("DisassociateSourceViewsRequest.arn required")
    if "sourceViews" in data:
        import aws_sdk_billing.types.billing_view_source_views_list

        out["source_views"] = (
            aws_sdk_billing.types.billing_view_source_views_list.deserialize_aws_json_1_0(
                data["sourceViews"]
            )
        )
    else:
        raise DeserializationError(
            "DisassociateSourceViewsRequest.source_views required"
        )
    return out
