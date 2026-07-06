"""Generated from Smithy shape ``com.amazonaws.iot#GetCommandResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.boolean_wrapper_object
    import aws_sdk_iot.types.command_arn
    import aws_sdk_iot.types.command_description
    import aws_sdk_iot.types.command_id
    import aws_sdk_iot.types.command_namespace
    import aws_sdk_iot.types.command_parameter_list
    import aws_sdk_iot.types.command_payload
    import aws_sdk_iot.types.command_payload_template_string
    import aws_sdk_iot.types.command_preprocessor
    import aws_sdk_iot.types.date_type
    import aws_sdk_iot.types.deprecation_flag
    import aws_sdk_iot.types.display_name
    import aws_sdk_iot.types.role_arn


class GetCommandResponse(TypedDict, closed=True):
    command_id: NotRequired["aws_sdk_iot.types.command_id.CommandId"]
    """<p>The unique identifier of the command.</p>"""
    command_arn: NotRequired["aws_sdk_iot.types.command_arn.CommandArn"]
    """<p>The Amazon Resource Number (ARN) of the command. For example, <code>arn:aws:iot:<region>:<accountid>:command/<commandId></code> </p>"""
    namespace: NotRequired["aws_sdk_iot.types.command_namespace.CommandNamespace"]
    """<p>The namespace of the command.</p>"""
    display_name: NotRequired["aws_sdk_iot.types.display_name.DisplayName"]
    """<p>The user-friendly name in the console for the command.</p>"""
    description: NotRequired["aws_sdk_iot.types.command_description.CommandDescription"]
    """<p>A short text description of the command.</p>"""
    mandatory_parameters: NotRequired[
        "aws_sdk_iot.types.command_parameter_list.CommandParameterList"
    ]
    """<p>A list of parameters for the command created.</p>"""
    payload: NotRequired["aws_sdk_iot.types.command_payload.CommandPayload"]
    """<p>The payload object that you provided for the command.</p>"""
    payload_template: NotRequired[
        "aws_sdk_iot.types.command_payload_template_string.CommandPayloadTemplateString"
    ]
    """<p>The payload template for the dynamic command.</p>"""
    preprocessor: NotRequired[
        "aws_sdk_iot.types.command_preprocessor.CommandPreprocessor"
    ]
    """<p>Configuration that determines how <code>payloadTemplate</code> is processed to generate command execution payload.</p>"""
    role_arn: NotRequired["aws_sdk_iot.types.role_arn.RoleArn"]
    """<p>The IAM role that you provided when creating the command with <code>AWS-IoT-FleetWise</code> as the namespace.</p>"""
    created_at: NotRequired["aws_sdk_iot.types.date_type.DateType"]
    """<p>The timestamp, when the command was created.</p>"""
    last_updated_at: NotRequired["aws_sdk_iot.types.date_type.DateType"]
    """<p>The timestamp, when the command was last updated.</p>"""
    deprecated: NotRequired["aws_sdk_iot.types.deprecation_flag.DeprecationFlag"]
    """<p>Indicates whether the command has been deprecated.</p>"""
    pending_deletion: NotRequired[
        "aws_sdk_iot.types.boolean_wrapper_object.BooleanWrapperObject"
    ]
    """<p>Indicates whether the command is being deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCommandResponse) -> dict:
    out: dict = {}
    if "command_id" in value:
        out["commandId"] = value["command_id"]
    if "command_arn" in value:
        out["commandArn"] = value["command_arn"]
    if "namespace" in value:
        import aws_sdk_iot.types.command_namespace

        out["namespace"] = aws_sdk_iot.types.command_namespace.serialize_json(
            value["namespace"]
        )
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "description" in value:
        out["description"] = value["description"]
    if "mandatory_parameters" in value:
        import aws_sdk_iot.types.command_parameter_list

        out["mandatoryParameters"] = (
            aws_sdk_iot.types.command_parameter_list.serialize_json(
                value["mandatory_parameters"]
            )
        )
    if "payload" in value:
        import aws_sdk_iot.types.command_payload

        out["payload"] = aws_sdk_iot.types.command_payload.serialize_json(
            value["payload"]
        )
    if "payload_template" in value:
        out["payloadTemplate"] = value["payload_template"]
    if "preprocessor" in value:
        import aws_sdk_iot.types.command_preprocessor

        out["preprocessor"] = aws_sdk_iot.types.command_preprocessor.serialize_json(
            value["preprocessor"]
        )
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    if "created_at" in value:
        import aws_sdk_iot.types.date_type

        out["createdAt"] = aws_sdk_iot.types.date_type.serialize_json(
            value["created_at"]
        )
    if "last_updated_at" in value:
        import aws_sdk_iot.types.date_type

        out["lastUpdatedAt"] = aws_sdk_iot.types.date_type.serialize_json(
            value["last_updated_at"]
        )
    if "deprecated" in value:
        out["deprecated"] = value["deprecated"]
    if "pending_deletion" in value:
        out["pendingDeletion"] = value["pending_deletion"]
    return out


def deserialize_json(data: dict) -> GetCommandResponse:
    out: GetCommandResponse = {}  # type: ignore[typeddict-item]
    if "commandId" in data:
        out["command_id"] = data["commandId"]
    if "commandArn" in data:
        out["command_arn"] = data["commandArn"]
    if "namespace" in data:
        import aws_sdk_iot.types.command_namespace

        out["namespace"] = aws_sdk_iot.types.command_namespace.deserialize_json(
            data["namespace"]
        )
    if "displayName" in data:
        out["display_name"] = data["displayName"]
    if "description" in data:
        out["description"] = data["description"]
    if "mandatoryParameters" in data:
        import aws_sdk_iot.types.command_parameter_list

        out["mandatory_parameters"] = (
            aws_sdk_iot.types.command_parameter_list.deserialize_json(
                data["mandatoryParameters"]
            )
        )
    if "payload" in data:
        import aws_sdk_iot.types.command_payload

        out["payload"] = aws_sdk_iot.types.command_payload.deserialize_json(
            data["payload"]
        )
    if "payloadTemplate" in data:
        out["payload_template"] = data["payloadTemplate"]
    if "preprocessor" in data:
        import aws_sdk_iot.types.command_preprocessor

        out["preprocessor"] = aws_sdk_iot.types.command_preprocessor.deserialize_json(
            data["preprocessor"]
        )
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    if "createdAt" in data:
        import aws_sdk_iot.types.date_type

        out["created_at"] = aws_sdk_iot.types.date_type.deserialize_json(
            data["createdAt"]
        )
    if "lastUpdatedAt" in data:
        import aws_sdk_iot.types.date_type

        out["last_updated_at"] = aws_sdk_iot.types.date_type.deserialize_json(
            data["lastUpdatedAt"]
        )
    if "deprecated" in data:
        out["deprecated"] = data["deprecated"]
    if "pendingDeletion" in data:
        out["pending_deletion"] = data["pendingDeletion"]
    return out
