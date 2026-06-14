"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#UpdatedAuthorizerConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.authorizer_configuration


class UpdatedAuthorizerConfiguration(TypedDict):
    optional_value: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.authorizer_configuration.AuthorizerConfiguration"
    ]
    """<p>The updated authorizer configuration value. If not specified, it will clear the current authorizer configuration of the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatedAuthorizerConfiguration) -> dict:
    out: dict = {}
    if "optional_value" in value:
        import aws_sdk_bedrock_agentcore_control.types.authorizer_configuration

        out["optionalValue"] = (
            aws_sdk_bedrock_agentcore_control.types.authorizer_configuration.serialize_json(
                value["optional_value"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdatedAuthorizerConfiguration:
    out: UpdatedAuthorizerConfiguration = {}  # type: ignore[typeddict-item]
    if "optionalValue" in data:
        import aws_sdk_bedrock_agentcore_control.types.authorizer_configuration

        out["optional_value"] = (
            aws_sdk_bedrock_agentcore_control.types.authorizer_configuration.deserialize_json(
                data["optionalValue"]
            )
        )
    return out
