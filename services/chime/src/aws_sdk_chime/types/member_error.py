"""Generated from Smithy shape ``com.amazonaws.chime#MemberError``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_chime.types.error_code
    import aws_sdk_chime.types.non_empty_string
    import aws_sdk_chime.types.string


class MemberError(TypedDict):
    member_id: NotRequired["aws_sdk_chime.types.non_empty_string.NonEmptyString"]
    """<p>The member ID.</p>"""
    error_code: NotRequired["aws_sdk_chime.types.error_code.ErrorCode"]
    """<p>The error code.</p>"""
    error_message: NotRequired["aws_sdk_chime.types.string.String"]
    """<p>The error message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MemberError) -> dict:
    out: dict = {}
    if "member_id" in value:
        out["MemberId"] = value["member_id"]
    if "error_code" in value:
        import aws_sdk_chime.types.error_code

        out["ErrorCode"] = aws_sdk_chime.types.error_code.serialize_json(
            value["error_code"]
        )
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    return out


def deserialize_json(data: dict) -> MemberError:
    out: MemberError = {}  # type: ignore[typeddict-item]
    if "MemberId" in data:
        out["member_id"] = data["MemberId"]
    if "ErrorCode" in data:
        import aws_sdk_chime.types.error_code

        out["error_code"] = aws_sdk_chime.types.error_code.deserialize_json(
            data["ErrorCode"]
        )
    if "ErrorMessage" in data:
        out["error_message"] = data["ErrorMessage"]
    return out
