"""Generated from Smithy shape ``com.amazonaws.datazone#ProjectMembershipAssignment``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import capo_datazone.types.member
    import capo_datazone.types.user_designation


class ProjectMembershipAssignment(TypedDict, closed=True):
    member: "capo_datazone.types.member.Member"
    """<p>The details about a project member.</p>"""
    designation: "capo_datazone.types.user_designation.UserDesignation"
    """<p>The designation of the project membership.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProjectMembershipAssignment) -> dict:
    out: dict = {}
    import capo_datazone.types.member

    out["member"] = capo_datazone.types.member.serialize_json(value["member"])
    import capo_datazone.types.user_designation

    out["designation"] = capo_datazone.types.user_designation.serialize_json(
        value["designation"]
    )
    return out


def deserialize_json(data: dict) -> ProjectMembershipAssignment:
    out: ProjectMembershipAssignment = {}  # type: ignore[typeddict-item]
    if "member" in data:
        import capo_datazone.types.member

        out["member"] = capo_datazone.types.member.deserialize_json(data["member"])
    else:
        raise DeserializationError("ProjectMembershipAssignment.member required")
    if "designation" in data:
        import capo_datazone.types.user_designation

        out["designation"] = capo_datazone.types.user_designation.deserialize_json(
            data["designation"]
        )
    else:
        raise DeserializationError("ProjectMembershipAssignment.designation required")
    return out
