"""Generated from Smithy shape ``com.amazonaws.datazone#DeleteProjectMembershipInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import capo_datazone.types.domain_id
    import capo_datazone.types.member
    import capo_datazone.types.project_id


class DeleteProjectMembershipInput(TypedDict, closed=True):
    domain_identifier: "capo_datazone.types.domain_id.DomainId"
    """<p>The ID of the Amazon DataZone domain where project membership is deleted.</p>"""
    project_identifier: "capo_datazone.types.project_id.ProjectId"
    """<p>The ID of the Amazon DataZone project the membership to which is deleted.</p>"""
    member: "capo_datazone.types.member.Member"
    """<p>The project member whose project membership is deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteProjectMembershipInput) -> dict:
    out: dict = {}
    import capo_datazone.types.member

    out["member"] = capo_datazone.types.member.serialize_json(value["member"])
    return out


def deserialize_json(data: dict) -> DeleteProjectMembershipInput:
    out: DeleteProjectMembershipInput = {}  # type: ignore[typeddict-item]
    if "member" in data:
        import capo_datazone.types.member

        out["member"] = capo_datazone.types.member.deserialize_json(data["member"])
    else:
        raise DeserializationError("DeleteProjectMembershipInput.member required")
    return out
