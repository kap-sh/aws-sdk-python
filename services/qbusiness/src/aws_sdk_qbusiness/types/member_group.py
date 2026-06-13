"""Generated from Smithy shape ``com.amazonaws.qbusiness#MemberGroup``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_qbusiness.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.group_name
    import aws_sdk_qbusiness.types.membership_type


class MemberGroup(TypedDict):
    group_name: "aws_sdk_qbusiness.types.group_name.GroupName"
    """<p>The name of the sub group.</p>"""
    type: NotRequired["aws_sdk_qbusiness.types.membership_type.MembershipType"]
    """<p>The type of the sub group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MemberGroup) -> dict:
    out: dict = {}
    out["groupName"] = value["group_name"]
    if "type" in value:
        import aws_sdk_qbusiness.types.membership_type

        out["type"] = aws_sdk_qbusiness.types.membership_type.serialize_json(
            value["type"]
        )
    return out


def deserialize_json(data: dict) -> MemberGroup:
    out: MemberGroup = {}  # type: ignore[typeddict-item]
    if "groupName" in data:
        out["group_name"] = data["groupName"]
    else:
        raise DeserializationError("MemberGroup.group_name required")
    if "type" in data:
        import aws_sdk_qbusiness.types.membership_type

        out["type"] = aws_sdk_qbusiness.types.membership_type.deserialize_json(
            data["type"]
        )
    return out
