"""Generated from Smithy shape ``com.amazonaws.mq#ConfigurationRevision``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mq.types.__integer
    import aws_sdk_mq.types.__string
    import aws_sdk_mq.types.__timestamp_iso8601


class ConfigurationRevision(TypedDict):
    created: NotRequired["aws_sdk_mq.types.__timestamp_iso8601.__timestampIso8601"]
    """<p>Required. The date and time of the configuration revision.</p>"""
    description: NotRequired["aws_sdk_mq.types.__string.__string"]
    """<p>The description of the configuration revision.</p>"""
    revision: NotRequired["aws_sdk_mq.types.__integer.__integer"]
    """<p>Required. The revision number of the configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConfigurationRevision) -> dict:
    out: dict = {}
    if "created" in value:
        import aws_sdk_mq.types.__timestamp_iso8601

        out["created"] = aws_sdk_mq.types.__timestamp_iso8601.serialize_json(
            value["created"]
        )
    if "description" in value:
        out["description"] = value["description"]
    if "revision" in value:
        out["revision"] = value["revision"]
    return out


def deserialize_json(data: dict) -> ConfigurationRevision:
    out: ConfigurationRevision = {}  # type: ignore[typeddict-item]
    if "created" in data:
        import aws_sdk_mq.types.__timestamp_iso8601

        out["created"] = aws_sdk_mq.types.__timestamp_iso8601.deserialize_json(
            data["created"]
        )
    if "description" in data:
        out["description"] = data["description"]
    if "revision" in data:
        out["revision"] = data["revision"]
    return out
