"""Generated from Smithy shape ``com.amazonaws.iot#CreateCommandRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.command_description
    import aws_sdk_iot.types.command_id
    import aws_sdk_iot.types.command_namespace
    import aws_sdk_iot.types.command_parameter_list
    import aws_sdk_iot.types.command_payload
    import aws_sdk_iot.types.command_payload_template_string
    import aws_sdk_iot.types.command_preprocessor
    import aws_sdk_iot.types.display_name
    import aws_sdk_iot.types.role_arn
    import aws_sdk_iot.types.tag_list


class CreateCommandRequest(TypedDict):
    command_id: "aws_sdk_iot.types.command_id.CommandId"
    """<p>A unique identifier for the command. We recommend using UUID. Alpha-numeric characters, hyphens, and underscores are valid for use here.</p>"""
    namespace: NotRequired["aws_sdk_iot.types.command_namespace.CommandNamespace"]
    """<p>The namespace of the command. The MQTT reserved topics and validations will be used for command executions according to the namespace setting.</p>"""
    display_name: NotRequired["aws_sdk_iot.types.display_name.DisplayName"]
    """<p>The user-friendly name in the console for the command. This name doesn't have to be unique. You can update the user-friendly name after you define it.</p>"""
    description: NotRequired["aws_sdk_iot.types.command_description.CommandDescription"]
    """<p>A short text decription of the command.</p>"""
    payload: NotRequired["aws_sdk_iot.types.command_payload.CommandPayload"]
    """<p>The payload object for the static command.</p> <p>You can upload a static payload file from your local storage that contains the instructions for the device to process. The payload file can use any format. To make sure that the device correctly interprets the payload, we recommend you to specify the payload content type.</p>"""
    payload_template: NotRequired[
        "aws_sdk_iot.types.command_payload_template_string.CommandPayloadTemplateString"
    ]
    """<p>The payload template for the dynamic command.</p> <note> <p>This parameter is required for dynamic commands where the command execution placeholders are supplied either from <code>mandatoryParameters</code> or when <code>StartCommandExecution</code> is invoked.</p> </note>"""
    preprocessor: NotRequired[
        "aws_sdk_iot.types.command_preprocessor.CommandPreprocessor"
    ]
    """<p>Configuration that determines how <code>payloadTemplate</code> is processed to generate command execution payload.</p> <note> <p>This parameter is required for dynamic commands, along with <code>payloadTemplate</code>, and <code>mandatoryParameters</code>.</p> </note>"""
    mandatory_parameters: NotRequired[
        "aws_sdk_iot.types.command_parameter_list.CommandParameterList"
    ]
    """<p>A list of parameters that are used by <code>StartCommandExecution</code> API for execution payload generation.</p>"""
    role_arn: NotRequired["aws_sdk_iot.types.role_arn.RoleArn"]
    """<p>The IAM role that you must provide when using the <code>AWS-IoT-FleetWise</code> namespace. The role grants IoT Device Management the permission to access IoT FleetWise resources for generating the payload for the command. This field is not supported when you use the <code>AWS-IoT</code> namespace.</p>"""
    tags: NotRequired["aws_sdk_iot.types.tag_list.TagList"]
    """<p>Name-value pairs that are used as metadata to manage a command.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateCommandRequest) -> dict:
    out: dict = {}
    if "namespace" in value:
        import aws_sdk_iot.types.command_namespace

        out["namespace"] = aws_sdk_iot.types.command_namespace.serialize_json(
            value["namespace"]
        )
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "description" in value:
        out["description"] = value["description"]
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
    if "mandatory_parameters" in value:
        import aws_sdk_iot.types.command_parameter_list

        out["mandatoryParameters"] = (
            aws_sdk_iot.types.command_parameter_list.serialize_json(
                value["mandatory_parameters"]
            )
        )
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    if "tags" in value:
        import aws_sdk_iot.types.tag_list

        out["tags"] = aws_sdk_iot.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateCommandRequest:
    out: CreateCommandRequest = {}  # type: ignore[typeddict-item]
    if "namespace" in data:
        import aws_sdk_iot.types.command_namespace

        out["namespace"] = aws_sdk_iot.types.command_namespace.deserialize_json(
            data["namespace"]
        )
    if "displayName" in data:
        out["display_name"] = data["displayName"]
    if "description" in data:
        out["description"] = data["description"]
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
    if "mandatoryParameters" in data:
        import aws_sdk_iot.types.command_parameter_list

        out["mandatory_parameters"] = (
            aws_sdk_iot.types.command_parameter_list.deserialize_json(
                data["mandatoryParameters"]
            )
        )
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    if "tags" in data:
        import aws_sdk_iot.types.tag_list

        out["tags"] = aws_sdk_iot.types.tag_list.deserialize_json(data["tags"])
    return out
