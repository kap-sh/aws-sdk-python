"""Generated from Smithy shape ``com.amazonaws.kendra#GroupOrderingIdSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kendra.types.failure_reason
    import aws_sdk_kendra.types.principal_mapping_status
    import aws_sdk_kendra.types.principal_ordering_id
    import aws_sdk_kendra.types.timestamp


class GroupOrderingIdSummary(TypedDict):
    status: NotRequired[
        "aws_sdk_kendra.types.principal_mapping_status.PrincipalMappingStatus"
    ]
    """<p>The current processing status of actions for mapping users to their groups. The status can be either <code>PROCESSING</code>, <code>SUCCEEDED</code>, <code>DELETING</code>, <code>DELETED</code>, or <code>FAILED</code>.</p>"""
    last_updated_at: NotRequired["aws_sdk_kendra.types.timestamp.Timestamp"]
    """<p>The Unix timestamp when an action was last updated. An action can be a <code>PUT</code> or <code>DELETE</code> action for mapping users to their groups.</p>"""
    received_at: NotRequired["aws_sdk_kendra.types.timestamp.Timestamp"]
    """<p>The Unix timestamp when an action was received by Amazon Kendra. An action can be a <code>PUT</code> or <code>DELETE</code> action for mapping users to their groups.</p>"""
    ordering_id: NotRequired[
        "aws_sdk_kendra.types.principal_ordering_id.PrincipalOrderingId"
    ]
    """<p>The order in which actions should complete processing. An action can be a <code>PUT</code> or <code>DELETE</code> action for mapping users to their groups.</p>"""
    failure_reason: NotRequired["aws_sdk_kendra.types.failure_reason.FailureReason"]
    """<p>The reason an action could not be processed. An action can be a <code>PUT</code> or <code>DELETE</code> action for mapping users to their groups.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GroupOrderingIdSummary) -> dict:
    out: dict = {}
    if "status" in value:
        import aws_sdk_kendra.types.principal_mapping_status

        out["Status"] = (
            aws_sdk_kendra.types.principal_mapping_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "last_updated_at" in value:
        import aws_sdk_kendra.types.timestamp

        out["LastUpdatedAt"] = aws_sdk_kendra.types.timestamp.serialize_aws_json_1_1(
            value["last_updated_at"]
        )
    if "received_at" in value:
        import aws_sdk_kendra.types.timestamp

        out["ReceivedAt"] = aws_sdk_kendra.types.timestamp.serialize_aws_json_1_1(
            value["received_at"]
        )
    if "ordering_id" in value:
        out["OrderingId"] = value["ordering_id"]
    if "failure_reason" in value:
        out["FailureReason"] = value["failure_reason"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GroupOrderingIdSummary:
    out: GroupOrderingIdSummary = {}  # type: ignore[typeddict-item]
    if "Status" in data:
        import aws_sdk_kendra.types.principal_mapping_status

        out["status"] = (
            aws_sdk_kendra.types.principal_mapping_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "LastUpdatedAt" in data:
        import aws_sdk_kendra.types.timestamp

        out["last_updated_at"] = (
            aws_sdk_kendra.types.timestamp.deserialize_aws_json_1_1(
                data["LastUpdatedAt"]
            )
        )
    if "ReceivedAt" in data:
        import aws_sdk_kendra.types.timestamp

        out["received_at"] = aws_sdk_kendra.types.timestamp.deserialize_aws_json_1_1(
            data["ReceivedAt"]
        )
    if "OrderingId" in data:
        out["ordering_id"] = data["OrderingId"]
    if "FailureReason" in data:
        out["failure_reason"] = data["FailureReason"]
    return out
