"""Generated from Smithy shape ``com.amazonaws.opensearch#AutoTuneStatus``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_opensearch.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.auto_tune_state
    import aws_sdk_opensearch.types.boolean
    import aws_sdk_opensearch.types.string
    import aws_sdk_opensearch.types.u_int_value
    import aws_sdk_opensearch.types.update_timestamp


class AutoTuneStatus(TypedDict):
    creation_date: "aws_sdk_opensearch.types.update_timestamp.UpdateTimestamp"
    """<p>Date and time when Auto-Tune was enabled for the domain.</p>"""
    update_date: "aws_sdk_opensearch.types.update_timestamp.UpdateTimestamp"
    """<p>Date and time when the Auto-Tune options were last updated for the domain.</p>"""
    update_version: "aws_sdk_opensearch.types.u_int_value.UIntValue"
    """<p>The latest version of the Auto-Tune options.</p>"""
    state: "aws_sdk_opensearch.types.auto_tune_state.AutoTuneState"
    """<p>The current state of Auto-Tune on the domain.</p>"""
    error_message: NotRequired["aws_sdk_opensearch.types.string.String"]
    """<p>Any errors that occurred while enabling or disabling Auto-Tune.</p>"""
    pending_deletion: NotRequired["aws_sdk_opensearch.types.boolean.Boolean"]
    """<p>Indicates whether the domain is being deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutoTuneStatus) -> dict:
    out: dict = {}
    import aws_sdk_opensearch.types.update_timestamp

    out["CreationDate"] = aws_sdk_opensearch.types.update_timestamp.serialize_json(
        value["creation_date"]
    )
    import aws_sdk_opensearch.types.update_timestamp

    out["UpdateDate"] = aws_sdk_opensearch.types.update_timestamp.serialize_json(
        value["update_date"]
    )
    out["UpdateVersion"] = value.get("update_version", 0)
    import aws_sdk_opensearch.types.auto_tune_state

    out["State"] = aws_sdk_opensearch.types.auto_tune_state.serialize_json(
        value["state"]
    )
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    if "pending_deletion" in value:
        out["PendingDeletion"] = value["pending_deletion"]
    return out


def deserialize_json(data: dict) -> AutoTuneStatus:
    out: AutoTuneStatus = {}  # type: ignore[typeddict-item]
    if "CreationDate" in data:
        import aws_sdk_opensearch.types.update_timestamp

        out["creation_date"] = (
            aws_sdk_opensearch.types.update_timestamp.deserialize_json(
                data["CreationDate"]
            )
        )
    else:
        raise DeserializationError("AutoTuneStatus.creation_date required")
    if "UpdateDate" in data:
        import aws_sdk_opensearch.types.update_timestamp

        out["update_date"] = aws_sdk_opensearch.types.update_timestamp.deserialize_json(
            data["UpdateDate"]
        )
    else:
        raise DeserializationError("AutoTuneStatus.update_date required")
    if "UpdateVersion" in data:
        out["update_version"] = data["UpdateVersion"]
    else:
        out["update_version"] = 0
    if "State" in data:
        import aws_sdk_opensearch.types.auto_tune_state

        out["state"] = aws_sdk_opensearch.types.auto_tune_state.deserialize_json(
            data["State"]
        )
    else:
        raise DeserializationError("AutoTuneStatus.state required")
    if "ErrorMessage" in data:
        out["error_message"] = data["ErrorMessage"]
    if "PendingDeletion" in data:
        out["pending_deletion"] = data["PendingDeletion"]
    return out
