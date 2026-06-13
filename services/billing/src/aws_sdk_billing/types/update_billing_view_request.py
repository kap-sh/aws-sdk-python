"""Generated from Smithy shape ``com.amazonaws.billing#UpdateBillingViewRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_billing.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_billing.types.billing_view_arn
    import aws_sdk_billing.types.billing_view_description
    import aws_sdk_billing.types.billing_view_name
    import aws_sdk_billing.types.expression


class UpdateBillingViewRequest(TypedDict):
    arn: "aws_sdk_billing.types.billing_view_arn.BillingViewArn"
    """<p> The Amazon Resource Name (ARN) that can be used to uniquely identify the billing view. </p>"""
    name: NotRequired["aws_sdk_billing.types.billing_view_name.BillingViewName"]
    """<p> The name of the billing view. </p>"""
    description: NotRequired[
        "aws_sdk_billing.types.billing_view_description.BillingViewDescription"
    ]
    """<p> The description of the billing view. </p>"""
    data_filter_expression: NotRequired["aws_sdk_billing.types.expression.Expression"]
    """<p>See <a href=\"https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_billing_Expression.html\">Expression</a>. Billing view only supports <code>LINKED_ACCOUNT</code>, <code>Tags</code>, and <code>CostCategories</code>. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateBillingViewRequest) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "data_filter_expression" in value:
        import aws_sdk_billing.types.expression

        out["dataFilterExpression"] = (
            aws_sdk_billing.types.expression.serialize_aws_json_1_0(
                value["data_filter_expression"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateBillingViewRequest:
    out: UpdateBillingViewRequest = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("UpdateBillingViewRequest.arn required")
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    if "dataFilterExpression" in data:
        import aws_sdk_billing.types.expression

        out["data_filter_expression"] = (
            aws_sdk_billing.types.expression.deserialize_aws_json_1_0(
                data["dataFilterExpression"]
            )
        )
    return out
