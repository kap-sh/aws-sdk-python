"""Generated from Smithy shape ``com.amazonaws.chime#Member``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime.types.member_type
    import aws_sdk_chime.types.non_empty_string
    import aws_sdk_chime.types.sensitive_string


class Member(TypedDict, closed=True):
    member_id: NotRequired["aws_sdk_chime.types.non_empty_string.NonEmptyString"]
    """<p>The member ID (user ID or bot ID).</p>"""
    member_type: NotRequired["aws_sdk_chime.types.member_type.MemberType"]
    """<p>The member type.</p>"""
    email: NotRequired["aws_sdk_chime.types.sensitive_string.SensitiveString"]
    """<p>The member email address.</p>"""
    full_name: NotRequired["aws_sdk_chime.types.sensitive_string.SensitiveString"]
    """<p>The member name.</p>"""
    account_id: NotRequired["aws_sdk_chime.types.non_empty_string.NonEmptyString"]
    """<p>The Amazon Chime account ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Member) -> dict:
    out: dict = {}
    if "member_id" in value:
        out["MemberId"] = value["member_id"]
    if "member_type" in value:
        import aws_sdk_chime.types.member_type

        out["MemberType"] = aws_sdk_chime.types.member_type.serialize_json(
            value["member_type"]
        )
    if "email" in value:
        out["Email"] = value["email"]
    if "full_name" in value:
        out["FullName"] = value["full_name"]
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    return out


def deserialize_json(data: dict) -> Member:
    out: Member = {}  # type: ignore[typeddict-item]
    if "MemberId" in data:
        out["member_id"] = data["MemberId"]
    if "MemberType" in data:
        import aws_sdk_chime.types.member_type

        out["member_type"] = aws_sdk_chime.types.member_type.deserialize_json(
            data["MemberType"]
        )
    if "Email" in data:
        out["email"] = data["Email"]
    if "FullName" in data:
        out["full_name"] = data["FullName"]
    if "AccountId" in data:
        out["account_id"] = data["AccountId"]
    return out
