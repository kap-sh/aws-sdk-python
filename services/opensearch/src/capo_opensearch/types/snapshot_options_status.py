"""Generated from Smithy shape ``com.amazonaws.opensearch#SnapshotOptionsStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_opensearch.errors import DeserializationError

if TYPE_CHECKING:
    import capo_opensearch.types.option_status
    import capo_opensearch.types.snapshot_options


class SnapshotOptionsStatus(TypedDict, closed=True):
    options: "capo_opensearch.types.snapshot_options.SnapshotOptions"
    """<p>The daily snapshot options specified for the domain.</p>"""
    status: "capo_opensearch.types.option_status.OptionStatus"
    """<p>The status of a daily automated snapshot.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SnapshotOptionsStatus) -> dict:
    out: dict = {}
    import capo_opensearch.types.snapshot_options

    out["Options"] = capo_opensearch.types.snapshot_options.serialize_json(
        value["options"]
    )
    import capo_opensearch.types.option_status

    out["Status"] = capo_opensearch.types.option_status.serialize_json(value["status"])
    return out


def deserialize_json(data: dict) -> SnapshotOptionsStatus:
    out: SnapshotOptionsStatus = {}  # type: ignore[typeddict-item]
    if "Options" in data:
        import capo_opensearch.types.snapshot_options

        out["options"] = capo_opensearch.types.snapshot_options.deserialize_json(
            data["Options"]
        )
    else:
        raise DeserializationError("SnapshotOptionsStatus.options required")
    if "Status" in data:
        import capo_opensearch.types.option_status

        out["status"] = capo_opensearch.types.option_status.deserialize_json(
            data["Status"]
        )
    else:
        raise DeserializationError("SnapshotOptionsStatus.status required")
    return out
