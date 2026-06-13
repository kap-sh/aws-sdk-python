"""Generated from Smithy shape ``com.amazonaws.qbusiness#AssociatedGroup``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.group_name
    import aws_sdk_qbusiness.types.membership_type


class AssociatedGroup(TypedDict):
    name: NotRequired["aws_sdk_qbusiness.types.group_name.GroupName"]
    """<p>The name of the group associated with the user. This is used to identify the group in access control decisions.</p>"""
    type: NotRequired["aws_sdk_qbusiness.types.membership_type.MembershipType"]
    """<p>The type of the associated group. This indicates the scope of the group's applicability.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociatedGroup) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "type" in value:
        import aws_sdk_qbusiness.types.membership_type

        out["type"] = aws_sdk_qbusiness.types.membership_type.serialize_json(
            value["type"]
        )
    return out


def deserialize_json(data: dict) -> AssociatedGroup:
    out: AssociatedGroup = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "type" in data:
        import aws_sdk_qbusiness.types.membership_type

        out["type"] = aws_sdk_qbusiness.types.membership_type.deserialize_json(
            data["type"]
        )
    return out
