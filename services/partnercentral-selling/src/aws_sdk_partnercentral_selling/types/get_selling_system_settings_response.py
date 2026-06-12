"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#GetSellingSystemSettingsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_partnercentral_selling.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_partnercentral_selling.types.catalog_identifier
    import aws_sdk_partnercentral_selling.types.resource_snapshot_job_role_arn


class GetSellingSystemSettingsResponse(TypedDict):
    catalog: "aws_sdk_partnercentral_selling.types.catalog_identifier.CatalogIdentifier"
    """<p>Specifies the catalog in which the settings are defined. Acceptable values include <code>AWS</code> for production and <code>Sandbox</code> for testing environments.</p>"""
    resource_snapshot_job_role_arn: NotRequired[
        "aws_sdk_partnercentral_selling.types.resource_snapshot_job_role_arn.ResourceSnapshotJobRoleArn"
    ]
    """<p>Specifies the ARN of the IAM Role used for resource snapshot job executions.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetSellingSystemSettingsResponse) -> dict:
    out: dict = {}
    out["Catalog"] = value["catalog"]
    if "resource_snapshot_job_role_arn" in value:
        out["ResourceSnapshotJobRoleArn"] = value["resource_snapshot_job_role_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetSellingSystemSettingsResponse:
    out: GetSellingSystemSettingsResponse = {}  # type: ignore[typeddict-item]
    if "Catalog" in data:
        out["catalog"] = data["Catalog"]
    else:
        raise DeserializationError("GetSellingSystemSettingsResponse.catalog required")
    if "ResourceSnapshotJobRoleArn" in data:
        out["resource_snapshot_job_role_arn"] = data["ResourceSnapshotJobRoleArn"]
    return out
