"""Generated from Smithy shape ``com.amazonaws.cloudformation#OperationEvent``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudformation.types.beacon_stack_operation_status
    import aws_sdk_cloudformation.types.client_request_token
    import aws_sdk_cloudformation.types.detailed_status
    import aws_sdk_cloudformation.types.event_id
    import aws_sdk_cloudformation.types.event_type
    import aws_sdk_cloudformation.types.hook_failure_mode
    import aws_sdk_cloudformation.types.hook_invocation_point
    import aws_sdk_cloudformation.types.hook_status
    import aws_sdk_cloudformation.types.hook_status_reason
    import aws_sdk_cloudformation.types.hook_type
    import aws_sdk_cloudformation.types.logical_resource_id
    import aws_sdk_cloudformation.types.operation_id
    import aws_sdk_cloudformation.types.operation_type
    import aws_sdk_cloudformation.types.physical_resource_id
    import aws_sdk_cloudformation.types.resource_properties
    import aws_sdk_cloudformation.types.resource_status
    import aws_sdk_cloudformation.types.resource_status_reason
    import aws_sdk_cloudformation.types.resource_type
    import aws_sdk_cloudformation.types.stack_id
    import aws_sdk_cloudformation.types.timestamp
    import aws_sdk_cloudformation.types.validation_name
    import aws_sdk_cloudformation.types.validation_path
    import aws_sdk_cloudformation.types.validation_status
    import aws_sdk_cloudformation.types.validation_status_reason


class OperationEvent(TypedDict):
    event_id: NotRequired["aws_sdk_cloudformation.types.event_id.EventId"]
    """<p>A unique identifier for this event.</p>"""
    stack_id: NotRequired["aws_sdk_cloudformation.types.stack_id.StackId"]
    """<p>The unique ID name of the instance of the stack.</p>"""
    operation_id: NotRequired["aws_sdk_cloudformation.types.operation_id.OperationId"]
    """<p>The unique identifier of the operation this event belongs to.</p>"""
    operation_type: NotRequired[
        "aws_sdk_cloudformation.types.operation_type.OperationType"
    ]
    """<p>The type of operation.</p>"""
    operation_status: NotRequired[
        "aws_sdk_cloudformation.types.beacon_stack_operation_status.BeaconStackOperationStatus"
    ]
    """<p>The current status of the operation.</p>"""
    event_type: NotRequired["aws_sdk_cloudformation.types.event_type.EventType"]
    """<p>The type of event.</p>"""
    logical_resource_id: NotRequired[
        "aws_sdk_cloudformation.types.logical_resource_id.LogicalResourceId"
    ]
    """<p>The logical name of the resource as specified in the template.</p>"""
    physical_resource_id: NotRequired[
        "aws_sdk_cloudformation.types.physical_resource_id.PhysicalResourceId"
    ]
    """<p>The name or unique identifier that corresponds to a physical instance ID of a resource.</p>"""
    resource_type: NotRequired[
        "aws_sdk_cloudformation.types.resource_type.ResourceType"
    ]
    """<p>Type of resource.</p>"""
    timestamp: NotRequired["aws_sdk_cloudformation.types.timestamp.Timestamp"]
    """<p>Time the status was updated.</p>"""
    start_time: NotRequired["aws_sdk_cloudformation.types.timestamp.Timestamp"]
    """<p>The time when the event started.</p>"""
    end_time: NotRequired["aws_sdk_cloudformation.types.timestamp.Timestamp"]
    """<p>The time when the event ended.</p>"""
    resource_status: NotRequired[
        "aws_sdk_cloudformation.types.resource_status.ResourceStatus"
    ]
    """<p>Current status of the resource.</p>"""
    resource_status_reason: NotRequired[
        "aws_sdk_cloudformation.types.resource_status_reason.ResourceStatusReason"
    ]
    """<p>Success or failure message associated with the resource.</p>"""
    resource_properties: NotRequired[
        "aws_sdk_cloudformation.types.resource_properties.ResourceProperties"
    ]
    """<p>The properties used to create the resource.</p>"""
    client_request_token: NotRequired[
        "aws_sdk_cloudformation.types.client_request_token.ClientRequestToken"
    ]
    """<p>A unique identifier for the request that initiated this operation.</p>"""
    hook_type: NotRequired["aws_sdk_cloudformation.types.hook_type.HookType"]
    """<p>The type name of the Hook that was invoked.</p>"""
    hook_status: NotRequired["aws_sdk_cloudformation.types.hook_status.HookStatus"]
    """<p>The status of the Hook invocation. </p>"""
    hook_status_reason: NotRequired[
        "aws_sdk_cloudformation.types.hook_status_reason.HookStatusReason"
    ]
    """<p>Additional information about the Hook status.</p>"""
    hook_invocation_point: NotRequired[
        "aws_sdk_cloudformation.types.hook_invocation_point.HookInvocationPoint"
    ]
    """<p>The point in the operation lifecycle when the Hook was invoked.</p>"""
    hook_failure_mode: NotRequired[
        "aws_sdk_cloudformation.types.hook_failure_mode.HookFailureMode"
    ]
    """<p>Specifies how Hook failures are handled.</p>"""
    detailed_status: NotRequired[
        "aws_sdk_cloudformation.types.detailed_status.DetailedStatus"
    ]
    """<p>Additional status information about the operation.</p>"""
    validation_failure_mode: NotRequired[
        "aws_sdk_cloudformation.types.hook_failure_mode.HookFailureMode"
    ]
    """<p>Specifies how validation failures are handled.</p>"""
    validation_name: NotRequired[
        "aws_sdk_cloudformation.types.validation_name.ValidationName"
    ]
    """<p>The name of the validation that was performed.</p>"""
    validation_status: NotRequired[
        "aws_sdk_cloudformation.types.validation_status.ValidationStatus"
    ]
    """<p>The status of the validation.</p>"""
    validation_status_reason: NotRequired[
        "aws_sdk_cloudformation.types.validation_status_reason.ValidationStatusReason"
    ]
    """<p>Additional information about the validation status.</p>"""
    validation_path: NotRequired[
        "aws_sdk_cloudformation.types.validation_path.ValidationPath"
    ]
    """<p>The path within the resource where the validation was applied.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: OperationEvent, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "event_id" in value:
        pairs.append((f"{prefix}.EventId", str(value["event_id"])))
    if "stack_id" in value:
        pairs.append((f"{prefix}.StackId", str(value["stack_id"])))
    if "operation_id" in value:
        pairs.append((f"{prefix}.OperationId", str(value["operation_id"])))
    if "operation_type" in value:
        import aws_sdk_cloudformation.types.operation_type

        aws_sdk_cloudformation.types.operation_type.serialize_query(
            value["operation_type"], pairs, f"{prefix}.OperationType"
        )
    if "operation_status" in value:
        import aws_sdk_cloudformation.types.beacon_stack_operation_status

        aws_sdk_cloudformation.types.beacon_stack_operation_status.serialize_query(
            value["operation_status"], pairs, f"{prefix}.OperationStatus"
        )
    if "event_type" in value:
        import aws_sdk_cloudformation.types.event_type

        aws_sdk_cloudformation.types.event_type.serialize_query(
            value["event_type"], pairs, f"{prefix}.EventType"
        )
    if "logical_resource_id" in value:
        pairs.append((f"{prefix}.LogicalResourceId", str(value["logical_resource_id"])))
    if "physical_resource_id" in value:
        pairs.append(
            (f"{prefix}.PhysicalResourceId", str(value["physical_resource_id"]))
        )
    if "resource_type" in value:
        pairs.append((f"{prefix}.ResourceType", str(value["resource_type"])))
    if "timestamp" in value:
        import aws_sdk_cloudformation.types.timestamp

        aws_sdk_cloudformation.types.timestamp.serialize_query(
            value["timestamp"], pairs, f"{prefix}.Timestamp"
        )
    if "start_time" in value:
        import aws_sdk_cloudformation.types.timestamp

        aws_sdk_cloudformation.types.timestamp.serialize_query(
            value["start_time"], pairs, f"{prefix}.StartTime"
        )
    if "end_time" in value:
        import aws_sdk_cloudformation.types.timestamp

        aws_sdk_cloudformation.types.timestamp.serialize_query(
            value["end_time"], pairs, f"{prefix}.EndTime"
        )
    if "resource_status" in value:
        import aws_sdk_cloudformation.types.resource_status

        aws_sdk_cloudformation.types.resource_status.serialize_query(
            value["resource_status"], pairs, f"{prefix}.ResourceStatus"
        )
    if "resource_status_reason" in value:
        pairs.append(
            (f"{prefix}.ResourceStatusReason", str(value["resource_status_reason"]))
        )
    if "resource_properties" in value:
        pairs.append(
            (f"{prefix}.ResourceProperties", str(value["resource_properties"]))
        )
    if "client_request_token" in value:
        pairs.append(
            (f"{prefix}.ClientRequestToken", str(value["client_request_token"]))
        )
    if "hook_type" in value:
        pairs.append((f"{prefix}.HookType", str(value["hook_type"])))
    if "hook_status" in value:
        import aws_sdk_cloudformation.types.hook_status

        aws_sdk_cloudformation.types.hook_status.serialize_query(
            value["hook_status"], pairs, f"{prefix}.HookStatus"
        )
    if "hook_status_reason" in value:
        pairs.append((f"{prefix}.HookStatusReason", str(value["hook_status_reason"])))
    if "hook_invocation_point" in value:
        import aws_sdk_cloudformation.types.hook_invocation_point

        aws_sdk_cloudformation.types.hook_invocation_point.serialize_query(
            value["hook_invocation_point"], pairs, f"{prefix}.HookInvocationPoint"
        )
    if "hook_failure_mode" in value:
        import aws_sdk_cloudformation.types.hook_failure_mode

        aws_sdk_cloudformation.types.hook_failure_mode.serialize_query(
            value["hook_failure_mode"], pairs, f"{prefix}.HookFailureMode"
        )
    if "detailed_status" in value:
        import aws_sdk_cloudformation.types.detailed_status

        aws_sdk_cloudformation.types.detailed_status.serialize_query(
            value["detailed_status"], pairs, f"{prefix}.DetailedStatus"
        )
    if "validation_failure_mode" in value:
        import aws_sdk_cloudformation.types.hook_failure_mode

        aws_sdk_cloudformation.types.hook_failure_mode.serialize_query(
            value["validation_failure_mode"], pairs, f"{prefix}.ValidationFailureMode"
        )
    if "validation_name" in value:
        pairs.append((f"{prefix}.ValidationName", str(value["validation_name"])))
    if "validation_status" in value:
        import aws_sdk_cloudformation.types.validation_status

        aws_sdk_cloudformation.types.validation_status.serialize_query(
            value["validation_status"], pairs, f"{prefix}.ValidationStatus"
        )
    if "validation_status_reason" in value:
        pairs.append(
            (f"{prefix}.ValidationStatusReason", str(value["validation_status_reason"]))
        )
    if "validation_path" in value:
        pairs.append((f"{prefix}.ValidationPath", str(value["validation_path"])))


