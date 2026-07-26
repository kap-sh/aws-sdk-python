"""Generated from Smithy shape ``com.amazonaws.qbusiness#MemberGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_qbusiness.errors import DeserializationError

if TYPE_CHECKING:
    import capo_qbusiness.types.group_name
    import capo_qbusiness.types.membership_type


class MemberGroup(TypedDict, closed=True):
    group_name: "capo_qbusiness.types.group_name.GroupName"
    """<p>The name of the sub group.</p>"""
    type: NotRequired["capo_qbusiness.types.membership_type.MembershipType"]
    """<p>The type of the sub group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MemberGroup) -> dict:
    out: dict = {}
    out["groupName"] = value["group_name"]
    if "type" in value:
        import capo_qbusiness.types.membership_type

        out["type"] = capo_qbusiness.types.membership_type.serialize_json(value["type"])
    return out


def deserialize_json(data: dict) -> MemberGroup:
    out: MemberGroup = {}  # type: ignore[typeddict-item]
    if "groupName" in data:
        out["group_name"] = data["groupName"]
    else:
        raise DeserializationError("MemberGroup.group_name required")
    if "type" in data:
        import capo_qbusiness.types.membership_type

        out["type"] = capo_qbusiness.types.membership_type.deserialize_json(
            data["type"]
        )
    return out
