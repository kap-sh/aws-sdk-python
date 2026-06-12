"""Generated from Smithy shape ``com.amazonaws.servicediscovery#Operation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_servicediscovery.types.aws_account_id
    import aws_sdk_servicediscovery.types.code
    import aws_sdk_servicediscovery.types.message
    import aws_sdk_servicediscovery.types.operation_id
    import aws_sdk_servicediscovery.types.operation_status
    import aws_sdk_servicediscovery.types.operation_targets_map
    import aws_sdk_servicediscovery.types.operation_type
    import aws_sdk_servicediscovery.types.timestamp


class Operation(TypedDict):
    id: NotRequired["aws_sdk_servicediscovery.types.operation_id.OperationId"]
    """<p>The ID of the operation that you want to get information about.</p>"""
    owner_account: NotRequired[
        "aws_sdk_servicediscovery.types.aws_account_id.AWSAccountId"
    ]
    """<p>The ID of the Amazon Web Services account that owns the namespace associated with the operation.</p>"""
    type: NotRequired["aws_sdk_servicediscovery.types.operation_type.OperationType"]
    """<p>The name of the operation that's associated with the specified ID.</p>"""
    status: NotRequired[
        "aws_sdk_servicediscovery.types.operation_status.OperationStatus"
    ]
    """<p>The status of the operation. Values include the following:</p> <dl> <dt>SUBMITTED</dt> <dd> <p>This is the initial state that occurs immediately after you submit a request.</p> </dd> <dt>PENDING</dt> <dd> <p>Cloud Map is performing the operation.</p> </dd> <dt>SUCCESS</dt> <dd> <p>The operation succeeded.</p> </dd> <dt>FAIL</dt> <dd> <p>The operation failed. For the failure reason, see <code>ErrorMessage</code>.</p> </dd> </dl>"""
    error_message: NotRequired["aws_sdk_servicediscovery.types.message.Message"]
    """<p>If the value of <code>Status</code> is <code>FAIL</code>, the reason that the operation failed.</p>"""
    error_code: NotRequired["aws_sdk_servicediscovery.types.code.Code"]
    """<p>The code associated with <code>ErrorMessage</code>. Values for <code>ErrorCode</code> include the following:</p> <ul> <li> <p> <code>ACCESS_DENIED</code> </p> </li> <li> <p> <code>CANNOT_CREATE_HOSTED_ZONE</code> </p> </li> <li> <p> <code>EXPIRED_TOKEN</code> </p> </li> <li> <p> <code>HOSTED_ZONE_NOT_FOUND</code> </p> </li> <li> <p> <code>INTERNAL_FAILURE</code> </p> </li> <li> <p> <code>INVALID_CHANGE_BATCH</code> </p> </li> <li> <p> <code>THROTTLED_REQUEST</code> </p> </li> </ul>"""
    create_date: NotRequired["aws_sdk_servicediscovery.types.timestamp.Timestamp"]
    """<p>The date and time that the request was submitted, in Unix date/time format and Coordinated Universal Time (UTC). The value of <code>CreateDate</code> is accurate to milliseconds. For example, the value <code>1516925490.087</code> represents Friday, January 26, 2018 12:11:30.087 AM.</p>"""
    update_date: NotRequired["aws_sdk_servicediscovery.types.timestamp.Timestamp"]
    """<p>The date and time that the value of <code>Status</code> changed to the current value, in Unix date/time format and Coordinated Universal Time (UTC). The value of <code>UpdateDate</code> is accurate to milliseconds. For example, the value <code>1516925490.087</code> represents Friday, January 26, 2018 12:11:30.087 AM.</p>"""
    targets: NotRequired[
        "aws_sdk_servicediscovery.types.operation_targets_map.OperationTargetsMap"
    ]
    """<p>The name of the target entity that's associated with the operation:</p> <dl> <dt>NAMESPACE</dt> <dd> <p>The namespace ID is returned in the <code>ResourceId</code> property.</p> </dd> <dt>SERVICE</dt> <dd> <p>The service ID is returned in the <code>ResourceId</code> property.</p> </dd> <dt>INSTANCE</dt> <dd> <p>The instance ID is returned in the <code>ResourceId</code> property.</p> </dd> </dl>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Operation) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "owner_account" in value:
        out["OwnerAccount"] = value["owner_account"]
    if "type" in value:
        import aws_sdk_servicediscovery.types.operation_type

        out["Type"] = (
            aws_sdk_servicediscovery.types.operation_type.serialize_aws_json_1_1(
                value["type"]
            )
        )
    if "status" in value:
        import aws_sdk_servicediscovery.types.operation_status

        out["Status"] = (
            aws_sdk_servicediscovery.types.operation_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    if "error_code" in value:
        out["ErrorCode"] = value["error_code"]
    if "create_date" in value:
        import aws_sdk_servicediscovery.types.timestamp

        out["CreateDate"] = (
            aws_sdk_servicediscovery.types.timestamp.serialize_aws_json_1_1(
                value["create_date"]
            )
        )
    if "update_date" in value:
        import aws_sdk_servicediscovery.types.timestamp

        out["UpdateDate"] = (
            aws_sdk_servicediscovery.types.timestamp.serialize_aws_json_1_1(
                value["update_date"]
            )
        )
    if "targets" in value:
        import aws_sdk_servicediscovery.types.operation_targets_map

        out["Targets"] = (
            aws_sdk_servicediscovery.types.operation_targets_map.serialize_aws_json_1_1(
                value["targets"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Operation:
    out: Operation = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "OwnerAccount" in data:
        out["owner_account"] = data["OwnerAccount"]
    if "Type" in data:
        import aws_sdk_servicediscovery.types.operation_type

        out["type"] = (
            aws_sdk_servicediscovery.types.operation_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    if "Status" in data:
        import aws_sdk_servicediscovery.types.operation_status

        out["status"] = (
            aws_sdk_servicediscovery.types.operation_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "ErrorMessage" in data:
        out["error_message"] = data["ErrorMessage"]
    if "ErrorCode" in data:
        out["error_code"] = data["ErrorCode"]
    if "CreateDate" in data:
        import aws_sdk_servicediscovery.types.timestamp

        out["create_date"] = (
            aws_sdk_servicediscovery.types.timestamp.deserialize_aws_json_1_1(
                data["CreateDate"]
            )
        )
    if "UpdateDate" in data:
        import aws_sdk_servicediscovery.types.timestamp

        out["update_date"] = (
            aws_sdk_servicediscovery.types.timestamp.deserialize_aws_json_1_1(
                data["UpdateDate"]
            )
        )
    if "Targets" in data:
        import aws_sdk_servicediscovery.types.operation_targets_map

        out["targets"] = (
            aws_sdk_servicediscovery.types.operation_targets_map.deserialize_aws_json_1_1(
                data["Targets"]
            )
        )
    return out
