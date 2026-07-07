"""Generated from Smithy shape ``com.amazonaws.qconnect#ToolConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.annotation
    import aws_sdk_qconnect.types.json_document
    import aws_sdk_qconnect.types.non_empty_sensitive_string
    import aws_sdk_qconnect.types.non_empty_string
    import aws_sdk_qconnect.types.tool_instruction
    import aws_sdk_qconnect.types.tool_output_filter_list
    import aws_sdk_qconnect.types.tool_override_input_value_list
    import aws_sdk_qconnect.types.tool_type
    import aws_sdk_qconnect.types.user_interaction_configuration


class ToolConfiguration(TypedDict, closed=True):
    tool_name: "aws_sdk_qconnect.types.non_empty_string.NonEmptyString"
    """<p>The name of the tool.</p>"""
    tool_type: "aws_sdk_qconnect.types.tool_type.ToolType"
    """<p>The type of the tool.</p>"""
    title: NotRequired[
        "aws_sdk_qconnect.types.non_empty_sensitive_string.NonEmptySensitiveString"
    ]
    """<p>The title of the tool configuration.</p>"""
    tool_id: NotRequired["aws_sdk_qconnect.types.non_empty_string.NonEmptyString"]
    """<p>The identifier of the tool, for example toolName from Model Context Provider server.</p>"""
    description: NotRequired[
        "aws_sdk_qconnect.types.non_empty_sensitive_string.NonEmptySensitiveString"
    ]
    """<p>The description of the tool configuration.</p>"""
    instruction: NotRequired["aws_sdk_qconnect.types.tool_instruction.ToolInstruction"]
    """<p>Instructions for using the tool.</p>"""
    override_input_values: NotRequired[
        "aws_sdk_qconnect.types.tool_override_input_value_list.ToolOverrideInputValueList"
    ]
    """<p>Override input values for the tool configuration.</p>"""
    output_filters: NotRequired[
        "aws_sdk_qconnect.types.tool_output_filter_list.ToolOutputFilterList"
    ]
    """<p>Output filters applies to the tool result.</p>"""
    input_schema: NotRequired["aws_sdk_qconnect.types.json_document.JSONDocument"]
    """<p>The input schema for the tool configuration.</p>"""
    output_schema: NotRequired["aws_sdk_qconnect.types.json_document.JSONDocument"]
    """<p>The output schema for the tool configuration.</p>"""
    annotations: NotRequired["aws_sdk_qconnect.types.annotation.Annotation"]
    """<p>Annotations for the tool configuration.</p>"""
    user_interaction_configuration: NotRequired[
        "aws_sdk_qconnect.types.user_interaction_configuration.UserInteractionConfiguration"
    ]
    """<p>Configuration for user interaction with the tool.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ToolConfiguration) -> dict:
    out: dict = {}
    out["toolName"] = value["tool_name"]
    out["toolType"] = value["tool_type"]
    if "title" in value:
        out["title"] = value["title"]
    if "tool_id" in value:
        out["toolId"] = value["tool_id"]
    if "description" in value:
        out["description"] = value["description"]
    if "instruction" in value:
        import aws_sdk_qconnect.types.tool_instruction

        out["instruction"] = aws_sdk_qconnect.types.tool_instruction.serialize_json(
            value["instruction"]
        )
    if "override_input_values" in value:
        import aws_sdk_qconnect.types.tool_override_input_value_list

        out["overrideInputValues"] = (
            aws_sdk_qconnect.types.tool_override_input_value_list.serialize_json(
                value["override_input_values"]
            )
        )
    if "output_filters" in value:
        import aws_sdk_qconnect.types.tool_output_filter_list

        out["outputFilters"] = (
            aws_sdk_qconnect.types.tool_output_filter_list.serialize_json(
                value["output_filters"]
            )
        )
    if "input_schema" in value:
        out["inputSchema"] = value["input_schema"]
    if "output_schema" in value:
        out["outputSchema"] = value["output_schema"]
    if "annotations" in value:
        import aws_sdk_qconnect.types.annotation

        out["annotations"] = aws_sdk_qconnect.types.annotation.serialize_json(
            value["annotations"]
        )
    if "user_interaction_configuration" in value:
        import aws_sdk_qconnect.types.user_interaction_configuration

        out["userInteractionConfiguration"] = (
            aws_sdk_qconnect.types.user_interaction_configuration.serialize_json(
                value["user_interaction_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> ToolConfiguration:
    out: ToolConfiguration = {}  # type: ignore[typeddict-item]
    if "toolName" in data:
        out["tool_name"] = data["toolName"]
    else:
        raise DeserializationError("ToolConfiguration.tool_name required")
    if "toolType" in data:
        out["tool_type"] = data["toolType"]
    else:
        raise DeserializationError("ToolConfiguration.tool_type required")
    if "title" in data:
        out["title"] = data["title"]
    if "toolId" in data:
        out["tool_id"] = data["toolId"]
    if "description" in data:
        out["description"] = data["description"]
    if "instruction" in data:
        import aws_sdk_qconnect.types.tool_instruction

        out["instruction"] = aws_sdk_qconnect.types.tool_instruction.deserialize_json(
            data["instruction"]
        )
    if "overrideInputValues" in data:
        import aws_sdk_qconnect.types.tool_override_input_value_list

        out["override_input_values"] = (
            aws_sdk_qconnect.types.tool_override_input_value_list.deserialize_json(
                data["overrideInputValues"]
            )
        )
    if "outputFilters" in data:
        import aws_sdk_qconnect.types.tool_output_filter_list

        out["output_filters"] = (
            aws_sdk_qconnect.types.tool_output_filter_list.deserialize_json(
                data["outputFilters"]
            )
        )
    if "inputSchema" in data:
        out["input_schema"] = data["inputSchema"]
    if "outputSchema" in data:
        out["output_schema"] = data["outputSchema"]
    if "annotations" in data:
        import aws_sdk_qconnect.types.annotation

        out["annotations"] = aws_sdk_qconnect.types.annotation.deserialize_json(
            data["annotations"]
        )
    if "userInteractionConfiguration" in data:
        import aws_sdk_qconnect.types.user_interaction_configuration

        out["user_interaction_configuration"] = (
            aws_sdk_qconnect.types.user_interaction_configuration.deserialize_json(
                data["userInteractionConfiguration"]
            )
        )
    return out
