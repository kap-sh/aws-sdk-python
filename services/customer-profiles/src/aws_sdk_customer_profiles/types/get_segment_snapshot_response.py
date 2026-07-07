"""Generated from Smithy shape ``com.amazonaws.customerprofiles#GetSegmentSnapshotResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_customer_profiles.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.data_format
    import aws_sdk_customer_profiles.types.encryption_key
    import aws_sdk_customer_profiles.types.role_arn
    import aws_sdk_customer_profiles.types.segment_snapshot_status
    import aws_sdk_customer_profiles.types.string1_to255
    import aws_sdk_customer_profiles.types.string1_to1000
    import aws_sdk_customer_profiles.types.uuid


class GetSegmentSnapshotResponse(TypedDict, closed=True):
    snapshot_id: "aws_sdk_customer_profiles.types.uuid.uuid"
    """<p>The unique identifier of the segment snapshot.</p>"""
    status: (
        "aws_sdk_customer_profiles.types.segment_snapshot_status.SegmentSnapshotStatus"
    )
    """<p>The status of the asynchronous job for exporting the segment snapshot.</p>"""
    status_message: NotRequired[
        "aws_sdk_customer_profiles.types.string1_to1000.string1To1000"
    ]
    """<p>The status message of the asynchronous job for exporting the segment snapshot.</p>"""
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
def serialize_json(value: GetSegmentSnapshotResponse) -> dict:
    out: dict = {}
    out["SnapshotId"] = value["snapshot_id"]
    import aws_sdk_customer_profiles.types.segment_snapshot_status

    out["Status"] = (
        aws_sdk_customer_profiles.types.segment_snapshot_status.serialize_json(
            value["status"]
        )
    )
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
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


def deserialize_json(data: dict) -> GetSegmentSnapshotResponse:
    out: GetSegmentSnapshotResponse = {}  # type: ignore[typeddict-item]
    if "SnapshotId" in data:
        out["snapshot_id"] = data["SnapshotId"]
    else:
        raise DeserializationError("GetSegmentSnapshotResponse.snapshot_id required")
    if "Status" in data:
        import aws_sdk_customer_profiles.types.segment_snapshot_status

        out["status"] = (
            aws_sdk_customer_profiles.types.segment_snapshot_status.deserialize_json(
                data["Status"]
            )
        )
    else:
        raise DeserializationError("GetSegmentSnapshotResponse.status required")
    if "StatusMessage" in data:
        out["status_message"] = data["StatusMessage"]
    if "DataFormat" in data:
        import aws_sdk_customer_profiles.types.data_format

        out["data_format"] = (
            aws_sdk_customer_profiles.types.data_format.deserialize_json(
                data["DataFormat"]
            )
        )
    else:
        raise DeserializationError("GetSegmentSnapshotResponse.data_format required")
    if "EncryptionKey" in data:
        out["encryption_key"] = data["EncryptionKey"]
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    if "DestinationUri" in data:
        out["destination_uri"] = data["DestinationUri"]
    return out
