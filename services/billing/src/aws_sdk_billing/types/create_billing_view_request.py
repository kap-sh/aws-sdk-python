"""Generated from Smithy shape ``com.amazonaws.billing#CreateBillingViewRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_billing.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_billing.types.billing_view_description
    import aws_sdk_billing.types.billing_view_name
    import aws_sdk_billing.types.billing_view_source_views_list
    import aws_sdk_billing.types.client_token
    import aws_sdk_billing.types.expression
    import aws_sdk_billing.types.resource_tag_list


class CreateBillingViewRequest(TypedDict, closed=True):
    name: "aws_sdk_billing.types.billing_view_name.BillingViewName"
    """<p> The name of the billing view. </p>"""
    description: NotRequired[
        "aws_sdk_billing.types.billing_view_description.BillingViewDescription"
    ]
    """<p> The description of the billing view. </p>"""
    source_views: "aws_sdk_billing.types.billing_view_source_views_list.BillingViewSourceViewsList"
    """<p>A list of billing views used as the data source for the custom billing view.</p>"""
    data_filter_expression: NotRequired["aws_sdk_billing.types.expression.Expression"]
    r"""<p> See <a href=\"https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_billing_Expression.html\">Expression</a>. Billing view only supports <code>LINKED_ACCOUNT</code>, <code>Tags</code>, and <code>CostCategories</code>. </p>"""
    client_token: NotRequired["aws_sdk_billing.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier you specify to ensure idempotency of the request. Idempotency ensures that an API request completes no more than one time. If the original request completes successfully, any subsequent retries complete successfully without performing any further actions with an idempotent request. </p>"""
    resource_tags: NotRequired[
        "aws_sdk_billing.types.resource_tag_list.ResourceTagList"
    ]
    """<p>A list of key value map specifying tags associated to the billing view being created. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateBillingViewRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    import aws_sdk_billing.types.billing_view_source_views_list

    out["sourceViews"] = (
        aws_sdk_billing.types.billing_view_source_views_list.serialize_aws_json_1_0(
            value["source_views"]
        )
    )
    if "data_filter_expression" in value:
        import aws_sdk_billing.types.expression

        out["dataFilterExpression"] = (
            aws_sdk_billing.types.expression.serialize_aws_json_1_0(
                value["data_filter_expression"]
            )
        )
    if "resource_tags" in value:
        import aws_sdk_billing.types.resource_tag_list

        out["resourceTags"] = (
            aws_sdk_billing.types.resource_tag_list.serialize_aws_json_1_0(
                value["resource_tags"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateBillingViewRequest:
    out: CreateBillingViewRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateBillingViewRequest.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "sourceViews" in data:
        import aws_sdk_billing.types.billing_view_source_views_list

        out["source_views"] = (
            aws_sdk_billing.types.billing_view_source_views_list.deserialize_aws_json_1_0(
                data["sourceViews"]
            )
        )
    else:
        raise DeserializationError("CreateBillingViewRequest.source_views required")
    if "dataFilterExpression" in data:
        import aws_sdk_billing.types.expression

        out["data_filter_expression"] = (
            aws_sdk_billing.types.expression.deserialize_aws_json_1_0(
                data["dataFilterExpression"]
            )
        )
    if "resourceTags" in data:
        import aws_sdk_billing.types.resource_tag_list

        out["resource_tags"] = (
            aws_sdk_billing.types.resource_tag_list.deserialize_aws_json_1_0(
                data["resourceTags"]
            )
        )
    return out
