"""Generated from Smithy shape ``com.amazonaws.datazone#DeleteProjectMembershipInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.member
    import aws_sdk_datazone.types.project_id


class DeleteProjectMembershipInput(TypedDict, closed=True):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The ID of the Amazon DataZone domain where project membership is deleted.</p>"""
    project_identifier: "aws_sdk_datazone.types.project_id.ProjectId"
    """<p>The ID of the Amazon DataZone project the membership to which is deleted.</p>"""
    member: "aws_sdk_datazone.types.member.Member"
    """<p>The project member whose project membership is deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteProjectMembershipInput) -> dict:
    out: dict = {}
    import aws_sdk_datazone.types.member

    out["member"] = aws_sdk_datazone.types.member.serialize_json(value["member"])
    return out


def deserialize_json(data: dict) -> DeleteProjectMembershipInput:
    out: DeleteProjectMembershipInput = {}  # type: ignore[typeddict-item]
    if "member" in data:
        import aws_sdk_datazone.types.member

        out["member"] = aws_sdk_datazone.types.member.deserialize_json(data["member"])
    else:
        raise DeserializationError("DeleteProjectMembershipInput.member required")
    return out
