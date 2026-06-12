"""Generated from Smithy shape ``com.amazonaws.appconfig#Configuration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appconfig.types.blob
    import aws_sdk_appconfig.types.string
    import aws_sdk_appconfig.types.version


class Configuration(TypedDict):
    content: NotRequired["aws_sdk_appconfig.types.blob.Blob"]
    """<p>The content of the configuration or the configuration data.</p> <important> <p>The <code>Content</code> attribute only contains data if the system finds new or updated configuration data. If there is no new or updated data and <code>ClientConfigurationVersion</code> matches the version of the current configuration, AppConfig returns a <code>204 No Content</code> HTTP response code and the <code>Content</code> value will be empty.</p> </important>"""
    configuration_version: NotRequired["aws_sdk_appconfig.types.version.Version"]
    """<p>The configuration version.</p>"""
    content_type: NotRequired["aws_sdk_appconfig.types.string.String"]
    """<p>A standard MIME type describing the format of the configuration content. For more information, see <a href=\"http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.17\">Content-Type</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Configuration) -> dict:
    out: dict = {}
    if "content" in value:
        import aws_sdk_appconfig.types.blob

        out["Content"] = aws_sdk_appconfig.types.blob.serialize_json(value["content"])
    return out


def deserialize_json(data: dict) -> Configuration:
    out: Configuration = {}  # type: ignore[typeddict-item]
    if "Content" in data:
        import aws_sdk_appconfig.types.blob

        out["content"] = aws_sdk_appconfig.types.blob.deserialize_json(data["Content"])
    return out
