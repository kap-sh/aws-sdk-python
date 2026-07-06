"""Generated from Smithy shape ``com.amazonaws.quicksight#FolderMember``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.member_type
    import aws_sdk_quicksight.types.restrictive_resource_id


class FolderMember(TypedDict, closed=True):
    member_id: NotRequired[
        "aws_sdk_quicksight.types.restrictive_resource_id.RestrictiveResourceId"
    ]
    """<p>The ID of an asset in the folder.</p>"""
    member_type: NotRequired["aws_sdk_quicksight.types.member_type.MemberType"]
    """<p>The type of asset that it is.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FolderMember) -> dict:
    out: dict = {}
    if "member_id" in value:
        out["MemberId"] = value["member_id"]
    if "member_type" in value:
        import aws_sdk_quicksight.types.member_type

        out["MemberType"] = aws_sdk_quicksight.types.member_type.serialize_json(
            value["member_type"]
        )
    return out


def deserialize_json(data: dict) -> FolderMember:
    out: FolderMember = {}  # type: ignore[typeddict-item]
    if "MemberId" in data:
        out["member_id"] = data["MemberId"]
    if "MemberType" in data:
        import aws_sdk_quicksight.types.member_type

        out["member_type"] = aws_sdk_quicksight.types.member_type.deserialize_json(
            data["MemberType"]
        )
    return out
