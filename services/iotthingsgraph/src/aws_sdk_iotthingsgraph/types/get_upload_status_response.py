"""Generated from Smithy shape ``com.amazonaws.iotthingsgraph#GetUploadStatusResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iotthingsgraph.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotthingsgraph.types.arn
    import aws_sdk_iotthingsgraph.types.namespace_name
    import aws_sdk_iotthingsgraph.types.string_list
    import aws_sdk_iotthingsgraph.types.timestamp
    import aws_sdk_iotthingsgraph.types.upload_id
    import aws_sdk_iotthingsgraph.types.upload_status
    import aws_sdk_iotthingsgraph.types.version


class GetUploadStatusResponse(TypedDict, closed=True):
    upload_id: "aws_sdk_iotthingsgraph.types.upload_id.UploadId"
    """<p>The ID of the upload.</p>"""
    upload_status: "aws_sdk_iotthingsgraph.types.upload_status.UploadStatus"
    """<p>The status of the upload. The initial status is <code>IN_PROGRESS</code>. The response show all validation failures if the upload fails.</p>"""
    namespace_arn: NotRequired["aws_sdk_iotthingsgraph.types.arn.Arn"]
    """<p>The ARN of the upload.</p>"""
    namespace_name: NotRequired[
        "aws_sdk_iotthingsgraph.types.namespace_name.NamespaceName"
    ]
    """<p>The name of the upload's namespace.</p>"""
    namespace_version: NotRequired["aws_sdk_iotthingsgraph.types.version.Version"]
    """<p>The version of the user's namespace. Defaults to the latest version of the user's namespace.</p>"""
    failure_reason: NotRequired["aws_sdk_iotthingsgraph.types.string_list.StringList"]
    """<p>The reason for an upload failure.</p>"""
    created_date: "aws_sdk_iotthingsgraph.types.timestamp.Timestamp"
    """<p>The date at which the upload was created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetUploadStatusResponse) -> dict:
    out: dict = {}
    out["uploadId"] = value["upload_id"]
    import aws_sdk_iotthingsgraph.types.upload_status

    out["uploadStatus"] = (
        aws_sdk_iotthingsgraph.types.upload_status.serialize_aws_json_1_1(
            value["upload_status"]
        )
    )
    if "namespace_arn" in value:
        out["namespaceArn"] = value["namespace_arn"]
    if "namespace_name" in value:
        out["namespaceName"] = value["namespace_name"]
    if "namespace_version" in value:
        out["namespaceVersion"] = value["namespace_version"]
    if "failure_reason" in value:
        import aws_sdk_iotthingsgraph.types.string_list

        out["failureReason"] = (
            aws_sdk_iotthingsgraph.types.string_list.serialize_aws_json_1_1(
                value["failure_reason"]
            )
        )
    import aws_sdk_iotthingsgraph.types.timestamp

    out["createdDate"] = aws_sdk_iotthingsgraph.types.timestamp.serialize_aws_json_1_1(
        value["created_date"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetUploadStatusResponse:
    out: GetUploadStatusResponse = {}  # type: ignore[typeddict-item]
    if "uploadId" in data:
        out["upload_id"] = data["uploadId"]
    else:
        raise DeserializationError("GetUploadStatusResponse.upload_id required")
    if "uploadStatus" in data:
        import aws_sdk_iotthingsgraph.types.upload_status

        out["upload_status"] = (
            aws_sdk_iotthingsgraph.types.upload_status.deserialize_aws_json_1_1(
                data["uploadStatus"]
            )
        )
    else:
        raise DeserializationError("GetUploadStatusResponse.upload_status required")
    if "namespaceArn" in data:
        out["namespace_arn"] = data["namespaceArn"]
    if "namespaceName" in data:
        out["namespace_name"] = data["namespaceName"]
    if "namespaceVersion" in data:
        out["namespace_version"] = data["namespaceVersion"]
    if "failureReason" in data:
        import aws_sdk_iotthingsgraph.types.string_list

        out["failure_reason"] = (
            aws_sdk_iotthingsgraph.types.string_list.deserialize_aws_json_1_1(
                data["failureReason"]
            )
        )
    if "createdDate" in data:
        import aws_sdk_iotthingsgraph.types.timestamp

        out["created_date"] = (
            aws_sdk_iotthingsgraph.types.timestamp.deserialize_aws_json_1_1(
                data["createdDate"]
            )
        )
    else:
        raise DeserializationError("GetUploadStatusResponse.created_date required")
    return out
