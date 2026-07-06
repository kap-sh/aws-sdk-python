"""Generated from Smithy shape ``com.amazonaws.datazone#CreateProjectMembershipInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.member
    import aws_sdk_datazone.types.project_id
    import aws_sdk_datazone.types.user_designation


class CreateProjectMembershipInput(TypedDict, closed=True):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The ID of the Amazon DataZone domain in which project membership is created.</p>"""
    project_identifier: "aws_sdk_datazone.types.project_id.ProjectId"
    """<p>The ID of the project for which this project membership was created.</p>"""
    member: "aws_sdk_datazone.types.member.Member"
    """<p>The project member whose project membership was created.</p>"""
    designation: "aws_sdk_datazone.types.user_designation.UserDesignation"
    """<p>The designation of the project membership.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateProjectMembershipInput) -> dict:
    out: dict = {}
    import aws_sdk_datazone.types.member

    out["member"] = aws_sdk_datazone.types.member.serialize_json(value["member"])
    import aws_sdk_datazone.types.user_designation

    out["designation"] = aws_sdk_datazone.types.user_designation.serialize_json(
        value["designation"]
    )
    return out


def deserialize_json(data: dict) -> CreateProjectMembershipInput:
    out: CreateProjectMembershipInput = {}  # type: ignore[typeddict-item]
    if "member" in data:
        import aws_sdk_datazone.types.member

        out["member"] = aws_sdk_datazone.types.member.deserialize_json(data["member"])
    else:
        raise DeserializationError("CreateProjectMembershipInput.member required")
    if "designation" in data:
        import aws_sdk_datazone.types.user_designation

        out["designation"] = aws_sdk_datazone.types.user_designation.deserialize_json(
            data["designation"]
        )
    else:
        raise DeserializationError("CreateProjectMembershipInput.designation required")
    return out
