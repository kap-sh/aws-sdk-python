"""Generated from Smithy shape ``com.amazonaws.opensearch#AppConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.app_config_type
    import aws_sdk_opensearch.types.app_config_value


class AppConfig(TypedDict):
    key: NotRequired["aws_sdk_opensearch.types.app_config_type.AppConfigType"]
    """<p>The configuration item to set, such as the admin role for the OpenSearch application.</p>"""
    value: NotRequired["aws_sdk_opensearch.types.app_config_value.AppConfigValue"]
    """<p>The value assigned to the configuration key, such as an IAM user ARN.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AppConfig) -> dict:
    out: dict = {}
    if "key" in value:
        import aws_sdk_opensearch.types.app_config_type

        out["key"] = aws_sdk_opensearch.types.app_config_type.serialize_json(
            value["key"]
        )
    if "value" in value:
        out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> AppConfig:
    out: AppConfig = {}  # type: ignore[typeddict-item]
    if "key" in data:
        import aws_sdk_opensearch.types.app_config_type

        out["key"] = aws_sdk_opensearch.types.app_config_type.deserialize_json(
            data["key"]
        )
    if "value" in data:
        out["value"] = data["value"]
    return out
