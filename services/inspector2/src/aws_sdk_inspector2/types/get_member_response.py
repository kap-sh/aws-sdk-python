"""Generated from Smithy shape ``com.amazonaws.inspector2#GetMemberResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.member


class GetMemberResponse(TypedDict, closed=True):
    member: NotRequired["aws_sdk_inspector2.types.member.Member"]
    """<p>Details of the retrieved member account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMemberResponse) -> dict:
    out: dict = {}
    if "member" in value:
        import aws_sdk_inspector2.types.member

        out["member"] = aws_sdk_inspector2.types.member.serialize_json(value["member"])
    return out


def deserialize_json(data: dict) -> GetMemberResponse:
    out: GetMemberResponse = {}  # type: ignore[typeddict-item]
    if "member" in data:
        import aws_sdk_inspector2.types.member

        out["member"] = aws_sdk_inspector2.types.member.deserialize_json(data["member"])
    return out
