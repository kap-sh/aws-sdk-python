"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ListProvisioningArtifactsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.page_token
    import aws_sdk_service_catalog.types.provisioning_artifact_details


class ListProvisioningArtifactsOutput(TypedDict):
    provisioning_artifact_details: NotRequired[
        "aws_sdk_service_catalog.types.provisioning_artifact_details.ProvisioningArtifactDetails"
    ]
    """<p>Information about the provisioning artifacts.</p>"""
    next_page_token: NotRequired["aws_sdk_service_catalog.types.page_token.PageToken"]
    """<p>The page token to use to retrieve the next set of results. If there are no additional results, this value is null.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListProvisioningArtifactsOutput) -> dict:
    out: dict = {}
    if "provisioning_artifact_details" in value:
        import aws_sdk_service_catalog.types.provisioning_artifact_details

        out["ProvisioningArtifactDetails"] = (
            aws_sdk_service_catalog.types.provisioning_artifact_details.serialize_aws_json_1_1(
                value["provisioning_artifact_details"]
            )
        )
    if "next_page_token" in value:
        out["NextPageToken"] = value["next_page_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListProvisioningArtifactsOutput:
    out: ListProvisioningArtifactsOutput = {}  # type: ignore[typeddict-item]
    if "ProvisioningArtifactDetails" in data:
        import aws_sdk_service_catalog.types.provisioning_artifact_details

        out["provisioning_artifact_details"] = (
            aws_sdk_service_catalog.types.provisioning_artifact_details.deserialize_aws_json_1_1(
                data["ProvisioningArtifactDetails"]
            )
        )
    if "NextPageToken" in data:
        out["next_page_token"] = data["NextPageToken"]
    return out
