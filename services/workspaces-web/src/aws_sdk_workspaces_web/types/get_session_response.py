"""Generated from Smithy shape ``com.amazonaws.workspacesweb#GetSessionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_workspaces_web.types.session


class GetSessionResponse(TypedDict, closed=True):
    session: NotRequired["aws_sdk_workspaces_web.types.session.Session"]
    """<p>The sessions in a list.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSessionResponse) -> dict:
    out: dict = {}
    if "session" in value:
        import aws_sdk_workspaces_web.types.session

        out["session"] = aws_sdk_workspaces_web.types.session.serialize_json(
            value["session"]
        )
    return out


def deserialize_json(data: dict) -> GetSessionResponse:
    out: GetSessionResponse = {}  # type: ignore[typeddict-item]
    if "session" in data:
        import aws_sdk_workspaces_web.types.session

        out["session"] = aws_sdk_workspaces_web.types.session.deserialize_json(
            data["session"]
        )
    return out
