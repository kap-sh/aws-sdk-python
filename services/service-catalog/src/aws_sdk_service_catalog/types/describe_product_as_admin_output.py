"""Generated from Smithy shape ``com.amazonaws.servicecatalog#DescribeProductAsAdminOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.budgets
    import aws_sdk_service_catalog.types.product_view_detail
    import aws_sdk_service_catalog.types.provisioning_artifact_summaries
    import aws_sdk_service_catalog.types.tag_option_details
    import aws_sdk_service_catalog.types.tags


class DescribeProductAsAdminOutput(TypedDict):
    product_view_detail: NotRequired[
        "aws_sdk_service_catalog.types.product_view_detail.ProductViewDetail"
    ]
    """<p>Information about the product view.</p>"""
    provisioning_artifact_summaries: NotRequired[
        "aws_sdk_service_catalog.types.provisioning_artifact_summaries.ProvisioningArtifactSummaries"
    ]
    """<p>Information about the provisioning artifacts (also known as versions) for the specified product.</p>"""
    tags: NotRequired["aws_sdk_service_catalog.types.tags.Tags"]
    """<p>Information about the tags associated with the product.</p>"""
    tag_options: NotRequired[
        "aws_sdk_service_catalog.types.tag_option_details.TagOptionDetails"
    ]
    """<p>Information about the TagOptions associated with the product.</p>"""
    budgets: NotRequired["aws_sdk_service_catalog.types.budgets.Budgets"]
    """<p>Information about the associated budgets.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeProductAsAdminOutput) -> dict:
    out: dict = {}
    if "product_view_detail" in value:
        import aws_sdk_service_catalog.types.product_view_detail

        out["ProductViewDetail"] = (
            aws_sdk_service_catalog.types.product_view_detail.serialize_aws_json_1_1(
                value["product_view_detail"]
            )
        )
    if "provisioning_artifact_summaries" in value:
        import aws_sdk_service_catalog.types.provisioning_artifact_summaries

        out["ProvisioningArtifactSummaries"] = (
            aws_sdk_service_catalog.types.provisioning_artifact_summaries.serialize_aws_json_1_1(
                value["provisioning_artifact_summaries"]
            )
        )
    if "tags" in value:
        import aws_sdk_service_catalog.types.tags

        out["Tags"] = aws_sdk_service_catalog.types.tags.serialize_aws_json_1_1(
            value["tags"]
        )
    if "tag_options" in value:
        import aws_sdk_service_catalog.types.tag_option_details

        out["TagOptions"] = (
            aws_sdk_service_catalog.types.tag_option_details.serialize_aws_json_1_1(
                value["tag_options"]
            )
        )
    if "budgets" in value:
        import aws_sdk_service_catalog.types.budgets

        out["Budgets"] = aws_sdk_service_catalog.types.budgets.serialize_aws_json_1_1(
            value["budgets"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeProductAsAdminOutput:
    out: DescribeProductAsAdminOutput = {}  # type: ignore[typeddict-item]
    if "ProductViewDetail" in data:
        import aws_sdk_service_catalog.types.product_view_detail

        out["product_view_detail"] = (
            aws_sdk_service_catalog.types.product_view_detail.deserialize_aws_json_1_1(
                data["ProductViewDetail"]
            )
        )
    if "ProvisioningArtifactSummaries" in data:
        import aws_sdk_service_catalog.types.provisioning_artifact_summaries

        out["provisioning_artifact_summaries"] = (
            aws_sdk_service_catalog.types.provisioning_artifact_summaries.deserialize_aws_json_1_1(
                data["ProvisioningArtifactSummaries"]
            )
        )
    if "Tags" in data:
        import aws_sdk_service_catalog.types.tags

        out["tags"] = aws_sdk_service_catalog.types.tags.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if "TagOptions" in data:
        import aws_sdk_service_catalog.types.tag_option_details

        out["tag_options"] = (
            aws_sdk_service_catalog.types.tag_option_details.deserialize_aws_json_1_1(
                data["TagOptions"]
            )
        )
    if "Budgets" in data:
        import aws_sdk_service_catalog.types.budgets

        out["budgets"] = aws_sdk_service_catalog.types.budgets.deserialize_aws_json_1_1(
            data["Budgets"]
        )
    return out
