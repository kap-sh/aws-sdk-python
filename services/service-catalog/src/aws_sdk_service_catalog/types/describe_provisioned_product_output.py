"""Generated from Smithy shape ``com.amazonaws.servicecatalog#DescribeProvisionedProductOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.cloud_watch_dashboards
    import aws_sdk_service_catalog.types.provisioned_product_detail


class DescribeProvisionedProductOutput(TypedDict):
    provisioned_product_detail: NotRequired[
        "aws_sdk_service_catalog.types.provisioned_product_detail.ProvisionedProductDetail"
    ]
    """<p>Information about the provisioned product.</p>"""
    cloud_watch_dashboards: NotRequired[
        "aws_sdk_service_catalog.types.cloud_watch_dashboards.CloudWatchDashboards"
    ]
    """<p>Any CloudWatch dashboards that were created when provisioning the product.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeProvisionedProductOutput) -> dict:
    out: dict = {}
    if "provisioned_product_detail" in value:
        import aws_sdk_service_catalog.types.provisioned_product_detail

        out["ProvisionedProductDetail"] = (
            aws_sdk_service_catalog.types.provisioned_product_detail.serialize_aws_json_1_1(
                value["provisioned_product_detail"]
            )
        )
    if "cloud_watch_dashboards" in value:
        import aws_sdk_service_catalog.types.cloud_watch_dashboards

        out["CloudWatchDashboards"] = (
            aws_sdk_service_catalog.types.cloud_watch_dashboards.serialize_aws_json_1_1(
                value["cloud_watch_dashboards"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeProvisionedProductOutput:
    out: DescribeProvisionedProductOutput = {}  # type: ignore[typeddict-item]
    if "ProvisionedProductDetail" in data:
        import aws_sdk_service_catalog.types.provisioned_product_detail

        out["provisioned_product_detail"] = (
            aws_sdk_service_catalog.types.provisioned_product_detail.deserialize_aws_json_1_1(
                data["ProvisionedProductDetail"]
            )
        )
    if "CloudWatchDashboards" in data:
        import aws_sdk_service_catalog.types.cloud_watch_dashboards

        out["cloud_watch_dashboards"] = (
            aws_sdk_service_catalog.types.cloud_watch_dashboards.deserialize_aws_json_1_1(
                data["CloudWatchDashboards"]
            )
        )
    return out
