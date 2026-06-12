"""Generated from Smithy shape ``com.amazonaws.qbusiness#ActionReviewPayloadField``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.action_payload_field_type
    import aws_sdk_qbusiness.types.action_payload_field_value
    import aws_sdk_qbusiness.types.action_review_payload_field_allowed_values
    import aws_sdk_qbusiness.types.action_review_payload_field_array_item_json_schema
    import aws_sdk_qbusiness.types.integer
    import aws_sdk_qbusiness.types.string

class ActionReviewPayloadField(TypedDict):
    display_name: NotRequired["aws_sdk_qbusiness.types.string.String"]
    """<p> The name of the field. </p>"""
    display_order: NotRequired["aws_sdk_qbusiness.types.integer.Integer"]
    """<p>The display order of fields in a payload.</p>"""
    display_description: NotRequired["aws_sdk_qbusiness.types.string.String"]
    """<p>The field level description of each action review input field. This could be an explanation of the field. In the Amazon Q Business web experience, these descriptions could be used to display as tool tips to help users understand the field. </p>"""
    type: NotRequired["aws_sdk_qbusiness.types.action_payload_field_type.ActionPayloadFieldType"]
    """<p>The type of field. </p>"""
    value: NotRequired["aws_sdk_qbusiness.types.action_payload_field_value.ActionPayloadFieldValue"]
    """<p>The field value.</p>"""
    allowed_values: NotRequired["aws_sdk_qbusiness.types.action_review_payload_field_allowed_values.ActionReviewPayloadFieldAllowedValues"]
    """<p>Information about the field values that an end user can use to provide to Amazon Q Business for Amazon Q Business to perform the requested plugin action.</p>"""
    allowed_format: NotRequired["aws_sdk_qbusiness.types.string.String"]
    """<p>The expected data format for the action review input field value. For example, in PTO request, <code>from</code> and <code>to</code> would be of <code>datetime</code> allowed format. </p>"""
    array_item_json_schema: NotRequired["aws_sdk_qbusiness.types.action_review_payload_field_array_item_json_schema.ActionReviewPayloadFieldArrayItemJsonSchema"]
    """<p>Use to create a custom form with array fields (fields with nested objects inside an array).</p>"""
    required: NotRequired["bool"]
    """<p>Information about whether the field is required.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: ActionReviewPayloadField) -> dict:
    out: dict = {}
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "display_order" in value:
        out["displayOrder"] = value["display_order"]
    if "display_description" in value:
        out["displayDescription"] = value["display_description"]
    if "type" in value:
        import aws_sdk_qbusiness.types.action_payload_field_type
        out["type"] = aws_sdk_qbusiness.types.action_payload_field_type.serialize_json(value["type"])
    if "value" in value:
        out["value"] = value["value"]
    if "allowed_values" in value:
        import aws_sdk_qbusiness.types.action_review_payload_field_allowed_values
        out["allowedValues"] = aws_sdk_qbusiness.types.action_review_payload_field_allowed_values.serialize_json(value["allowed_values"])
    if "allowed_format" in value:
        out["allowedFormat"] = value["allowed_format"]
    if "array_item_json_schema" in value:
        out["arrayItemJsonSchema"] = value["array_item_json_schema"]
    if "required" in value:
        out["required"] = value["required"]
    return out


def deserialize_json(data: dict) -> ActionReviewPayloadField:
    out: ActionReviewPayloadField = {}  # type: ignore[typeddict-item]
    if "displayName" in data:
        out["display_name"] = data["displayName"]
    if "displayOrder" in data:
        out["display_order"] = data["displayOrder"]
    if "displayDescription" in data:
        out["display_description"] = data["displayDescription"]
    if "type" in data:
        import aws_sdk_qbusiness.types.action_payload_field_type
        out["type"] = aws_sdk_qbusiness.types.action_payload_field_type.deserialize_json(data["type"])
    if "value" in data:
        out["value"] = data["value"]
    if "allowedValues" in data:
        import aws_sdk_qbusiness.types.action_review_payload_field_allowed_values
        out["allowed_values"] = aws_sdk_qbusiness.types.action_review_payload_field_allowed_values.deserialize_json(data["allowedValues"])
    if "allowedFormat" in data:
        out["allowed_format"] = data["allowedFormat"]
    if "arrayItemJsonSchema" in data:
        out["array_item_json_schema"] = data["arrayItemJsonSchema"]
    if "required" in data:
        out["required"] = data["required"]
    return out