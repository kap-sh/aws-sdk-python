"""Generated from Smithy shape ``com.amazonaws.qbusiness#PrincipalUser``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_qbusiness.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.membership_type
    import aws_sdk_qbusiness.types.read_access_type
    import aws_sdk_qbusiness.types.user_id


class PrincipalUser(TypedDict):
    id: NotRequired["aws_sdk_qbusiness.types.user_id.UserId"]
    """<p> The identifier of the user. </p>"""
    access: "aws_sdk_qbusiness.types.read_access_type.ReadAccessType"
    """<p>Provides information about whether to allow or deny access to the principal.</p>"""
    membership_type: NotRequired[
        "aws_sdk_qbusiness.types.membership_type.MembershipType"
    ]
    """<p>The type of group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PrincipalUser) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    import aws_sdk_qbusiness.types.read_access_type

    out["access"] = aws_sdk_qbusiness.types.read_access_type.serialize_json(
        value["access"]
    )
    if "membership_type" in value:
        import aws_sdk_qbusiness.types.membership_type

        out["membershipType"] = aws_sdk_qbusiness.types.membership_type.serialize_json(
            value["membership_type"]
        )
    return out


def deserialize_json(data: dict) -> PrincipalUser:
    out: PrincipalUser = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "access" in data:
        import aws_sdk_qbusiness.types.read_access_type

        out["access"] = aws_sdk_qbusiness.types.read_access_type.deserialize_json(
            data["access"]
        )
    else:
        raise DeserializationError("PrincipalUser.access required")
    if "membershipType" in data:
        import aws_sdk_qbusiness.types.membership_type

        out["membership_type"] = (
            aws_sdk_qbusiness.types.membership_type.deserialize_json(
                data["membershipType"]
            )
        )
    return out
