"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#WorkerConfigurationRevisionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafkaconnect.types.__long
    import capo_kafkaconnect.types.__string
    import capo_kafkaconnect.types.__timestamp_iso8601


class WorkerConfigurationRevisionSummary(TypedDict, closed=True):
    creation_time: NotRequired[
        "capo_kafkaconnect.types.__timestamp_iso8601.__timestampIso8601"
    ]
    """<p>The time that a worker configuration revision was created.</p>"""
    description: NotRequired["capo_kafkaconnect.types.__string.__string"]
    """<p>The description of a worker configuration revision.</p>"""
    revision: "capo_kafkaconnect.types.__long.__long"
    """<p>The revision of a worker configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WorkerConfigurationRevisionSummary) -> dict:
    out: dict = {}
    if "creation_time" in value:
        import capo_kafkaconnect.types.__timestamp_iso8601

        out["creationTime"] = (
            capo_kafkaconnect.types.__timestamp_iso8601.serialize_json(
                value["creation_time"]
            )
        )
    if "description" in value:
        out["description"] = value["description"]
    out["revision"] = value.get("revision", 0)
    return out


def deserialize_json(data: dict) -> WorkerConfigurationRevisionSummary:
    out: WorkerConfigurationRevisionSummary = {}  # type: ignore[typeddict-item]
    if "creationTime" in data:
        import capo_kafkaconnect.types.__timestamp_iso8601

        out["creation_time"] = (
            capo_kafkaconnect.types.__timestamp_iso8601.deserialize_json(
                data["creationTime"]
            )
        )
    if "description" in data:
        out["description"] = data["description"]
    if "revision" in data:
        out["revision"] = data["revision"]
    else:
        out["revision"] = 0
    return out
