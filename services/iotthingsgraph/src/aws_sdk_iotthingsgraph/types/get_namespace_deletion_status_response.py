"""Generated from Smithy shape ``com.amazonaws.iotthingsgraph#GetNamespaceDeletionStatusResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iotthingsgraph.types.arn
    import aws_sdk_iotthingsgraph.types.namespace_deletion_status
    import aws_sdk_iotthingsgraph.types.namespace_deletion_status_error_codes
    import aws_sdk_iotthingsgraph.types.namespace_name
    import aws_sdk_iotthingsgraph.types.string


class GetNamespaceDeletionStatusResponse(TypedDict):
    namespace_arn: NotRequired["aws_sdk_iotthingsgraph.types.arn.Arn"]
    """<p>The ARN of the namespace that is being deleted.</p>"""
    namespace_name: NotRequired[
        "aws_sdk_iotthingsgraph.types.namespace_name.NamespaceName"
    ]
    """<p>The name of the namespace that is being deleted.</p>"""
    status: NotRequired[
        "aws_sdk_iotthingsgraph.types.namespace_deletion_status.NamespaceDeletionStatus"
    ]
    """<p>The status of the deletion request.</p>"""
    error_code: NotRequired[
        "aws_sdk_iotthingsgraph.types.namespace_deletion_status_error_codes.NamespaceDeletionStatusErrorCodes"
    ]
    """<p>An error code returned by the namespace deletion task.</p>"""
    error_message: NotRequired["aws_sdk_iotthingsgraph.types.string.String"]
    """<p>An error code returned by the namespace deletion task.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetNamespaceDeletionStatusResponse) -> dict:
    out: dict = {}
    if "namespace_arn" in value:
        out["namespaceArn"] = value["namespace_arn"]
    if "namespace_name" in value:
        out["namespaceName"] = value["namespace_name"]
    if "status" in value:
        import aws_sdk_iotthingsgraph.types.namespace_deletion_status

        out["status"] = (
            aws_sdk_iotthingsgraph.types.namespace_deletion_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "error_code" in value:
        import aws_sdk_iotthingsgraph.types.namespace_deletion_status_error_codes

        out["errorCode"] = (
            aws_sdk_iotthingsgraph.types.namespace_deletion_status_error_codes.serialize_aws_json_1_1(
                value["error_code"]
            )
        )
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetNamespaceDeletionStatusResponse:
    out: GetNamespaceDeletionStatusResponse = {}  # type: ignore[typeddict-item]
    if "namespaceArn" in data:
        out["namespace_arn"] = data["namespaceArn"]
    if "namespaceName" in data:
        out["namespace_name"] = data["namespaceName"]
    if "status" in data:
        import aws_sdk_iotthingsgraph.types.namespace_deletion_status

        out["status"] = (
            aws_sdk_iotthingsgraph.types.namespace_deletion_status.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    if "errorCode" in data:
        import aws_sdk_iotthingsgraph.types.namespace_deletion_status_error_codes

        out["error_code"] = (
            aws_sdk_iotthingsgraph.types.namespace_deletion_status_error_codes.deserialize_aws_json_1_1(
                data["errorCode"]
            )
        )
    if "errorMessage" in data:
        out["error_message"] = data["errorMessage"]
    return out
