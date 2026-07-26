"""Generated from Smithy shape ``com.amazonaws.mq#ConfigurationRevision``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mq.types.__integer
    import capo_mq.types.__string
    import capo_mq.types.__timestamp_iso8601


class ConfigurationRevision(TypedDict, closed=True):
    created: NotRequired["capo_mq.types.__timestamp_iso8601.__timestampIso8601"]
    """<p>Required. The date and time of the configuration revision.</p>"""
    description: NotRequired["capo_mq.types.__string.__string"]
    """<p>The description of the configuration revision.</p>"""
    revision: NotRequired["capo_mq.types.__integer.__integer"]
    """<p>Required. The revision number of the configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConfigurationRevision) -> dict:
    out: dict = {}
    if "created" in value:
        import capo_mq.types.__timestamp_iso8601

        out["created"] = capo_mq.types.__timestamp_iso8601.serialize_json(
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
        import capo_mq.types.__timestamp_iso8601

        out["created"] = capo_mq.types.__timestamp_iso8601.deserialize_json(
            data["created"]
        )
    if "description" in data:
        out["description"] = data["description"]
    if "revision" in data:
        out["revision"] = data["revision"]
    return out
