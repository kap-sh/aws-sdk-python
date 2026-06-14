"""Generated from Smithy shape ``com.amazonaws.datazone#ProjectMembershipAssignment``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.member
    import aws_sdk_datazone.types.user_designation


class ProjectMembershipAssignment(TypedDict):
    member: "aws_sdk_datazone.types.member.Member"
    """<p>The details about a project member.</p>"""
    designation: "aws_sdk_datazone.types.user_designation.UserDesignation"
    """<p>The designation of the project membership.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProjectMembershipAssignment) -> dict:
    out: dict = {}
    import aws_sdk_datazone.types.member

    out["member"] = aws_sdk_datazone.types.member.serialize_json(value["member"])
    import aws_sdk_datazone.types.user_designation

    out["designation"] = aws_sdk_datazone.types.user_designation.serialize_json(
        value["designation"]
    )
    return out


def deserialize_json(data: dict) -> ProjectMembershipAssignment:
    out: ProjectMembershipAssignment = {}  # type: ignore[typeddict-item]
    if "member" in data:
        import aws_sdk_datazone.types.member

        out["member"] = aws_sdk_datazone.types.member.deserialize_json(data["member"])
    else:
        raise DeserializationError("ProjectMembershipAssignment.member required")
    if "designation" in data:
        import aws_sdk_datazone.types.user_designation

        out["designation"] = aws_sdk_datazone.types.user_designation.deserialize_json(
            data["designation"]
        )
    else:
        raise DeserializationError("ProjectMembershipAssignment.designation required")
    return out
