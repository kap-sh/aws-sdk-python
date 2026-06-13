"""Generated from Smithy shape ``com.amazonaws.devopsagent#DynatraceServiceAuthorizationConfig``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_devops_agent.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.dynatrace_o_auth_client_credentials_config


class _DynatraceServiceAuthorizationConfig_oAuthClientCredentials(TypedDict):
    oAuthClientCredentials: "aws_sdk_devops_agent.types.dynatrace_o_auth_client_credentials_config.DynatraceOAuthClientCredentialsConfig"


DynatraceServiceAuthorizationConfig: TypeAlias = (
    _DynatraceServiceAuthorizationConfig_oAuthClientCredentials
)


# --- restJson1 ser/de ---
def serialize_json(value: DynatraceServiceAuthorizationConfig) -> dict:
    if "oAuthClientCredentials" in value:
        import aws_sdk_devops_agent.types.dynatrace_o_auth_client_credentials_config

        return {
            "oAuthClientCredentials": aws_sdk_devops_agent.types.dynatrace_o_auth_client_credentials_config.serialize_json(
                value["oAuthClientCredentials"]
            )
        }
    else:
        raise SerializationError(
            "DynatraceServiceAuthorizationConfig: no variant present"
        )


def deserialize_json(data: dict) -> DynatraceServiceAuthorizationConfig:
    if "oAuthClientCredentials" in data:
        import aws_sdk_devops_agent.types.dynatrace_o_auth_client_credentials_config

        return {
            "oAuthClientCredentials": aws_sdk_devops_agent.types.dynatrace_o_auth_client_credentials_config.deserialize_json(
                data["oAuthClientCredentials"]
            )
        }
    else:
        raise DeserializationError(
            "DynatraceServiceAuthorizationConfig: no recognized variant key"
        )
