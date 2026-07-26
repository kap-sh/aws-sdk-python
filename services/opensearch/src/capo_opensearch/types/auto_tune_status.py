"""Generated from Smithy shape ``com.amazonaws.opensearch#AutoTuneStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_opensearch.errors import DeserializationError

if TYPE_CHECKING:
    import capo_opensearch.types.auto_tune_state
    import capo_opensearch.types.boolean
    import capo_opensearch.types.string
    import capo_opensearch.types.u_int_value
    import capo_opensearch.types.update_timestamp


class AutoTuneStatus(TypedDict, closed=True):
    creation_date: "capo_opensearch.types.update_timestamp.UpdateTimestamp"
    """<p>Date and time when Auto-Tune was enabled for the domain.</p>"""
    update_date: "capo_opensearch.types.update_timestamp.UpdateTimestamp"
    """<p>Date and time when the Auto-Tune options were last updated for the domain.</p>"""
    update_version: "capo_opensearch.types.u_int_value.UIntValue"
    """<p>The latest version of the Auto-Tune options.</p>"""
    state: "capo_opensearch.types.auto_tune_state.AutoTuneState"
    """<p>The current state of Auto-Tune on the domain.</p>"""
    error_message: NotRequired["capo_opensearch.types.string.String"]
    """<p>Any errors that occurred while enabling or disabling Auto-Tune.</p>"""
    pending_deletion: NotRequired["capo_opensearch.types.boolean.Boolean"]
    """<p>Indicates whether the domain is being deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutoTuneStatus) -> dict:
    out: dict = {}
    import capo_opensearch.types.update_timestamp

    out["CreationDate"] = capo_opensearch.types.update_timestamp.serialize_json(
        value["creation_date"]
    )
    import capo_opensearch.types.update_timestamp

    out["UpdateDate"] = capo_opensearch.types.update_timestamp.serialize_json(
        value["update_date"]
    )
    out["UpdateVersion"] = value.get("update_version", 0)
    import capo_opensearch.types.auto_tune_state

    out["State"] = capo_opensearch.types.auto_tune_state.serialize_json(value["state"])
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    if "pending_deletion" in value:
        out["PendingDeletion"] = value["pending_deletion"]
    return out


def deserialize_json(data: dict) -> AutoTuneStatus:
    out: AutoTuneStatus = {}  # type: ignore[typeddict-item]
    if "CreationDate" in data:
        import capo_opensearch.types.update_timestamp

        out["creation_date"] = capo_opensearch.types.update_timestamp.deserialize_json(
            data["CreationDate"]
        )
    else:
        raise DeserializationError("AutoTuneStatus.creation_date required")
    if "UpdateDate" in data:
        import capo_opensearch.types.update_timestamp

        out["update_date"] = capo_opensearch.types.update_timestamp.deserialize_json(
            data["UpdateDate"]
        )
    else:
        raise DeserializationError("AutoTuneStatus.update_date required")
    if "UpdateVersion" in data:
        out["update_version"] = data["UpdateVersion"]
    else:
        out["update_version"] = 0
    if "State" in data:
        import capo_opensearch.types.auto_tune_state

        out["state"] = capo_opensearch.types.auto_tune_state.deserialize_json(
            data["State"]
        )
    else:
        raise DeserializationError("AutoTuneStatus.state required")
    if "ErrorMessage" in data:
        out["error_message"] = data["ErrorMessage"]
    if "PendingDeletion" in data:
        out["pending_deletion"] = data["PendingDeletion"]
    return out
