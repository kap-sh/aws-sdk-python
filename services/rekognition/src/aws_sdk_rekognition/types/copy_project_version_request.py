"""Generated from Smithy shape ``com.amazonaws.rekognition#CopyProjectVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_rekognition.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.kms_key_id
    import aws_sdk_rekognition.types.output_config
    import aws_sdk_rekognition.types.project_arn
    import aws_sdk_rekognition.types.project_version_arn
    import aws_sdk_rekognition.types.tag_map
    import aws_sdk_rekognition.types.version_name


class CopyProjectVersionRequest(TypedDict, closed=True):
    source_project_arn: "aws_sdk_rekognition.types.project_arn.ProjectArn"
    """<p>The ARN of the source project in the trusting AWS account.</p>"""
    source_project_version_arn: (
        "aws_sdk_rekognition.types.project_version_arn.ProjectVersionArn"
    )
    """<p>The ARN of the model version in the source project that you want to copy to a destination project.</p>"""
    destination_project_arn: "aws_sdk_rekognition.types.project_arn.ProjectArn"
    """<p>The ARN of the project in the trusted AWS account that you want to copy the model version to. </p>"""
    version_name: "aws_sdk_rekognition.types.version_name.VersionName"
    """<p>A name for the version of the model that's copied to the destination project.</p>"""
    output_config: "aws_sdk_rekognition.types.output_config.OutputConfig"
    """<p>The S3 bucket and folder location where the training output for the source model version is placed.</p>"""
    tags: NotRequired["aws_sdk_rekognition.types.tag_map.TagMap"]
    """<p>The key-value tags to assign to the model version. </p>"""
    kms_key_id: NotRequired["aws_sdk_rekognition.types.kms_key_id.KmsKeyId"]
    """<p>The identifier for your AWS Key Management Service key (AWS KMS key). You can supply the Amazon Resource Name (ARN) of your KMS key, the ID of your KMS key, an alias for your KMS key, or an alias ARN. The key is used to encrypt training results and manifest files written to the output Amazon S3 bucket (<code>OutputConfig</code>).</p> <p>If you choose to use your own KMS key, you need the following permissions on the KMS key.</p> <ul> <li> <p>kms:CreateGrant</p> </li> <li> <p>kms:DescribeKey</p> </li> <li> <p>kms:GenerateDataKey</p> </li> <li> <p>kms:Decrypt</p> </li> </ul> <p>If you don't specify a value for <code>KmsKeyId</code>, images copied into the service are encrypted using a key that AWS owns and manages.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CopyProjectVersionRequest) -> dict:
    out: dict = {}
    out["SourceProjectArn"] = value["source_project_arn"]
    out["SourceProjectVersionArn"] = value["source_project_version_arn"]
    out["DestinationProjectArn"] = value["destination_project_arn"]
    out["VersionName"] = value["version_name"]
    import aws_sdk_rekognition.types.output_config

    out["OutputConfig"] = (
        aws_sdk_rekognition.types.output_config.serialize_aws_json_1_1(
            value["output_config"]
        )
    )
    if "tags" in value:
        import aws_sdk_rekognition.types.tag_map

        out["Tags"] = aws_sdk_rekognition.types.tag_map.serialize_aws_json_1_1(
            value["tags"]
        )
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CopyProjectVersionRequest:
    out: CopyProjectVersionRequest = {}  # type: ignore[typeddict-item]
    if "SourceProjectArn" in data:
        out["source_project_arn"] = data["SourceProjectArn"]
    else:
        raise DeserializationError(
            "CopyProjectVersionRequest.source_project_arn required"
        )
    if "SourceProjectVersionArn" in data:
        out["source_project_version_arn"] = data["SourceProjectVersionArn"]
    else:
        raise DeserializationError(
            "CopyProjectVersionRequest.source_project_version_arn required"
        )
    if "DestinationProjectArn" in data:
        out["destination_project_arn"] = data["DestinationProjectArn"]
    else:
        raise DeserializationError(
            "CopyProjectVersionRequest.destination_project_arn required"
        )
    if "VersionName" in data:
        out["version_name"] = data["VersionName"]
    else:
        raise DeserializationError("CopyProjectVersionRequest.version_name required")
    if "OutputConfig" in data:
        import aws_sdk_rekognition.types.output_config

        out["output_config"] = (
            aws_sdk_rekognition.types.output_config.deserialize_aws_json_1_1(
                data["OutputConfig"]
            )
        )
    else:
        raise DeserializationError("CopyProjectVersionRequest.output_config required")
    if "Tags" in data:
        import aws_sdk_rekognition.types.tag_map

        out["tags"] = aws_sdk_rekognition.types.tag_map.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if "KmsKeyId" in data:
        out["kms_key_id"] = data["KmsKeyId"]
    return out
