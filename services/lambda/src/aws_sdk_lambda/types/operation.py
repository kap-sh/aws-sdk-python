"""Generated from Smithy shape ``com.amazonaws.lambda#Operation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_lambda.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lambda.types.callback_details
    import aws_sdk_lambda.types.chained_invoke_details
    import aws_sdk_lambda.types.context_details
    import aws_sdk_lambda.types.execution_details
    import aws_sdk_lambda.types.execution_timestamp
    import aws_sdk_lambda.types.operation_id
    import aws_sdk_lambda.types.operation_name
    import aws_sdk_lambda.types.operation_status
    import aws_sdk_lambda.types.operation_sub_type
    import aws_sdk_lambda.types.operation_type
    import aws_sdk_lambda.types.step_details
    import aws_sdk_lambda.types.wait_details


class Operation(TypedDict):
    id: "aws_sdk_lambda.types.operation_id.OperationId"
    """<p>The unique identifier for this operation.</p>"""
    parent_id: NotRequired["aws_sdk_lambda.types.operation_id.OperationId"]
    """<p>The unique identifier of the parent operation, if this operation is running within a child context.</p>"""
    name: NotRequired["aws_sdk_lambda.types.operation_name.OperationName"]
    """<p>The customer-provided name for this operation.</p>"""
    type: "aws_sdk_lambda.types.operation_type.OperationType"
    """<p>The type of operation.</p>"""
    sub_type: NotRequired["aws_sdk_lambda.types.operation_sub_type.OperationSubType"]
    """<p>The subtype of the operation, providing additional categorization.</p>"""
    start_timestamp: "aws_sdk_lambda.types.execution_timestamp.ExecutionTimestamp"
    r"""<p>The date and time when the operation started, in <a href=\"https://www.w3.org/TR/NOTE-datetime\">ISO-8601 format</a> (YYYY-MM-DDThh:mm:ss.sTZD).</p>"""
    end_timestamp: NotRequired[
        "aws_sdk_lambda.types.execution_timestamp.ExecutionTimestamp"
    ]
    r"""<p>The date and time when the operation ended, in <a href=\"https://www.w3.org/TR/NOTE-datetime\">ISO-8601 format</a> (YYYY-MM-DDThh:mm:ss.sTZD).</p>"""
    status: "aws_sdk_lambda.types.operation_status.OperationStatus"
    """<p>The current status of the operation.</p>"""
    execution_details: NotRequired[
        "aws_sdk_lambda.types.execution_details.ExecutionDetails"
    ]
    """<p>Details about the execution, if this operation represents an execution.</p>"""
    context_details: NotRequired["aws_sdk_lambda.types.context_details.ContextDetails"]
    """<p>Details about the context, if this operation represents a context.</p>"""
    step_details: NotRequired["aws_sdk_lambda.types.step_details.StepDetails"]
    """<p>Details about the step, if this operation represents a step.</p>"""
    wait_details: NotRequired["aws_sdk_lambda.types.wait_details.WaitDetails"]
    """<p>Details about the wait operation, if this operation represents a wait.</p>"""
    callback_details: NotRequired[
        "aws_sdk_lambda.types.callback_details.CallbackDetails"
    ]
    chained_invoke_details: NotRequired[
        "aws_sdk_lambda.types.chained_invoke_details.ChainedInvokeDetails"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: Operation) -> dict:
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
    import aws_sdk_lambda.types.execution_timestamp

    out["StartTimestamp"] = aws_sdk_lambda.types.execution_timestamp.serialize_json(
        value["start_timestamp"]
    )
    if "end_timestamp" in value:
        import aws_sdk_lambda.types.execution_timestamp

        out["EndTimestamp"] = aws_sdk_lambda.types.execution_timestamp.serialize_json(
            value["end_timestamp"]
        )
    import aws_sdk_lambda.types.operation_status

    out["Status"] = aws_sdk_lambda.types.operation_status.serialize_json(
        value["status"]
    )
    if "execution_details" in value:
        import aws_sdk_lambda.types.execution_details

        out["ExecutionDetails"] = aws_sdk_lambda.types.execution_details.serialize_json(
            value["execution_details"]
        )
    if "context_details" in value:
        import aws_sdk_lambda.types.context_details

        out["ContextDetails"] = aws_sdk_lambda.types.context_details.serialize_json(
            value["context_details"]
        )
    if "step_details" in value:
        import aws_sdk_lambda.types.step_details

        out["StepDetails"] = aws_sdk_lambda.types.step_details.serialize_json(
            value["step_details"]
        )
    if "wait_details" in value:
        import aws_sdk_lambda.types.wait_details

        out["WaitDetails"] = aws_sdk_lambda.types.wait_details.serialize_json(
            value["wait_details"]
        )
    if "callback_details" in value:
        import aws_sdk_lambda.types.callback_details

        out["CallbackDetails"] = aws_sdk_lambda.types.callback_details.serialize_json(
            value["callback_details"]
        )
    if "chained_invoke_details" in value:
        import aws_sdk_lambda.types.chained_invoke_details

        out["ChainedInvokeDetails"] = (
            aws_sdk_lambda.types.chained_invoke_details.serialize_json(
                value["chained_invoke_details"]
            )
        )
    return out


