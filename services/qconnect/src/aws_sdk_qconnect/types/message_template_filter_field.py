"""Generated from Smithy shape ``com.amazonaws.qconnect#MessageTemplateFilterField``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.message_template_filter_operator
    import aws_sdk_qconnect.types.message_template_filter_value_list
    import aws_sdk_qconnect.types.non_empty_string


class MessageTemplateFilterField(TypedDict, closed=True):
    name: "aws_sdk_qconnect.types.non_empty_string.NonEmptyString"
    """<p>The name of the attribute field to filter the message templates by.</p>"""
    values: NotRequired[
        "aws_sdk_qconnect.types.message_template_filter_value_list.MessageTemplateFilterValueList"
    ]
    """<p>The values of attribute field to filter the message template by.</p>"""
    operator: "aws_sdk_qconnect.types.message_template_filter_operator.MessageTemplateFilterOperator"
    """<p>The operator to use for filtering.</p>"""
    include_no_existence: NotRequired["bool"]
    """<p>Whether to treat null value as a match for the attribute field.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MessageTemplateFilterField) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "values" in value:
        import aws_sdk_qconnect.types.message_template_filter_value_list

        out["values"] = (
            aws_sdk_qconnect.types.message_template_filter_value_list.serialize_json(
                value["values"]
            )
        )
    out["operator"] = value["operator"]
    if "include_no_existence" in value:
        out["includeNoExistence"] = value["include_no_existence"]
    return out


def deserialize_json(data: dict) -> MessageTemplateFilterField:
    out: MessageTemplateFilterField = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("MessageTemplateFilterField.name required")
    if "values" in data:
        import aws_sdk_qconnect.types.message_template_filter_value_list

        out["values"] = (
            aws_sdk_qconnect.types.message_template_filter_value_list.deserialize_json(
                data["values"]
            )
        )
    if "operator" in data:
        out["operator"] = data["operator"]
    else:
        raise DeserializationError("MessageTemplateFilterField.operator required")
    if "includeNoExistence" in data:
        out["include_no_existence"] = data["includeNoExistence"]
    return out
