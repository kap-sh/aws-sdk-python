"""Generated from Smithy shape ``com.amazonaws.codepipeline#RuleConfigurationProperty``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_codepipeline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.boolean
    import aws_sdk_codepipeline.types.description
    import aws_sdk_codepipeline.types.rule_configuration_key
    import aws_sdk_codepipeline.types.rule_configuration_property_type


class RuleConfigurationProperty(TypedDict, closed=True):
    name: "aws_sdk_codepipeline.types.rule_configuration_key.RuleConfigurationKey"
    """<p>The name of the rule configuration property.</p>"""
    required: "aws_sdk_codepipeline.types.boolean.Boolean"
    """<p>Whether the configuration property is a required value.</p>"""
    key: "aws_sdk_codepipeline.types.boolean.Boolean"
    """<p>Whether the configuration property is a key.</p>"""
    secret: "aws_sdk_codepipeline.types.boolean.Boolean"
    """<p>Whether the configuration property is secret.</p> <p>When updating a pipeline, passing * * * * * without changing any other values of the action preserves the previous value of the secret.</p>"""
    queryable: "aws_sdk_codepipeline.types.boolean.Boolean"
    """<p>Indicates whether the property can be queried.</p> <p>If you create a pipeline with a condition and rule, and that rule contains a queryable property, the value for that configuration property is subject to other restrictions. The value must be less than or equal to twenty (20) characters. The value can contain only alphanumeric characters, underscores, and hyphens.</p>"""
    description: NotRequired["aws_sdk_codepipeline.types.description.Description"]
    """<p>The description of the action configuration property that is displayed to users.</p>"""
    type: NotRequired[
        "aws_sdk_codepipeline.types.rule_configuration_property_type.RuleConfigurationPropertyType"
    ]
    """<p>The type of the configuration property.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RuleConfigurationProperty) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["required"] = value.get("required", False)
    out["key"] = value.get("key", False)
    out["secret"] = value.get("secret", False)
    out["queryable"] = value.get("queryable", False)
    if "description" in value:
        out["description"] = value["description"]
    if "type" in value:
        import aws_sdk_codepipeline.types.rule_configuration_property_type

        out["type"] = (
            aws_sdk_codepipeline.types.rule_configuration_property_type.serialize_aws_json_1_1(
                value["type"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RuleConfigurationProperty:
    out: RuleConfigurationProperty = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("RuleConfigurationProperty.name required")
    if "required" in data:
        out["required"] = data["required"]
    else:
        out["required"] = False
    if "key" in data:
        out["key"] = data["key"]
    else:
        out["key"] = False
    if "secret" in data:
        out["secret"] = data["secret"]
    else:
        out["secret"] = False
    if "queryable" in data:
        out["queryable"] = data["queryable"]
    else:
        out["queryable"] = False
    if "description" in data:
        out["description"] = data["description"]
    if "type" in data:
        import aws_sdk_codepipeline.types.rule_configuration_property_type

        out["type"] = (
            aws_sdk_codepipeline.types.rule_configuration_property_type.deserialize_aws_json_1_1(
                data["type"]
            )
        )
    return out
