"""Generated from Smithy shape ``com.amazonaws.connectcampaigns#DialerConfig``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_connectcampaigns.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_connectcampaigns.types.agentless_dialer_config
    import aws_sdk_connectcampaigns.types.predictive_dialer_config
    import aws_sdk_connectcampaigns.types.progressive_dialer_config


class _DialerConfig_progressiveDialerConfig(TypedDict, closed=True):
    progressiveDialerConfig: "aws_sdk_connectcampaigns.types.progressive_dialer_config.ProgressiveDialerConfig"


class _DialerConfig_predictiveDialerConfig(TypedDict, closed=True):
    predictiveDialerConfig: (
        "aws_sdk_connectcampaigns.types.predictive_dialer_config.PredictiveDialerConfig"
    )


class _DialerConfig_agentlessDialerConfig(TypedDict, closed=True):
    agentlessDialerConfig: (
        "aws_sdk_connectcampaigns.types.agentless_dialer_config.AgentlessDialerConfig"
    )


DialerConfig: TypeAlias = (
    _DialerConfig_progressiveDialerConfig
    | _DialerConfig_predictiveDialerConfig
    | _DialerConfig_agentlessDialerConfig
)


# --- restJson1 ser/de ---
def serialize_json(value: DialerConfig) -> dict:
    if "progressiveDialerConfig" in value:
        import aws_sdk_connectcampaigns.types.progressive_dialer_config

        return {
            "progressiveDialerConfig": aws_sdk_connectcampaigns.types.progressive_dialer_config.serialize_json(
                value["progressiveDialerConfig"]
            )
        }
    elif "predictiveDialerConfig" in value:
        import aws_sdk_connectcampaigns.types.predictive_dialer_config

        return {
            "predictiveDialerConfig": aws_sdk_connectcampaigns.types.predictive_dialer_config.serialize_json(
                value["predictiveDialerConfig"]
            )
        }
    elif "agentlessDialerConfig" in value:
        import aws_sdk_connectcampaigns.types.agentless_dialer_config

        return {
            "agentlessDialerConfig": aws_sdk_connectcampaigns.types.agentless_dialer_config.serialize_json(
                value["agentlessDialerConfig"]
            )
        }
    else:
        raise SerializationError("DialerConfig: no variant present")


def deserialize_json(data: dict) -> DialerConfig:
    if "progressiveDialerConfig" in data:
        import aws_sdk_connectcampaigns.types.progressive_dialer_config

        return {
            "progressiveDialerConfig": aws_sdk_connectcampaigns.types.progressive_dialer_config.deserialize_json(
                data["progressiveDialerConfig"]
            )
        }
    elif "predictiveDialerConfig" in data:
        import aws_sdk_connectcampaigns.types.predictive_dialer_config

        return {
            "predictiveDialerConfig": aws_sdk_connectcampaigns.types.predictive_dialer_config.deserialize_json(
                data["predictiveDialerConfig"]
            )
        }
    elif "agentlessDialerConfig" in data:
        import aws_sdk_connectcampaigns.types.agentless_dialer_config

        return {
            "agentlessDialerConfig": aws_sdk_connectcampaigns.types.agentless_dialer_config.deserialize_json(
                data["agentlessDialerConfig"]
            )
        }
    else:
        raise DeserializationError("DialerConfig: no recognized variant key")
