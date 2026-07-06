"""Generated from Smithy shape ``com.amazonaws.qbusiness#AssociatedUser``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.membership_type
    import aws_sdk_qbusiness.types.string


class AssociatedUser(TypedDict, closed=True):
    id: NotRequired["aws_sdk_qbusiness.types.string.String"]
    """<p>The unique identifier of the associated user. This is used to identify the user in access control decisions.</p>"""
    type: NotRequired["aws_sdk_qbusiness.types.membership_type.MembershipType"]
    """<p>The type of the associated user. This indicates the scope of the user's association.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociatedUser) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "type" in value:
        import aws_sdk_qbusiness.types.membership_type

        out["type"] = aws_sdk_qbusiness.types.membership_type.serialize_json(
            value["type"]
        )
    return out


def deserialize_json(data: dict) -> AssociatedUser:
    out: AssociatedUser = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "type" in data:
        import aws_sdk_qbusiness.types.membership_type

        out["type"] = aws_sdk_qbusiness.types.membership_type.deserialize_json(
            data["type"]
        )
    return out
