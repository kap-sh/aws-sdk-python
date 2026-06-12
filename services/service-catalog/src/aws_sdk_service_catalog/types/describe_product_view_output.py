"""Generated from Smithy shape ``com.amazonaws.servicecatalog#DescribeProductViewOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.product_view_summary
    import aws_sdk_service_catalog.types.provisioning_artifacts


class DescribeProductViewOutput(TypedDict):
    product_view_summary: NotRequired[
        "aws_sdk_service_catalog.types.product_view_summary.ProductViewSummary"
    ]
    """<p>Summary information about the product.</p>"""
    provisioning_artifacts: NotRequired[
        "aws_sdk_service_catalog.types.provisioning_artifacts.ProvisioningArtifacts"
    ]
    """<p>Information about the provisioning artifacts for the product.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeProductViewOutput) -> dict:
    out: dict = {}
    if "product_view_summary" in value:
        import aws_sdk_service_catalog.types.product_view_summary

        out["ProductViewSummary"] = (
            aws_sdk_service_catalog.types.product_view_summary.serialize_aws_json_1_1(
                value["product_view_summary"]
            )
        )
    if "provisioning_artifacts" in value:
        import aws_sdk_service_catalog.types.provisioning_artifacts

        out["ProvisioningArtifacts"] = (
            aws_sdk_service_catalog.types.provisioning_artifacts.serialize_aws_json_1_1(
                value["provisioning_artifacts"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeProductViewOutput:
    out: DescribeProductViewOutput = {}  # type: ignore[typeddict-item]
    if "ProductViewSummary" in data:
        import aws_sdk_service_catalog.types.product_view_summary

        out["product_view_summary"] = (
            aws_sdk_service_catalog.types.product_view_summary.deserialize_aws_json_1_1(
                data["ProductViewSummary"]
            )
        )
    if "ProvisioningArtifacts" in data:
        import aws_sdk_service_catalog.types.provisioning_artifacts

        out["provisioning_artifacts"] = (
            aws_sdk_service_catalog.types.provisioning_artifacts.deserialize_aws_json_1_1(
                data["ProvisioningArtifacts"]
            )
        )
    return out