def deserialize_json(data: dict) -> Operation:
    out: Operation = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("Operation.id required")
    if "ParentId" in data:
        out["parent_id"] = data["ParentId"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Type" in data:
        import aws_sdk_lambda.types.operation_type

        out["type"] = aws_sdk_lambda.types.operation_type.deserialize_json(data["Type"])
    else:
        raise DeserializationError("Operation.type required")
    if "SubType" in data:
        out["sub_type"] = data["SubType"]
    if "StartTimestamp" in data:
        import aws_sdk_lambda.types.execution_timestamp

        out["start_timestamp"] = (
            aws_sdk_lambda.types.execution_timestamp.deserialize_json(
                data["StartTimestamp"]
            )
        )
    else:
        raise DeserializationError("Operation.start_timestamp required")
    if "EndTimestamp" in data:
        import aws_sdk_lambda.types.execution_timestamp

        out["end_timestamp"] = (
            aws_sdk_lambda.types.execution_timestamp.deserialize_json(
                data["EndTimestamp"]
            )
        )
    if "Status" in data:
        import aws_sdk_lambda.types.operation_status

        out["status"] = aws_sdk_lambda.types.operation_status.deserialize_json(
            data["Status"]
        )
    else:
        raise DeserializationError("Operation.status required")
    if "ExecutionDetails" in data:
        import aws_sdk_lambda.types.execution_details

        out["execution_details"] = (
            aws_sdk_lambda.types.execution_details.deserialize_json(
                data["ExecutionDetails"]
            )
        )
    if "ContextDetails" in data:
        import aws_sdk_lambda.types.context_details

        out["context_details"] = aws_sdk_lambda.types.context_details.deserialize_json(
            data["ContextDetails"]
        )
    if "StepDetails" in data:
        import aws_sdk_lambda.types.step_details

        out["step_details"] = aws_sdk_lambda.types.step_details.deserialize_json(
            data["StepDetails"]
        )
    if "WaitDetails" in data:
        import aws_sdk_lambda.types.wait_details

        out["wait_details"] = aws_sdk_lambda.types.wait_details.deserialize_json(
            data["WaitDetails"]
        )
    if "CallbackDetails" in data:
        import aws_sdk_lambda.types.callback_details

        out["callback_details"] = (
            aws_sdk_lambda.types.callback_details.deserialize_json(
                data["CallbackDetails"]
            )
        )
    if "ChainedInvokeDetails" in data:
        import aws_sdk_lambda.types.chained_invoke_details

        out["chained_invoke_details"] = (
            aws_sdk_lambda.types.chained_invoke_details.deserialize_json(
                data["ChainedInvokeDetails"]
            )
        )
    return out
