"""Generated from Smithy shape ``com.amazonaws.appsync#HttpDataSourceConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appsync.types.authorization_config
    import aws_sdk_appsync.types.string


class HttpDataSourceConfig(TypedDict):
    endpoint: NotRequired["aws_sdk_appsync.types.string.String"]
    """<p>The HTTP URL endpoint. You can specify either the domain name or IP, and port combination, and the URL scheme must be HTTP or HTTPS. If you don't specify the port, AppSync uses the default port 80 for the HTTP endpoint and port 443 for HTTPS endpoints.</p>"""
    authorization_config: NotRequired[
        "aws_sdk_appsync.types.authorization_config.AuthorizationConfig"
    ]
    """<p>The authorization configuration in case the HTTP endpoint requires authorization.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HttpDataSourceConfig) -> dict:
    out: dict = {}
    if "endpoint" in value:
        out["endpoint"] = value["endpoint"]
    if "authorization_config" in value:
        import aws_sdk_appsync.types.authorization_config

        out["authorizationConfig"] = (
            aws_sdk_appsync.types.authorization_config.serialize_json(
                value["authorization_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> HttpDataSourceConfig:
    out: HttpDataSourceConfig = {}  # type: ignore[typeddict-item]
    if "endpoint" in data:
        out["endpoint"] = data["endpoint"]
    if "authorizationConfig" in data:
        import aws_sdk_appsync.types.authorization_config

        out["authorization_config"] = (
            aws_sdk_appsync.types.authorization_config.deserialize_json(
                data["authorizationConfig"]
            )
        )
    return out
