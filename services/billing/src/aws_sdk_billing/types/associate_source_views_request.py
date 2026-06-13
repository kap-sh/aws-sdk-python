"""Generated from Smithy shape ``com.amazonaws.billing#AssociateSourceViewsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_billing.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_billing.types.billing_view_arn
    import aws_sdk_billing.types.billing_view_source_views_list


class AssociateSourceViewsRequest(TypedDict):
    arn: "aws_sdk_billing.types.billing_view_arn.BillingViewArn"
    """<p> The Amazon Resource Name (ARN) of the billing view to associate source views with. </p>"""
    source_views: "aws_sdk_billing.types.billing_view_source_views_list.BillingViewSourceViewsList"
    """<p> A list of ARNs of the source billing views to associate. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AssociateSourceViewsRequest) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    import aws_sdk_billing.types.billing_view_source_views_list

    out["sourceViews"] = (
        aws_sdk_billing.types.billing_view_source_views_list.serialize_aws_json_1_0(
            value["source_views"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> AssociateSourceViewsRequest:
    out: AssociateSourceViewsRequest = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("AssociateSourceViewsRequest.arn required")
    if "sourceViews" in data:
        import aws_sdk_billing.types.billing_view_source_views_list

        out["source_views"] = (
            aws_sdk_billing.types.billing_view_source_views_list.deserialize_aws_json_1_0(
                data["sourceViews"]
            )
        )
    else:
        raise DeserializationError("AssociateSourceViewsRequest.source_views required")
    return out
