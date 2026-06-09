"""Generated from Smithy shape ``com.amazonaws.lambda#OperationUpdate``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_lambda.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lambda.types.callback_options
    import aws_sdk_lambda.types.chained_invoke_options
    import aws_sdk_lambda.types.context_options
    import aws_sdk_lambda.types.error_object
    import aws_sdk_lambda.types.operation_action
    import aws_sdk_lambda.types.operation_id
    import aws_sdk_lambda.types.operation_name
    import aws_sdk_lambda.types.operation_payload
    import aws_sdk_lambda.types.operation_sub_type
    import aws_sdk_lambda.types.operation_type
    import aws_sdk_lambda.types.step_options
    import aws_sdk_lambda.types.wait_options


class OperationUpdate(TypedDict):
    id: "aws_sdk_lambda.types.operation_id.OperationId"
    """<p>The unique identifier for this operation.</p>"""
    parent_id: NotRequired["aws_sdk_lambda.types.operation_id.OperationId"]
    """<p>The unique identifier of the parent operation, if this operation is running within a child context.</p>"""
    name: NotRequired["aws_sdk_lambda.types.operation_name.OperationName"]
    """<p>The customer-provided name for this operation.</p>"""
    type: "aws_sdk_lambda.types.operation_type.OperationType"
    """<p>The type of operation to update.</p>"""
    sub_type: NotRequired["aws_sdk_lambda.types.operation_sub_type.OperationSubType"]
    """<p>The subtype of the operation, providing additional categorization.</p>"""
    action: "aws_sdk_lambda.types.operation_action.OperationAction"
    """<p>The action to take on the operation.</p>"""
    payload: NotRequired["aws_sdk_lambda.types.operation_payload.OperationPayload"]
    """<p>The payload for successful operations.</p>"""
    error: NotRequired["aws_sdk_lambda.types.error_object.ErrorObject"]
    """<p>The error information for failed operations.</p>"""
    context_options: NotRequired["aws_sdk_lambda.types.context_options.ContextOptions"]
    """<p>Options for context operations.</p>"""
    step_options: NotRequired["aws_sdk_lambda.types.step_options.StepOptions"]
    """<p>Options for step operations.</p>"""
    wait_options: NotRequired["aws_sdk_lambda.types.wait_options.WaitOptions"]
    """<p>Options for wait operations.</p>"""
    callback_options: NotRequired[
        "aws_sdk_lambda.types.callback_options.CallbackOptions"
    ]
    chained_invoke_options: NotRequired[
        "aws_sdk_lambda.types.chained_invoke_options.ChainedInvokeOptions"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: OperationUpdate) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    if "parent_id" in value:
        out["ParentId"] = value["parent_id"]
    if "name" in value:
        out["Name"] = value["name"]
    import aws_sdk_lambda.types.operation_type

    out["Type"] = aws_sdk_lambda.types.operation_type.serialize_json(value["type"])
    if "sub_type" in value:
        out["SubType"] = value["sub_type"]
    import aws_sdk_lambda.types.operation_action

    out["Action"] = aws_sdk_lambda.types.operation_action.serialize_json(
        value["action"]
    )
    if "payload" in value:
        out["Payload"] = value["payload"]
    if "error" in value:
        import aws_sdk_lambda.types.error_object

        out["Error"] = aws_sdk_lambda.types.error_object.serialize_json(value["error"])
    if "context_options" in value:
        import aws_sdk_lambda.types.context_options

        out["ContextOptions"] = aws_sdk_lambda.types.context_options.serialize_json(
            value["context_options"]
        )
    if "step_options" in value:
        import aws_sdk_lambda.types.step_options

        out["StepOptions"] = aws_sdk_lambda.types.step_options.serialize_json(
            value["step_options"]
        )
    if "wait_options" in value:
        import aws_sdk_lambda.types.wait_options

        out["WaitOptions"] = aws_sdk_lambda.types.wait_options.serialize_json(
            value["wait_options"]
        )
    if "callback_options" in value:
        import aws_sdk_lambda.types.callback_options

        out["CallbackOptions"] = aws_sdk_lambda.types.callback_options.serialize_json(
            value["callback_options"]
        )
    if "chained_invoke_options" in value:
        import aws_sdk_lambda.types.chained_invoke_options

        out["ChainedInvokeOptions"] = (
            aws_sdk_lambda.types.chained_invoke_options.serialize_json(
                value["chained_invoke_options"]
            )
        )
    return out


def deserialize_json(data: dict) -> OperationUpdate:
    out: OperationUpdate = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("OperationUpdate.id required")
    if "ParentId" in data:
        out["parent_id"] = data["ParentId"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Type" in data:
        import aws_sdk_lambda.types.operation_type

        out["type"] = aws_sdk_lambda.types.operation_type.deserialize_json(data["Type"])
    else:
        raise DeserializationError("OperationUpdate.type required")
    if "SubType" in data:
        out["sub_type"] = data["SubType"]
    if "Action" in data:
        import aws_sdk_lambda.types.operation_action

        out["action"] = aws_sdk_lambda.types.operation_action.deserialize_json(
            data["Action"]
        )
    else:
        raise DeserializationError("OperationUpdate.action required")
    if "Payload" in data:
        out["payload"] = data["Payload"]
    if "Error" in data:
        import aws_sdk_lambda.types.error_object

        out["error"] = aws_sdk_lambda.types.error_object.deserialize_json(data["Error"])
    if "ContextOptions" in data:
        import aws_sdk_lambda.types.context_options

        out["context_options"] = aws_sdk_lambda.types.context_options.deserialize_json(
            data["ContextOptions"]
        )
    if "StepOptions" in data:
        import aws_sdk_lambda.types.step_options

        out["step_options"] = aws_sdk_lambda.types.step_options.deserialize_json(
            data["StepOptions"]
        )
    if "WaitOptions" in data:
        import aws_sdk_lambda.types.wait_options

        out["wait_options"] = aws_sdk_lambda.types.wait_options.deserialize_json(
            data["WaitOptions"]
        )
    if "CallbackOptions" in data:
        import aws_sdk_lambda.types.callback_options

        out["callback_options"] = (
            aws_sdk_lambda.types.callback_options.deserialize_json(
                data["CallbackOptions"]
            )
        )
    if "ChainedInvokeOptions" in data:
        import aws_sdk_lambda.types.chained_invoke_options

        out["chained_invoke_options"] = (
            aws_sdk_lambda.types.chained_invoke_options.deserialize_json(
                data["ChainedInvokeOptions"]
            )
        )
    return out
