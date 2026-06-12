"""Generated from Smithy shape ``com.amazonaws.connectcases#FieldSummary``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_connectcases.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.field_arn
    import aws_sdk_connectcases.types.field_attributes
    import aws_sdk_connectcases.types.field_id
    import aws_sdk_connectcases.types.field_name
    import aws_sdk_connectcases.types.field_namespace
    import aws_sdk_connectcases.types.field_type


class FieldSummary(TypedDict):
    field_id: "aws_sdk_connectcases.types.field_id.FieldId"
    """<p>The unique identifier of a field.</p>"""
    field_arn: "aws_sdk_connectcases.types.field_arn.FieldArn"
    """<p>The Amazon Resource Name (ARN) of the field.</p>"""
    name: "aws_sdk_connectcases.types.field_name.FieldName"
    """<p>Name of the field.</p>"""
    type: "aws_sdk_connectcases.types.field_type.FieldType"
    """<p>The type of a field.</p>"""
    namespace: "aws_sdk_connectcases.types.field_namespace.FieldNamespace"
    """<p>The namespace of a field.</p>"""
    attributes: NotRequired[
        "aws_sdk_connectcases.types.field_attributes.FieldAttributes"
    ]
    """<p>Union of field attributes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FieldSummary) -> dict:
    out: dict = {}
    out["fieldId"] = value["field_id"]
    out["fieldArn"] = value["field_arn"]
    out["name"] = value["name"]
    out["type"] = value["type"]
    out["namespace"] = value["namespace"]
    if "attributes" in value:
        import aws_sdk_connectcases.types.field_attributes

        out["attributes"] = aws_sdk_connectcases.types.field_attributes.serialize_json(
            value["attributes"]
        )
    return out


def deserialize_json(data: dict) -> FieldSummary:
    out: FieldSummary = {}  # type: ignore[typeddict-item]
    if "fieldId" in data:
        out["field_id"] = data["fieldId"]
    else:
        raise DeserializationError("FieldSummary.field_id required")
    if "fieldArn" in data:
        out["field_arn"] = data["fieldArn"]
    else:
        raise DeserializationError("FieldSummary.field_arn required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("FieldSummary.name required")
    if "type" in data:
        out["type"] = data["type"]
    else:
        raise DeserializationError("FieldSummary.type required")
    if "namespace" in data:
        out["namespace"] = data["namespace"]
    else:
        raise DeserializationError("FieldSummary.namespace required")
    if "attributes" in data:
        import aws_sdk_connectcases.types.field_attributes

        out["attributes"] = (
            aws_sdk_connectcases.types.field_attributes.deserialize_json(
                data["attributes"]
            )
        )
    return out
