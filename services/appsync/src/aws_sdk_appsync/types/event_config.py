"""Generated from Smithy shape ``com.amazonaws.appsync#EventConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_appsync.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_appsync.types.auth_modes
    import aws_sdk_appsync.types.auth_providers
    import aws_sdk_appsync.types.event_log_config


class EventConfig(TypedDict):
    auth_providers: "aws_sdk_appsync.types.auth_providers.AuthProviders"
    """<p>A list of authorization providers.</p>"""
    connection_auth_modes: "aws_sdk_appsync.types.auth_modes.AuthModes"
    """<p>A list of valid authorization modes for the Event API connections.</p>"""
    default_publish_auth_modes: "aws_sdk_appsync.types.auth_modes.AuthModes"
    """<p>A list of valid authorization modes for the Event API publishing.</p>"""
    default_subscribe_auth_modes: "aws_sdk_appsync.types.auth_modes.AuthModes"
    """<p>A list of valid authorization modes for the Event API subscriptions.</p>"""
    log_config: NotRequired["aws_sdk_appsync.types.event_log_config.EventLogConfig"]
    """<p>The CloudWatch Logs configuration for the Event API.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EventConfig) -> dict:
    out: dict = {}
    import aws_sdk_appsync.types.auth_providers

    out["authProviders"] = aws_sdk_appsync.types.auth_providers.serialize_json(
        value["auth_providers"]
    )
    import aws_sdk_appsync.types.auth_modes

    out["connectionAuthModes"] = aws_sdk_appsync.types.auth_modes.serialize_json(
        value["connection_auth_modes"]
    )
    import aws_sdk_appsync.types.auth_modes

    out["defaultPublishAuthModes"] = aws_sdk_appsync.types.auth_modes.serialize_json(
        value["default_publish_auth_modes"]
    )
    import aws_sdk_appsync.types.auth_modes

    out["defaultSubscribeAuthModes"] = aws_sdk_appsync.types.auth_modes.serialize_json(
        value["default_subscribe_auth_modes"]
    )
    if "log_config" in value:
        import aws_sdk_appsync.types.event_log_config

        out["logConfig"] = aws_sdk_appsync.types.event_log_config.serialize_json(
            value["log_config"]
        )
    return out


def deserialize_json(data: dict) -> EventConfig:
    out: EventConfig = {}  # type: ignore[typeddict-item]
    if "authProviders" in data:
        import aws_sdk_appsync.types.auth_providers

        out["auth_providers"] = aws_sdk_appsync.types.auth_providers.deserialize_json(
            data["authProviders"]
        )
    else:
        raise DeserializationError("EventConfig.auth_providers required")
    if "connectionAuthModes" in data:
        import aws_sdk_appsync.types.auth_modes

        out["connection_auth_modes"] = (
            aws_sdk_appsync.types.auth_modes.deserialize_json(
                data["connectionAuthModes"]
            )
        )
    else:
        raise DeserializationError("EventConfig.connection_auth_modes required")
    if "defaultPublishAuthModes" in data:
        import aws_sdk_appsync.types.auth_modes

        out["default_publish_auth_modes"] = (
            aws_sdk_appsync.types.auth_modes.deserialize_json(
                data["defaultPublishAuthModes"]
            )
        )
    else:
        raise DeserializationError("EventConfig.default_publish_auth_modes required")
    if "defaultSubscribeAuthModes" in data:
        import aws_sdk_appsync.types.auth_modes

        out["default_subscribe_auth_modes"] = (
            aws_sdk_appsync.types.auth_modes.deserialize_json(
                data["defaultSubscribeAuthModes"]
            )
        )
    else:
        raise DeserializationError("EventConfig.default_subscribe_auth_modes required")
    if "logConfig" in data:
        import aws_sdk_appsync.types.event_log_config

        out["log_config"] = aws_sdk_appsync.types.event_log_config.deserialize_json(
            data["logConfig"]
        )
    return out
