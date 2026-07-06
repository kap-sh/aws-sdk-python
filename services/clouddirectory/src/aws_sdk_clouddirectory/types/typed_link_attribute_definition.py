"""Generated from Smithy shape ``com.amazonaws.clouddirectory#TypedLinkAttributeDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_clouddirectory.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.attribute_name
    import aws_sdk_clouddirectory.types.bool
    import aws_sdk_clouddirectory.types.facet_attribute_type
    import aws_sdk_clouddirectory.types.required_attribute_behavior
    import aws_sdk_clouddirectory.types.rule_map
    import aws_sdk_clouddirectory.types.typed_attribute_value


class TypedLinkAttributeDefinition(TypedDict, closed=True):
    name: "aws_sdk_clouddirectory.types.attribute_name.AttributeName"
    """<p>The unique name of the typed link attribute.</p>"""
    type: "aws_sdk_clouddirectory.types.facet_attribute_type.FacetAttributeType"
    """<p>The type of the attribute.</p>"""
    default_value: NotRequired[
        "aws_sdk_clouddirectory.types.typed_attribute_value.TypedAttributeValue"
    ]
    """<p>The default value of the attribute (if configured).</p>"""
    is_immutable: "aws_sdk_clouddirectory.types.bool.Bool"
    """<p>Whether the attribute is mutable or not.</p>"""
    rules: NotRequired["aws_sdk_clouddirectory.types.rule_map.RuleMap"]
    """<p>Validation rules that are attached to the attribute definition.</p>"""
    required_behavior: "aws_sdk_clouddirectory.types.required_attribute_behavior.RequiredAttributeBehavior"
    """<p>The required behavior of the <code>TypedLinkAttributeDefinition</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TypedLinkAttributeDefinition) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import aws_sdk_clouddirectory.types.facet_attribute_type

    out["Type"] = aws_sdk_clouddirectory.types.facet_attribute_type.serialize_json(
        value["type"]
    )
    if "default_value" in value:
        import aws_sdk_clouddirectory.types.typed_attribute_value

        out["DefaultValue"] = (
            aws_sdk_clouddirectory.types.typed_attribute_value.serialize_json(
                value["default_value"]
            )
        )
    out["IsImmutable"] = value.get("is_immutable", False)
    if "rules" in value:
        import aws_sdk_clouddirectory.types.rule_map

        out["Rules"] = aws_sdk_clouddirectory.types.rule_map.serialize_json(
            value["rules"]
        )
    import aws_sdk_clouddirectory.types.required_attribute_behavior

    out["RequiredBehavior"] = (
        aws_sdk_clouddirectory.types.required_attribute_behavior.serialize_json(
            value["required_behavior"]
        )
    )
    return out


def deserialize_json(data: dict) -> TypedLinkAttributeDefinition:
    out: TypedLinkAttributeDefinition = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("TypedLinkAttributeDefinition.name required")
    if "Type" in data:
        import aws_sdk_clouddirectory.types.facet_attribute_type

        out["type"] = (
            aws_sdk_clouddirectory.types.facet_attribute_type.deserialize_json(
                data["Type"]
            )
        )
    else:
        raise DeserializationError("TypedLinkAttributeDefinition.type required")
    if "DefaultValue" in data:
        import aws_sdk_clouddirectory.types.typed_attribute_value

        out["default_value"] = (
            aws_sdk_clouddirectory.types.typed_attribute_value.deserialize_json(
                data["DefaultValue"]
            )
        )
    if "IsImmutable" in data:
        out["is_immutable"] = data["IsImmutable"]
    else:
        out["is_immutable"] = False
    if "Rules" in data:
        import aws_sdk_clouddirectory.types.rule_map

        out["rules"] = aws_sdk_clouddirectory.types.rule_map.deserialize_json(
            data["Rules"]
        )
    if "RequiredBehavior" in data:
        import aws_sdk_clouddirectory.types.required_attribute_behavior

        out["required_behavior"] = (
            aws_sdk_clouddirectory.types.required_attribute_behavior.deserialize_json(
                data["RequiredBehavior"]
            )
        )
    else:
        raise DeserializationError(
            "TypedLinkAttributeDefinition.required_behavior required"
        )
    return out
