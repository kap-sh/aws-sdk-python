"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ConfigurationBundleAction``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.static_override
    import aws_sdk_bedrock_agentcore_control.types.weighted_override


class _ConfigurationBundleAction_staticOverride(TypedDict):
    staticOverride: (
        "aws_sdk_bedrock_agentcore_control.types.static_override.StaticOverride"
    )


class _ConfigurationBundleAction_weightedOverride(TypedDict):
    weightedOverride: (
        "aws_sdk_bedrock_agentcore_control.types.weighted_override.WeightedOverride"
    )


ConfigurationBundleAction: TypeAlias = (
    _ConfigurationBundleAction_staticOverride
    | _ConfigurationBundleAction_weightedOverride
)


# --- restJson1 ser/de ---
def serialize_json(value: ConfigurationBundleAction) -> dict:
    if "staticOverride" in value:
        import aws_sdk_bedrock_agentcore_control.types.static_override

        return {
            "staticOverride": aws_sdk_bedrock_agentcore_control.types.static_override.serialize_json(
                value["staticOverride"]
            )
        }
    elif "weightedOverride" in value:
        import aws_sdk_bedrock_agentcore_control.types.weighted_override

        return {
            "weightedOverride": aws_sdk_bedrock_agentcore_control.types.weighted_override.serialize_json(
                value["weightedOverride"]
            )
        }
    else:
        raise SerializationError("ConfigurationBundleAction: no variant present")


def deserialize_json(data: dict) -> ConfigurationBundleAction:
    if "staticOverride" in data:
        import aws_sdk_bedrock_agentcore_control.types.static_override

        return {
            "staticOverride": aws_sdk_bedrock_agentcore_control.types.static_override.deserialize_json(
                data["staticOverride"]
            )
        }
    elif "weightedOverride" in data:
        import aws_sdk_bedrock_agentcore_control.types.weighted_override

        return {
            "weightedOverride": aws_sdk_bedrock_agentcore_control.types.weighted_override.deserialize_json(
                data["weightedOverride"]
            )
        }
    else:
        raise DeserializationError(
            "ConfigurationBundleAction: no recognized variant key"
        )
