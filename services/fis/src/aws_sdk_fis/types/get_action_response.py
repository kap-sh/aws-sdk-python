"""Generated from Smithy shape ``com.amazonaws.fis#GetActionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_fis.types.action


class GetActionResponse(TypedDict):
    action: NotRequired["aws_sdk_fis.types.action.Action"]
    """<p>Information about the action.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetActionResponse) -> dict:
    out: dict = {}
    if "action" in value:
        import aws_sdk_fis.types.action

        out["action"] = aws_sdk_fis.types.action.serialize_json(value["action"])
    return out


def deserialize_json(data: dict) -> GetActionResponse:
    out: GetActionResponse = {}  # type: ignore[typeddict-item]
    if "action" in data:
        import aws_sdk_fis.types.action

        out["action"] = aws_sdk_fis.types.action.deserialize_json(data["action"])
    return out
