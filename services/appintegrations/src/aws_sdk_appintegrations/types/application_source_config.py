"""Generated from Smithy shape ``com.amazonaws.appintegrations#ApplicationSourceConfig``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_appintegrations.types.external_url_config

class ApplicationSourceConfig(TypedDict):
    external_url_config: NotRequired["aws_sdk_appintegrations.types.external_url_config.ExternalUrlConfig"]
    """<p>The external URL source for the application.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: ApplicationSourceConfig) -> dict:
    out: dict = {}
    if "external_url_config" in value:
        import aws_sdk_appintegrations.types.external_url_config
        out["ExternalUrlConfig"] = aws_sdk_appintegrations.types.external_url_config.serialize_json(value["external_url_config"])
    return out


def deserialize_json(data: dict) -> ApplicationSourceConfig:
    out: ApplicationSourceConfig = {}  # type: ignore[typeddict-item]
    if "ExternalUrlConfig" in data:
        import aws_sdk_appintegrations.types.external_url_config
        out["external_url_config"] = aws_sdk_appintegrations.types.external_url_config.deserialize_json(data["ExternalUrlConfig"])
    return out