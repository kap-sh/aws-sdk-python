"""Generated from Smithy shape ``com.amazonaws.emr#UpdateStudioInput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_emr.types.subnet_id_list
    import aws_sdk_emr.types.xml_string
    import aws_sdk_emr.types.xml_string_max_len256


class UpdateStudioInput(TypedDict):
    studio_id: NotRequired["aws_sdk_emr.types.xml_string_max_len256.XmlStringMaxLen256"]
    """<p>The ID of the Amazon EMR Studio to update.</p>"""
    name: NotRequired["aws_sdk_emr.types.xml_string_max_len256.XmlStringMaxLen256"]
    """<p>A descriptive name for the Amazon EMR Studio.</p>"""
    description: NotRequired[
        "aws_sdk_emr.types.xml_string_max_len256.XmlStringMaxLen256"
    ]
    """<p>A detailed description to assign to the Amazon EMR Studio.</p>"""
    subnet_ids: NotRequired["aws_sdk_emr.types.subnet_id_list.SubnetIdList"]
    """<p>A list of subnet IDs to associate with the Amazon EMR Studio. The list can include new subnet IDs, but must also include all of the subnet IDs previously associated with the Studio. The list order does not matter. A Studio can have a maximum of 5 subnets. The subnets must belong to the same VPC as the Studio. </p>"""
    default_s3_location: NotRequired["aws_sdk_emr.types.xml_string.XmlString"]
    """<p>The Amazon S3 location to back up Workspaces and notebook files for the Amazon EMR Studio.</p>"""
    encryption_key_arn: NotRequired["aws_sdk_emr.types.xml_string.XmlString"]
    """<p>The KMS key identifier (ARN) used to encrypt Amazon EMR Studio workspace and notebook files when backed up to Amazon S3.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateStudioInput) -> dict:
    out: dict = {}
    if "studio_id" in value:
        out["StudioId"] = value["studio_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "subnet_ids" in value:
        import aws_sdk_emr.types.subnet_id_list

        out["SubnetIds"] = aws_sdk_emr.types.subnet_id_list.serialize_aws_json_1_1(
            value["subnet_ids"]
        )
    if "default_s3_location" in value:
        out["DefaultS3Location"] = value["default_s3_location"]
    if "encryption_key_arn" in value:
        out["EncryptionKeyArn"] = value["encryption_key_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateStudioInput:
    out: UpdateStudioInput = {}  # type: ignore[typeddict-item]
    if "StudioId" in data:
        out["studio_id"] = data["StudioId"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "SubnetIds" in data:
        import aws_sdk_emr.types.subnet_id_list

        out["subnet_ids"] = aws_sdk_emr.types.subnet_id_list.deserialize_aws_json_1_1(
            data["SubnetIds"]
        )
    if "DefaultS3Location" in data:
        out["default_s3_location"] = data["DefaultS3Location"]
    if "EncryptionKeyArn" in data:
        out["encryption_key_arn"] = data["EncryptionKeyArn"]
    return out