def deserialize_query(el: Element) -> OperationEvent:
    out: OperationEvent = {}  # type: ignore[typeddict-item]
    child_event_id = el.find("EventId")
    if child_event_id is not None:
        out["event_id"] = str(child_event_id.text or "")
    child_stack_id = el.find("StackId")
    if child_stack_id is not None:
        out["stack_id"] = str(child_stack_id.text or "")
    child_operation_id = el.find("OperationId")
    if child_operation_id is not None:
        out["operation_id"] = str(child_operation_id.text or "")
    child_operation_type = el.find("OperationType")
    if child_operation_type is not None:
        import aws_sdk_cloudformation.types.operation_type

        out["operation_type"] = (
            aws_sdk_cloudformation.types.operation_type.deserialize_query(
                child_operation_type
            )
        )
    child_operation_status = el.find("OperationStatus")
    if child_operation_status is not None:
        import aws_sdk_cloudformation.types.beacon_stack_operation_status

        out["operation_status"] = (
            aws_sdk_cloudformation.types.beacon_stack_operation_status.deserialize_query(
                child_operation_status
            )
        )
    child_event_type = el.find("EventType")
    if child_event_type is not None:
        import aws_sdk_cloudformation.types.event_type

        out["event_type"] = aws_sdk_cloudformation.types.event_type.deserialize_query(
            child_event_type
        )
    child_logical_resource_id = el.find("LogicalResourceId")
    if child_logical_resource_id is not None:
        out["logical_resource_id"] = str(child_logical_resource_id.text or "")
    child_physical_resource_id = el.find("PhysicalResourceId")
    if child_physical_resource_id is not None:
        out["physical_resource_id"] = str(child_physical_resource_id.text or "")
    child_resource_type = el.find("ResourceType")
    if child_resource_type is not None:
        out["resource_type"] = str(child_resource_type.text or "")
    child_timestamp = el.find("Timestamp")
    if child_timestamp is not None:
        import aws_sdk_cloudformation.types.timestamp

        out["timestamp"] = aws_sdk_cloudformation.types.timestamp.deserialize_query(
            child_timestamp
        )
    child_start_time = el.find("StartTime")
    if child_start_time is not None:
        import aws_sdk_cloudformation.types.timestamp

        out["start_time"] = aws_sdk_cloudformation.types.timestamp.deserialize_query(
            child_start_time
        )
    child_end_time = el.find("EndTime")
    if child_end_time is not None:
        import aws_sdk_cloudformation.types.timestamp

        out["end_time"] = aws_sdk_cloudformation.types.timestamp.deserialize_query(
            child_end_time
        )
    child_resource_status = el.find("ResourceStatus")
    if child_resource_status is not None:
        import aws_sdk_cloudformation.types.resource_status

        out["resource_status"] = (
            aws_sdk_cloudformation.types.resource_status.deserialize_query(
                child_resource_status
            )
        )
    child_resource_status_reason = el.find("ResourceStatusReason")
    if child_resource_status_reason is not None:
        out["resource_status_reason"] = str(child_resource_status_reason.text or "")
    child_resource_properties = el.find("ResourceProperties")
    if child_resource_properties is not None:
        out["resource_properties"] = str(child_resource_properties.text or "")
    child_client_request_token = el.find("ClientRequestToken")
    if child_client_request_token is not None:
        out["client_request_token"] = str(child_client_request_token.text or "")
    child_hook_type = el.find("HookType")
    if child_hook_type is not None:
        out["hook_type"] = str(child_hook_type.text or "")
    child_hook_status = el.find("HookStatus")
    if child_hook_status is not None:
        import aws_sdk_cloudformation.types.hook_status

        out["hook_status"] = aws_sdk_cloudformation.types.hook_status.deserialize_query(
            child_hook_status
        )
    child_hook_status_reason = el.find("HookStatusReason")
    if child_hook_status_reason is not None:
        out["hook_status_reason"] = str(child_hook_status_reason.text or "")
    child_hook_invocation_point = el.find("HookInvocationPoint")
    if child_hook_invocation_point is not None:
        import aws_sdk_cloudformation.types.hook_invocation_point

        out["hook_invocation_point"] = (
            aws_sdk_cloudformation.types.hook_invocation_point.deserialize_query(
                child_hook_invocation_point
            )
        )
    child_hook_failure_mode = el.find("HookFailureMode")
    if child_hook_failure_mode is not None:
        import aws_sdk_cloudformation.types.hook_failure_mode

        out["hook_failure_mode"] = (
            aws_sdk_cloudformation.types.hook_failure_mode.deserialize_query(
                child_hook_failure_mode
            )
        )
    child_detailed_status = el.find("DetailedStatus")
    if child_detailed_status is not None:
        import aws_sdk_cloudformation.types.detailed_status

        out["detailed_status"] = (
            aws_sdk_cloudformation.types.detailed_status.deserialize_query(
                child_detailed_status
            )
        )
    child_validation_failure_mode = el.find("ValidationFailureMode")
    if child_validation_failure_mode is not None:
        import aws_sdk_cloudformation.types.hook_failure_mode

        out["validation_failure_mode"] = (
            aws_sdk_cloudformation.types.hook_failure_mode.deserialize_query(
                child_validation_failure_mode
            )
        )
    child_validation_name = el.find("ValidationName")
    if child_validation_name is not None:
        out["validation_name"] = str(child_validation_name.text or "")
    child_validation_status = el.find("ValidationStatus")
    if child_validation_status is not None:
        import aws_sdk_cloudformation.types.validation_status

        out["validation_status"] = (
            aws_sdk_cloudformation.types.validation_status.deserialize_query(
                child_validation_status
            )
        )
    child_validation_status_reason = el.find("ValidationStatusReason")
    if child_validation_status_reason is not None:
        out["validation_status_reason"] = str(child_validation_status_reason.text or "")
    child_validation_path = el.find("ValidationPath")
    if child_validation_path is not None:
        out["validation_path"] = str(child_validation_path.text or "")
    return out
