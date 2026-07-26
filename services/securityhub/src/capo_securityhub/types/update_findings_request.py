"""Generated from Smithy shape ``com.amazonaws.securityhub#UpdateFindingsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.aws_security_finding_filters
    import capo_securityhub.types.note_update
    import capo_securityhub.types.record_state


class UpdateFindingsRequest(TypedDict, closed=True):
    filters: NotRequired[
        "capo_securityhub.types.aws_security_finding_filters.AwsSecurityFindingFilters"
    ]
    """<p>A collection of attributes that specify which findings you want to update.</p>"""
    note: NotRequired["capo_securityhub.types.note_update.NoteUpdate"]
    """<p>The updated note for the finding.</p>"""
    record_state: NotRequired["capo_securityhub.types.record_state.RecordState"]
    """<p>The updated record state for the finding.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateFindingsRequest) -> dict:
    out: dict = {}
    if "filters" in value:
        import capo_securityhub.types.aws_security_finding_filters

        out["Filters"] = (
            capo_securityhub.types.aws_security_finding_filters.serialize_json(
                value["filters"]
            )
        )
    if "note" in value:
        import capo_securityhub.types.note_update

        out["Note"] = capo_securityhub.types.note_update.serialize_json(value["note"])
    if "record_state" in value:
        import capo_securityhub.types.record_state

        out["RecordState"] = capo_securityhub.types.record_state.serialize_json(
            value["record_state"]
        )
    return out


def deserialize_json(data: dict) -> UpdateFindingsRequest:
    out: UpdateFindingsRequest = {}  # type: ignore[typeddict-item]
    if "Filters" in data:
        import capo_securityhub.types.aws_security_finding_filters

        out["filters"] = (
            capo_securityhub.types.aws_security_finding_filters.deserialize_json(
                data["Filters"]
            )
        )
    if "Note" in data:
        import capo_securityhub.types.note_update

        out["note"] = capo_securityhub.types.note_update.deserialize_json(data["Note"])
    if "RecordState" in data:
        import capo_securityhub.types.record_state

        out["record_state"] = capo_securityhub.types.record_state.deserialize_json(
            data["RecordState"]
        )
    return out
