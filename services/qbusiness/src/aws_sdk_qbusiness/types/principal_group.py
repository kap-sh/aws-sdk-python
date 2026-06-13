"""Generated from Smithy shape ``com.amazonaws.qbusiness#PrincipalGroup``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_qbusiness.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.group_name
    import aws_sdk_qbusiness.types.membership_type
    import aws_sdk_qbusiness.types.read_access_type


class PrincipalGroup(TypedDict):
    name: NotRequired["aws_sdk_qbusiness.types.group_name.GroupName"]
    """<p>The name of the group.</p>"""
    access: "aws_sdk_qbusiness.types.read_access_type.ReadAccessType"
    """<p>Provides information about whether to allow or deny access to the principal.</p>"""
    membership_type: NotRequired[
        "aws_sdk_qbusiness.types.membership_type.MembershipType"
    ]
    """<p>The type of group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PrincipalGroup) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
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


def deserialize_json(data: dict) -> PrincipalGroup:
    out: PrincipalGroup = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "access" in data:
        import aws_sdk_qbusiness.types.read_access_type

        out["access"] = aws_sdk_qbusiness.types.read_access_type.deserialize_json(
            data["access"]
        )
    else:
        raise DeserializationError("PrincipalGroup.access required")
    if "membershipType" in data:
        import aws_sdk_qbusiness.types.membership_type

        out["membership_type"] = (
            aws_sdk_qbusiness.types.membership_type.deserialize_json(
                data["membershipType"]
            )
        )
    return out
