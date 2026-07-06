"""Generated from Smithy shape ``com.amazonaws.qconnect#UpdateSessionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.session_data


class UpdateSessionResponse(TypedDict, closed=True):
    session: NotRequired["aws_sdk_qconnect.types.session_data.SessionData"]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSessionResponse) -> dict:
    out: dict = {}
    if "session" in value:
        import aws_sdk_qconnect.types.session_data

        out["session"] = aws_sdk_qconnect.types.session_data.serialize_json(
            value["session"]
        )
    return out


def deserialize_json(data: dict) -> UpdateSessionResponse:
    out: UpdateSessionResponse = {}  # type: ignore[typeddict-item]
    if "session" in data:
        import aws_sdk_qconnect.types.session_data

        out["session"] = aws_sdk_qconnect.types.session_data.deserialize_json(
            data["session"]
        )
    return out
