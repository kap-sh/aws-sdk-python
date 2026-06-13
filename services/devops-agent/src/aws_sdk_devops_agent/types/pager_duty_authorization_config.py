"""Generated from Smithy shape ``com.amazonaws.devopsagent#PagerDutyAuthorizationConfig``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_devops_agent.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.pager_duty_o_auth_client_credentials_config


class _PagerDutyAuthorizationConfig_oAuthClientCredentials(TypedDict):
    oAuthClientCredentials: "aws_sdk_devops_agent.types.pager_duty_o_auth_client_credentials_config.PagerDutyOAuthClientCredentialsConfig"


PagerDutyAuthorizationConfig: TypeAlias = (
    _PagerDutyAuthorizationConfig_oAuthClientCredentials
)


# --- restJson1 ser/de ---
def serialize_json(value: PagerDutyAuthorizationConfig) -> dict:
    if "oAuthClientCredentials" in value:
        import aws_sdk_devops_agent.types.pager_duty_o_auth_client_credentials_config

        return {
            "oAuthClientCredentials": aws_sdk_devops_agent.types.pager_duty_o_auth_client_credentials_config.serialize_json(
                value["oAuthClientCredentials"]
            )
        }
    else:
        raise SerializationError("PagerDutyAuthorizationConfig: no variant present")


def deserialize_json(data: dict) -> PagerDutyAuthorizationConfig:
    if "oAuthClientCredentials" in data:
        import aws_sdk_devops_agent.types.pager_duty_o_auth_client_credentials_config

        return {
            "oAuthClientCredentials": aws_sdk_devops_agent.types.pager_duty_o_auth_client_credentials_config.deserialize_json(
                data["oAuthClientCredentials"]
            )
        }
    else:
        raise DeserializationError(
            "PagerDutyAuthorizationConfig: no recognized variant key"
        )
