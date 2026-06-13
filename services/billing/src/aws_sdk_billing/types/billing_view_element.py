"""Generated from Smithy shape ``com.amazonaws.billing#BillingViewElement``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import datetime

    import aws_sdk_billing.types.account_id
    import aws_sdk_billing.types.billing_view_arn
    import aws_sdk_billing.types.billing_view_description
    import aws_sdk_billing.types.billing_view_health_status
    import aws_sdk_billing.types.billing_view_name
    import aws_sdk_billing.types.billing_view_type
    import aws_sdk_billing.types.expression


class BillingViewElement(TypedDict):
    arn: NotRequired["aws_sdk_billing.types.billing_view_arn.BillingViewArn"]
    """<p> The Amazon Resource Name (ARN) that can be used to uniquely identify the billing view. </p>"""
    name: NotRequired["aws_sdk_billing.types.billing_view_name.BillingViewName"]
    """<p> The account name of the billing view. </p>"""
    description: NotRequired[
        "aws_sdk_billing.types.billing_view_description.BillingViewDescription"
    ]
    """<p> The description of the billing view. </p>"""
    billing_view_type: NotRequired[
        "aws_sdk_billing.types.billing_view_type.BillingViewType"
    ]
    """<p>The type of billing group. </p>"""
    owner_account_id: NotRequired["aws_sdk_billing.types.account_id.AccountId"]
    """<p>The account owner of the billing view. </p>"""
    source_account_id: NotRequired["aws_sdk_billing.types.account_id.AccountId"]
    """<p> The Amazon Web Services account ID that owns the source billing view, if this is a derived billing view. </p>"""
    data_filter_expression: NotRequired["aws_sdk_billing.types.expression.Expression"]
    """<p> See <a href=\"https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_billing_Expression.html\">Expression</a>. Billing view only supports <code>LINKED_ACCOUNT</code>, <code>Tags</code>, and <code>CostCategories</code>. </p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The time when the billing view was created. </p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The time when the billing view was last updated. </p>"""
    derived_view_count: NotRequired["int"]
    """<p> The number of billing views that use this billing view as a source. </p>"""
    source_view_count: NotRequired["int"]
    """<p> The number of source views associated with this billing view. </p>"""
    view_definition_last_updated_at: NotRequired["datetime.datetime"]
    """<p> The timestamp of when the billing view definition was last updated. </p>"""
    health_status: NotRequired[
        "aws_sdk_billing.types.billing_view_health_status.BillingViewHealthStatus"
    ]
    """<p> The current health status of the billing view. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BillingViewElement) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "billing_view_type" in value:
        import aws_sdk_billing.types.billing_view_type

        out["billingViewType"] = (
            aws_sdk_billing.types.billing_view_type.serialize_aws_json_1_0(
                value["billing_view_type"]
            )
        )
    if "owner_account_id" in value:
        out["ownerAccountId"] = value["owner_account_id"]
    if "source_account_id" in value:
        out["sourceAccountId"] = value["source_account_id"]
    if "data_filter_expression" in value:
        import aws_sdk_billing.types.expression

        out["dataFilterExpression"] = (
            aws_sdk_billing.types.expression.serialize_aws_json_1_0(
                value["data_filter_expression"]
            )
        )
    if "created_at" in value:
        import aws_sdk_billing.types._prelude.timestamp

        out["createdAt"] = (
            aws_sdk_billing.types._prelude.timestamp.serialize_aws_json_1_0(
                value["created_at"]
            )
        )
    if "updated_at" in value:
        import aws_sdk_billing.types._prelude.timestamp

        out["updatedAt"] = (
            aws_sdk_billing.types._prelude.timestamp.serialize_aws_json_1_0(
                value["updated_at"]
            )
        )
    if "derived_view_count" in value:
        out["derivedViewCount"] = value["derived_view_count"]
    if "source_view_count" in value:
        out["sourceViewCount"] = value["source_view_count"]
    if "view_definition_last_updated_at" in value:
        import aws_sdk_billing.types._prelude.timestamp

        out["viewDefinitionLastUpdatedAt"] = (
            aws_sdk_billing.types._prelude.timestamp.serialize_aws_json_1_0(
                value["view_definition_last_updated_at"]
            )
        )
    if "health_status" in value:
        import aws_sdk_billing.types.billing_view_health_status

        out["healthStatus"] = (
            aws_sdk_billing.types.billing_view_health_status.serialize_aws_json_1_0(
                value["health_status"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> BillingViewElement:
    out: BillingViewElement = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    if "billingViewType" in data:
        import aws_sdk_billing.types.billing_view_type

        out["billing_view_type"] = (
            aws_sdk_billing.types.billing_view_type.deserialize_aws_json_1_0(
                data["billingViewType"]
            )
        )
    if "ownerAccountId" in data:
        out["owner_account_id"] = data["ownerAccountId"]
    if "sourceAccountId" in data:
        out["source_account_id"] = data["sourceAccountId"]
    if "dataFilterExpression" in data:
        import aws_sdk_billing.types.expression

        out["data_filter_expression"] = (
            aws_sdk_billing.types.expression.deserialize_aws_json_1_0(
                data["dataFilterExpression"]
            )
        )
    if "createdAt" in data:
        import aws_sdk_billing.types._prelude.timestamp

        out["created_at"] = (
            aws_sdk_billing.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["createdAt"]
            )
        )
    if "updatedAt" in data:
        import aws_sdk_billing.types._prelude.timestamp

        out["updated_at"] = (
            aws_sdk_billing.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["updatedAt"]
            )
        )
    if "derivedViewCount" in data:
        out["derived_view_count"] = data["derivedViewCount"]
    if "sourceViewCount" in data:
        out["source_view_count"] = data["sourceViewCount"]
    if "viewDefinitionLastUpdatedAt" in data:
        import aws_sdk_billing.types._prelude.timestamp

        out["view_definition_last_updated_at"] = (
            aws_sdk_billing.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["viewDefinitionLastUpdatedAt"]
            )
        )
    if "healthStatus" in data:
        import aws_sdk_billing.types.billing_view_health_status

        out["health_status"] = (
            aws_sdk_billing.types.billing_view_health_status.deserialize_aws_json_1_0(
                data["healthStatus"]
            )
        )
    return out
