"""Generated from Smithy shape ``com.amazonaws.servicecatalog#DescribeProductOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.budgets
    import aws_sdk_service_catalog.types.launch_paths
    import aws_sdk_service_catalog.types.product_view_summary
    import aws_sdk_service_catalog.types.provisioning_artifacts


class DescribeProductOutput(TypedDict):
    product_view_summary: NotRequired[
        "aws_sdk_service_catalog.types.product_view_summary.ProductViewSummary"
    ]
    """<p>Summary information about the product view.</p>"""
    provisioning_artifacts: NotRequired[
        "aws_sdk_service_catalog.types.provisioning_artifacts.ProvisioningArtifacts"
    ]
    """<p>Information about the provisioning artifacts for the specified product.</p>"""
    budgets: NotRequired["aws_sdk_service_catalog.types.budgets.Budgets"]
    """<p>Information about the associated budgets.</p>"""
    launch_paths: NotRequired["aws_sdk_service_catalog.types.launch_paths.LaunchPaths"]
    """<p>Information about the associated launch paths.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeProductOutput) -> dict:
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
    if "budgets" in value:
        import aws_sdk_service_catalog.types.budgets

        out["Budgets"] = aws_sdk_service_catalog.types.budgets.serialize_aws_json_1_1(
            value["budgets"]
        )
    if "launch_paths" in value:
        import aws_sdk_service_catalog.types.launch_paths

        out["LaunchPaths"] = (
            aws_sdk_service_catalog.types.launch_paths.serialize_aws_json_1_1(
                value["launch_paths"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeProductOutput:
    out: DescribeProductOutput = {}  # type: ignore[typeddict-item]
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
    if "Budgets" in data:
        import aws_sdk_service_catalog.types.budgets

        out["budgets"] = aws_sdk_service_catalog.types.budgets.deserialize_aws_json_1_1(
            data["Budgets"]
        )
    if "LaunchPaths" in data:
        import aws_sdk_service_catalog.types.launch_paths

        out["launch_paths"] = (
            aws_sdk_service_catalog.types.launch_paths.deserialize_aws_json_1_1(
                data["LaunchPaths"]
            )
        )
    return out
