"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ProvisioningArtifactView``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.product_view_summary
    import aws_sdk_service_catalog.types.provisioning_artifact


class ProvisioningArtifactView(TypedDict):
    product_view_summary: NotRequired[
        "aws_sdk_service_catalog.types.product_view_summary.ProductViewSummary"
    ]
    """<p>Summary information about a product view.</p>"""
    provisioning_artifact: NotRequired[
        "aws_sdk_service_catalog.types.provisioning_artifact.ProvisioningArtifact"
    ]
    """<p>Information about a provisioning artifact. A provisioning artifact is also known as a product version.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProvisioningArtifactView) -> dict:
    out: dict = {}
    if "product_view_summary" in value:
        import aws_sdk_service_catalog.types.product_view_summary

        out["ProductViewSummary"] = (
            aws_sdk_service_catalog.types.product_view_summary.serialize_aws_json_1_1(
                value["product_view_summary"]
            )
        )
    if "provisioning_artifact" in value:
        import aws_sdk_service_catalog.types.provisioning_artifact

        out["ProvisioningArtifact"] = (
            aws_sdk_service_catalog.types.provisioning_artifact.serialize_aws_json_1_1(
                value["provisioning_artifact"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ProvisioningArtifactView:
    out: ProvisioningArtifactView = {}  # type: ignore[typeddict-item]
    if "ProductViewSummary" in data:
        import aws_sdk_service_catalog.types.product_view_summary

        out["product_view_summary"] = (
            aws_sdk_service_catalog.types.product_view_summary.deserialize_aws_json_1_1(
                data["ProductViewSummary"]
            )
        )
    if "ProvisioningArtifact" in data:
        import aws_sdk_service_catalog.types.provisioning_artifact

        out["provisioning_artifact"] = (
            aws_sdk_service_catalog.types.provisioning_artifact.deserialize_aws_json_1_1(
                data["ProvisioningArtifact"]
            )
        )
    return out
