"""Generated from Smithy shape ``com.amazonaws.wisdom#GetSessionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_wisdom.types.session_data


class GetSessionResponse(TypedDict):
    session: NotRequired["aws_sdk_wisdom.types.session_data.SessionData"]
    """<p>The session.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSessionResponse) -> dict:
    out: dict = {}
    if "session" in value:
        import aws_sdk_wisdom.types.session_data

        out["session"] = aws_sdk_wisdom.types.session_data.serialize_json(
            value["session"]
        )
    return out


def deserialize_json(data: dict) -> GetSessionResponse:
    out: GetSessionResponse = {}  # type: ignore[typeddict-item]
    if "session" in data:
        import aws_sdk_wisdom.types.session_data

        out["session"] = aws_sdk_wisdom.types.session_data.deserialize_json(
            data["session"]
        )
    return out
