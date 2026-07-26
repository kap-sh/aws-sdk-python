"""Generated from Smithy shape ``com.amazonaws.migrationhubrefactorspaces#UrlEndpointConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_migration_hub_refactor_spaces.types.uri


class UrlEndpointConfig(TypedDict, closed=True):
    url: NotRequired["capo_migration_hub_refactor_spaces.types.uri.Uri"]
    """<p>The HTTP URL endpoint. </p>"""
    health_url: NotRequired["capo_migration_hub_refactor_spaces.types.uri.Uri"]
    """<p>The health check URL of the URL endpoint type. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UrlEndpointConfig) -> dict:
    out: dict = {}
    if "url" in value:
        out["Url"] = value["url"]
    if "health_url" in value:
        out["HealthUrl"] = value["health_url"]
    return out


def deserialize_json(data: dict) -> UrlEndpointConfig:
    out: UrlEndpointConfig = {}  # type: ignore[typeddict-item]
    if "Url" in data:
        out["url"] = data["Url"]
    if "HealthUrl" in data:
        out["health_url"] = data["HealthUrl"]
    return out
