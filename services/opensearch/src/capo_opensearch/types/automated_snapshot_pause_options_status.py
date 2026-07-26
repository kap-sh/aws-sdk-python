"""Generated from Smithy shape ``com.amazonaws.opensearch#AutomatedSnapshotPauseOptionsStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_opensearch.errors import DeserializationError

if TYPE_CHECKING:
    import capo_opensearch.types.automated_snapshot_pause_options
    import capo_opensearch.types.option_status


class AutomatedSnapshotPauseOptionsStatus(TypedDict, closed=True):
    options: "capo_opensearch.types.automated_snapshot_pause_options.AutomatedSnapshotPauseOptions"
    """<p>Automated snapshot pause options for the domain.</p>"""
    status: "capo_opensearch.types.option_status.OptionStatus"
    """<p>The current status of the automated snapshot pause options for the domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedSnapshotPauseOptionsStatus) -> dict:
    out: dict = {}
    import capo_opensearch.types.automated_snapshot_pause_options

    out["Options"] = (
        capo_opensearch.types.automated_snapshot_pause_options.serialize_json(
            value["options"]
        )
    )
    import capo_opensearch.types.option_status

    out["Status"] = capo_opensearch.types.option_status.serialize_json(value["status"])
    return out


def deserialize_json(data: dict) -> AutomatedSnapshotPauseOptionsStatus:
    out: AutomatedSnapshotPauseOptionsStatus = {}  # type: ignore[typeddict-item]
    if "Options" in data:
        import capo_opensearch.types.automated_snapshot_pause_options

        out["options"] = (
            capo_opensearch.types.automated_snapshot_pause_options.deserialize_json(
                data["Options"]
            )
        )
    else:
        raise DeserializationError(
            "AutomatedSnapshotPauseOptionsStatus.options required"
        )
    if "Status" in data:
        import capo_opensearch.types.option_status

        out["status"] = capo_opensearch.types.option_status.deserialize_json(
            data["Status"]
        )
    else:
        raise DeserializationError(
            "AutomatedSnapshotPauseOptionsStatus.status required"
        )
    return out
