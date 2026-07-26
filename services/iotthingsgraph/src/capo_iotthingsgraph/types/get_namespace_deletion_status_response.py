"""Generated from Smithy shape ``com.amazonaws.iotthingsgraph#GetNamespaceDeletionStatusResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotthingsgraph.types.arn
    import capo_iotthingsgraph.types.namespace_deletion_status
    import capo_iotthingsgraph.types.namespace_deletion_status_error_codes
    import capo_iotthingsgraph.types.namespace_name
    import capo_iotthingsgraph.types.string


class GetNamespaceDeletionStatusResponse(TypedDict, closed=True):
    namespace_arn: NotRequired["capo_iotthingsgraph.types.arn.Arn"]
    """<p>The ARN of the namespace that is being deleted.</p>"""
    namespace_name: NotRequired[
        "capo_iotthingsgraph.types.namespace_name.NamespaceName"
    ]
    """<p>The name of the namespace that is being deleted.</p>"""
    status: NotRequired[
        "capo_iotthingsgraph.types.namespace_deletion_status.NamespaceDeletionStatus"
    ]
    """<p>The status of the deletion request.</p>"""
    error_code: NotRequired[
        "capo_iotthingsgraph.types.namespace_deletion_status_error_codes.NamespaceDeletionStatusErrorCodes"
    ]
    """<p>An error code returned by the namespace deletion task.</p>"""
    error_message: NotRequired["capo_iotthingsgraph.types.string.String"]
    """<p>An error code returned by the namespace deletion task.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetNamespaceDeletionStatusResponse) -> dict:
    out: dict = {}
    if "namespace_arn" in value:
        out["namespaceArn"] = value["namespace_arn"]
    if "namespace_name" in value:
        out["namespaceName"] = value["namespace_name"]
    if "status" in value:
        import capo_iotthingsgraph.types.namespace_deletion_status

        out["status"] = (
            capo_iotthingsgraph.types.namespace_deletion_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "error_code" in value:
        import capo_iotthingsgraph.types.namespace_deletion_status_error_codes

        out["errorCode"] = (
            capo_iotthingsgraph.types.namespace_deletion_status_error_codes.serialize_aws_json_1_1(
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
        import capo_iotthingsgraph.types.namespace_deletion_status

        out["status"] = (
            capo_iotthingsgraph.types.namespace_deletion_status.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    if "errorCode" in data:
        import capo_iotthingsgraph.types.namespace_deletion_status_error_codes

        out["error_code"] = (
            capo_iotthingsgraph.types.namespace_deletion_status_error_codes.deserialize_aws_json_1_1(
                data["errorCode"]
            )
        )
    if "errorMessage" in data:
        out["error_message"] = data["errorMessage"]
    return out
