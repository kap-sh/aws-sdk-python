"""Generated from Smithy shape ``com.amazonaws.devopsagent#NewRelicServiceAuthorizationConfig``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_devops_agent.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.new_relic_api_key_config


class _NewRelicServiceAuthorizationConfig_apiKey(TypedDict):
    apiKey: "aws_sdk_devops_agent.types.new_relic_api_key_config.NewRelicApiKeyConfig"


NewRelicServiceAuthorizationConfig: TypeAlias = (
    _NewRelicServiceAuthorizationConfig_apiKey
)


# --- restJson1 ser/de ---
def serialize_json(value: NewRelicServiceAuthorizationConfig) -> dict:
    if "apiKey" in value:
        import aws_sdk_devops_agent.types.new_relic_api_key_config

        return {
            "apiKey": aws_sdk_devops_agent.types.new_relic_api_key_config.serialize_json(
                value["apiKey"]
            )
        }
    else:
        raise SerializationError(
            "NewRelicServiceAuthorizationConfig: no variant present"
        )


def deserialize_json(data: dict) -> NewRelicServiceAuthorizationConfig:
    if "apiKey" in data:
        import aws_sdk_devops_agent.types.new_relic_api_key_config

        return {
            "apiKey": aws_sdk_devops_agent.types.new_relic_api_key_config.deserialize_json(
                data["apiKey"]
            )
        }
    else:
        raise DeserializationError(
            "NewRelicServiceAuthorizationConfig: no recognized variant key"
        )
