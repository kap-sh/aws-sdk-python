"""Generated from Smithy shape ``com.amazonaws.kafka#ConfigurationRevision``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafka.types.__long
    import capo_kafka.types.__string
    import capo_kafka.types.__timestamp_iso8601


class ConfigurationRevision(TypedDict, closed=True):
    creation_time: NotRequired[
        "capo_kafka.types.__timestamp_iso8601.__timestampIso8601"
    ]
    """<p>The time when the configuration revision was created.</p>"""
    description: NotRequired["capo_kafka.types.__string.__string"]
    """<p>The description of the configuration revision.</p>"""
    revision: NotRequired["capo_kafka.types.__long.__long"]
    """<p>The revision number.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConfigurationRevision) -> dict:
    out: dict = {}
    if "creation_time" in value:
        import capo_kafka.types.__timestamp_iso8601

        out["creationTime"] = capo_kafka.types.__timestamp_iso8601.serialize_json(
            value["creation_time"]
        )
    if "description" in value:
        out["description"] = value["description"]
    if "revision" in value:
        out["revision"] = value["revision"]
    return out


def deserialize_json(data: dict) -> ConfigurationRevision:
    out: ConfigurationRevision = {}  # type: ignore[typeddict-item]
    if "creationTime" in data:
        import capo_kafka.types.__timestamp_iso8601

        out["creation_time"] = capo_kafka.types.__timestamp_iso8601.deserialize_json(
            data["creationTime"]
        )
    if "description" in data:
        out["description"] = data["description"]
    if "revision" in data:
        out["revision"] = data["revision"]
    return out
