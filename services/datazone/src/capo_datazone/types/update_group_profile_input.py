"""Generated from Smithy shape ``com.amazonaws.datazone#UpdateGroupProfileInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import capo_datazone.types.domain_id
    import capo_datazone.types.group_identifier
    import capo_datazone.types.group_profile_status


class UpdateGroupProfileInput(TypedDict, closed=True):
    domain_identifier: "capo_datazone.types.domain_id.DomainId"
    """<p>The identifier of the Amazon DataZone domain in which a group profile is updated.</p>"""
    group_identifier: "capo_datazone.types.group_identifier.GroupIdentifier"
    """<p>The identifier of the group profile that is updated.</p>"""
    status: "capo_datazone.types.group_profile_status.GroupProfileStatus"
    """<p>The status of the group profile that is updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateGroupProfileInput) -> dict:
    out: dict = {}
    import capo_datazone.types.group_profile_status

    out["status"] = capo_datazone.types.group_profile_status.serialize_json(
        value["status"]
    )
    return out


def deserialize_json(data: dict) -> UpdateGroupProfileInput:
    out: UpdateGroupProfileInput = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import capo_datazone.types.group_profile_status

        out["status"] = capo_datazone.types.group_profile_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("UpdateGroupProfileInput.status required")
    return out
