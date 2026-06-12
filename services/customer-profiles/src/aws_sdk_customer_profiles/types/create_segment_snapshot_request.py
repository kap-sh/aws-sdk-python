"""Generated from Smithy shape ``com.amazonaws.customerprofiles#CreateSegmentSnapshotRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_customer_profiles.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.data_format
    import aws_sdk_customer_profiles.types.encryption_key
    import aws_sdk_customer_profiles.types.name
    import aws_sdk_customer_profiles.types.role_arn
    import aws_sdk_customer_profiles.types.string1_to255


class CreateSegmentSnapshotRequest(TypedDict):
    domain_name: "aws_sdk_customer_profiles.types.name.name"
    """<p>The unique name of the domain.</p>"""
    segment_definition_name: "aws_sdk_customer_profiles.types.name.name"
    """<p>The name of the segment definition used in this snapshot request.</p>"""
    data_format: "aws_sdk_customer_profiles.types.data_format.DataFormat"
    """<p>The format in which the segment will be exported.</p>"""
    encryption_key: NotRequired[
        "aws_sdk_customer_profiles.types.encryption_key.encryptionKey"
    ]
    """<p>The Amazon Resource Name (ARN) of the KMS key used to encrypt the exported segment.</p>"""
    role_arn: NotRequired["aws_sdk_customer_profiles.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of the IAM role that allows Customer Profiles service principal to assume the role for conducting KMS and S3 operations.</p>"""
    destination_uri: NotRequired[
        "aws_sdk_customer_profiles.types.string1_to255.string1To255"
    ]
    """<p>The destination to which the segment will be exported. This field must be provided if the request is not submitted from the Connect Customer Admin Website.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSegmentSnapshotRequest) -> dict:
    out: dict = {}
    import aws_sdk_customer_profiles.types.data_format

    out["DataFormat"] = aws_sdk_customer_profiles.types.data_format.serialize_json(
        value["data_format"]
    )
    if "encryption_key" in value:
        out["EncryptionKey"] = value["encryption_key"]
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "destination_uri" in value:
        out["DestinationUri"] = value["destination_uri"]
    return out


def deserialize_json(data: dict) -> CreateSegmentSnapshotRequest:
    out: CreateSegmentSnapshotRequest = {}  # type: ignore[typeddict-item]
    if "DataFormat" in data:
        import aws_sdk_customer_profiles.types.data_format

        out["data_format"] = (
            aws_sdk_customer_profiles.types.data_format.deserialize_json(
                data["DataFormat"]
            )
        )
    else:
        raise DeserializationError("CreateSegmentSnapshotRequest.data_format required")
    if "EncryptionKey" in data:
        out["encryption_key"] = data["EncryptionKey"]
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    if "DestinationUri" in data:
        out["destination_uri"] = data["DestinationUri"]
    return out
