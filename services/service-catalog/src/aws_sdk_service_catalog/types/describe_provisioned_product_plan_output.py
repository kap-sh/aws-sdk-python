"""Generated from Smithy shape ``com.amazonaws.servicecatalog#DescribeProvisionedProductPlanOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.page_token
    import aws_sdk_service_catalog.types.provisioned_product_plan_details
    import aws_sdk_service_catalog.types.resource_changes


class DescribeProvisionedProductPlanOutput(TypedDict, closed=True):
    provisioned_product_plan_details: NotRequired[
        "aws_sdk_service_catalog.types.provisioned_product_plan_details.ProvisionedProductPlanDetails"
    ]
    """<p>Information about the plan.</p>"""
    resource_changes: NotRequired[
        "aws_sdk_service_catalog.types.resource_changes.ResourceChanges"
    ]
    """<p>Information about the resource changes that will occur when the plan is executed.</p>"""
    next_page_token: NotRequired["aws_sdk_service_catalog.types.page_token.PageToken"]
    """<p>The page token to use to retrieve the next set of results. If there are no additional results, this value is null.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeProvisionedProductPlanOutput) -> dict:
    out: dict = {}
    if "provisioned_product_plan_details" in value:
        import aws_sdk_service_catalog.types.provisioned_product_plan_details

        out["ProvisionedProductPlanDetails"] = (
            aws_sdk_service_catalog.types.provisioned_product_plan_details.serialize_aws_json_1_1(
                value["provisioned_product_plan_details"]
            )
        )
    if "resource_changes" in value:
        import aws_sdk_service_catalog.types.resource_changes

        out["ResourceChanges"] = (
            aws_sdk_service_catalog.types.resource_changes.serialize_aws_json_1_1(
                value["resource_changes"]
            )
        )
    if "next_page_token" in value:
        out["NextPageToken"] = value["next_page_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeProvisionedProductPlanOutput:
    out: DescribeProvisionedProductPlanOutput = {}  # type: ignore[typeddict-item]
    if "ProvisionedProductPlanDetails" in data:
        import aws_sdk_service_catalog.types.provisioned_product_plan_details

        out["provisioned_product_plan_details"] = (
            aws_sdk_service_catalog.types.provisioned_product_plan_details.deserialize_aws_json_1_1(
                data["ProvisionedProductPlanDetails"]
            )
        )
    if "ResourceChanges" in data:
        import aws_sdk_service_catalog.types.resource_changes

        out["resource_changes"] = (
            aws_sdk_service_catalog.types.resource_changes.deserialize_aws_json_1_1(
                data["ResourceChanges"]
            )
        )
    if "NextPageToken" in data:
        out["next_page_token"] = data["NextPageToken"]
    return out
