"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#Variant``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.variant_configuration
    import aws_sdk_bedrock_agentcore.types.variant_name


class Variant(TypedDict, closed=True):
    name: "aws_sdk_bedrock_agentcore.types.variant_name.VariantName"
    """<p>The name of the variant. Must be <code>C</code> for control or <code>T1</code> for treatment.</p>"""
    weight: "int"
    """<p>The percentage of traffic to route to this variant. Weights across all variants must sum to 100.</p>"""
    variant_configuration: (
        "aws_sdk_bedrock_agentcore.types.variant_configuration.VariantConfiguration"
    )
    """<p>The configuration for this variant, including the configuration bundle or target reference.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Variant) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["weight"] = value["weight"]
    import aws_sdk_bedrock_agentcore.types.variant_configuration

    out["variantConfiguration"] = (
        aws_sdk_bedrock_agentcore.types.variant_configuration.serialize_json(
            value["variant_configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> Variant:
    out: Variant = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("Variant.name required")
    if "weight" in data:
        out["weight"] = data["weight"]
    else:
        raise DeserializationError("Variant.weight required")
    if "variantConfiguration" in data:
        import aws_sdk_bedrock_agentcore.types.variant_configuration

        out["variant_configuration"] = (
            aws_sdk_bedrock_agentcore.types.variant_configuration.deserialize_json(
                data["variantConfiguration"]
            )
        )
    else:
        raise DeserializationError("Variant.variant_configuration required")
    return out
