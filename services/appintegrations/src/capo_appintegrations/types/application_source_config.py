"""Generated from Smithy shape ``com.amazonaws.appintegrations#ApplicationSourceConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appintegrations.types.external_url_config


class ApplicationSourceConfig(TypedDict, closed=True):
    external_url_config: NotRequired[
        "capo_appintegrations.types.external_url_config.ExternalUrlConfig"
    ]
    """<p>The external URL source for the application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ApplicationSourceConfig) -> dict:
    out: dict = {}
    if "external_url_config" in value:
        import capo_appintegrations.types.external_url_config

        out["ExternalUrlConfig"] = (
            capo_appintegrations.types.external_url_config.serialize_json(
                value["external_url_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> ApplicationSourceConfig:
    out: ApplicationSourceConfig = {}  # type: ignore[typeddict-item]
    if "ExternalUrlConfig" in data:
        import capo_appintegrations.types.external_url_config

        out["external_url_config"] = (
            capo_appintegrations.types.external_url_config.deserialize_json(
                data["ExternalUrlConfig"]
            )
        )
    return out
