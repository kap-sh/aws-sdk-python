"""Generated from Smithy shape ``com.amazonaws.opensearch#AppConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.app_config_type
    import capo_opensearch.types.app_config_value


class AppConfig(TypedDict, closed=True):
    key: NotRequired["capo_opensearch.types.app_config_type.AppConfigType"]
    """<p>The configuration item to set, such as the admin role for the OpenSearch application.</p>"""
    value: NotRequired["capo_opensearch.types.app_config_value.AppConfigValue"]
    """<p>The value assigned to the configuration key, such as an IAM user ARN.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AppConfig) -> dict:
    out: dict = {}
    if "key" in value:
        import capo_opensearch.types.app_config_type

        out["key"] = capo_opensearch.types.app_config_type.serialize_json(value["key"])
    if "value" in value:
        out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> AppConfig:
    out: AppConfig = {}  # type: ignore[typeddict-item]
    if "key" in data:
        import capo_opensearch.types.app_config_type

        out["key"] = capo_opensearch.types.app_config_type.deserialize_json(data["key"])
    if "value" in data:
        out["value"] = data["value"]
    return out
