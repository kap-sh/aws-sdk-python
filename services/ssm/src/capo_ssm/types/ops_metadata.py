"""Generated from Smithy shape ``com.amazonaws.ssm#OpsMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.date_time
    import capo_ssm.types.ops_metadata_arn
    import capo_ssm.types.ops_metadata_resource_id
    import capo_ssm.types.string


class OpsMetadata(TypedDict, closed=True):
    resource_id: NotRequired[
        "capo_ssm.types.ops_metadata_resource_id.OpsMetadataResourceId"
    ]
    """<p>The ID of the Application Manager application.</p>"""
    ops_metadata_arn: NotRequired["capo_ssm.types.ops_metadata_arn.OpsMetadataArn"]
    """<p>The Amazon Resource Name (ARN) of the OpsMetadata Object or blob.</p>"""
    last_modified_date: NotRequired["capo_ssm.types.date_time.DateTime"]
    """<p>The date the OpsMetadata object was last updated.</p>"""
    last_modified_user: NotRequired["capo_ssm.types.string.String"]
    """<p>The user name who last updated the OpsMetadata object.</p>"""
    creation_date: NotRequired["capo_ssm.types.date_time.DateTime"]
    """<p>The date the OpsMetadata objects was created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OpsMetadata) -> dict:
    out: dict = {}
    if "resource_id" in value:
        out["ResourceId"] = value["resource_id"]
    if "ops_metadata_arn" in value:
        out["OpsMetadataArn"] = value["ops_metadata_arn"]
    if "last_modified_date" in value:
        import capo_ssm.types.date_time

        out["LastModifiedDate"] = capo_ssm.types.date_time.serialize_aws_json_1_1(
            value["last_modified_date"]
        )
    if "last_modified_user" in value:
        out["LastModifiedUser"] = value["last_modified_user"]
    if "creation_date" in value:
        import capo_ssm.types.date_time

        out["CreationDate"] = capo_ssm.types.date_time.serialize_aws_json_1_1(
            value["creation_date"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> OpsMetadata:
    out: OpsMetadata = {}  # type: ignore[typeddict-item]
    if data.get("ResourceId") is not None:
        out["resource_id"] = data["ResourceId"]
    if data.get("OpsMetadataArn") is not None:
        out["ops_metadata_arn"] = data["OpsMetadataArn"]
    if data.get("LastModifiedDate") is not None:
        import capo_ssm.types.date_time

        out["last_modified_date"] = capo_ssm.types.date_time.deserialize_aws_json_1_1(
            data["LastModifiedDate"]
        )
    if data.get("LastModifiedUser") is not None:
        out["last_modified_user"] = data["LastModifiedUser"]
    if data.get("CreationDate") is not None:
        import capo_ssm.types.date_time

        out["creation_date"] = capo_ssm.types.date_time.deserialize_aws_json_1_1(
            data["CreationDate"]
        )
    return out
