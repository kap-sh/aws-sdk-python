"""Generated from Smithy shape ``com.amazonaws.datazone#ProjectMember``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.member_details
    import aws_sdk_datazone.types.user_designation


class ProjectMember(TypedDict, closed=True):
    member_details: "aws_sdk_datazone.types.member_details.MemberDetails"
    """<p>The membership details of a project member.</p>"""
    designation: "aws_sdk_datazone.types.user_designation.UserDesignation"
    """<p>The designated role of a project member.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProjectMember) -> dict:
    out: dict = {}
    import aws_sdk_datazone.types.member_details

    out["memberDetails"] = aws_sdk_datazone.types.member_details.serialize_json(
        value["member_details"]
    )
    import aws_sdk_datazone.types.user_designation

    out["designation"] = aws_sdk_datazone.types.user_designation.serialize_json(
        value["designation"]
    )
    return out


def deserialize_json(data: dict) -> ProjectMember:
    out: ProjectMember = {}  # type: ignore[typeddict-item]
    if "memberDetails" in data:
        import aws_sdk_datazone.types.member_details

        out["member_details"] = aws_sdk_datazone.types.member_details.deserialize_json(
            data["memberDetails"]
        )
    else:
        raise DeserializationError("ProjectMember.member_details required")
    if "designation" in data:
        import aws_sdk_datazone.types.user_designation

        out["designation"] = aws_sdk_datazone.types.user_designation.deserialize_json(
            data["designation"]
        )
    else:
        raise DeserializationError("ProjectMember.designation required")
    return out
