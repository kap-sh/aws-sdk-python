"""Generated from Smithy shape ``com.amazonaws.codepipeline#ActionTypeProperty``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_codepipeline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.action_configuration_key
    import aws_sdk_codepipeline.types.boolean
    import aws_sdk_codepipeline.types.property_description


class ActionTypeProperty(TypedDict, closed=True):
    name: "aws_sdk_codepipeline.types.action_configuration_key.ActionConfigurationKey"
    """<p>The property name that is displayed to users.</p>"""
    optional: "aws_sdk_codepipeline.types.boolean.Boolean"
    """<p>Whether the configuration property is an optional value.</p>"""
    key: "aws_sdk_codepipeline.types.boolean.Boolean"
    """<p>Whether the configuration property is a key.</p>"""
    no_echo: "aws_sdk_codepipeline.types.boolean.Boolean"
    """<p>Whether to omit the field value entered by the customer in the log. If <code>true</code>, the value is not saved in CloudTrail logs for the action execution.</p>"""
    queryable: "aws_sdk_codepipeline.types.boolean.Boolean"
    """<p>Indicates that the property is used with polling. An action type can have up to one queryable property. If it has one, that property must be both required and not secret.</p>"""
    description: NotRequired[
        "aws_sdk_codepipeline.types.property_description.PropertyDescription"
    ]
    """<p>The description of the property that is displayed to users.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ActionTypeProperty) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["optional"] = value.get("optional", False)
    out["key"] = value.get("key", False)
    out["noEcho"] = value.get("no_echo", False)
    out["queryable"] = value.get("queryable", False)
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ActionTypeProperty:
    out: ActionTypeProperty = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("ActionTypeProperty.name required")
    if "optional" in data:
        out["optional"] = data["optional"]
    else:
        out["optional"] = False
    if "key" in data:
        out["key"] = data["key"]
    else:
        out["key"] = False
    if "noEcho" in data:
        out["no_echo"] = data["noEcho"]
    else:
        out["no_echo"] = False
    if "queryable" in data:
        out["queryable"] = data["queryable"]
    else:
        out["queryable"] = False
    if "description" in data:
        out["description"] = data["description"]
    return out
