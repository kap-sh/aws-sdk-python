"""Generated from Smithy shape ``com.amazonaws.workspacesweb#UpdatePortalResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_workspaces_web.types.portal


class UpdatePortalResponse(TypedDict, closed=True):
    portal: NotRequired["aws_sdk_workspaces_web.types.portal.Portal"]
    """<p>The web portal.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatePortalResponse) -> dict:
    out: dict = {}
    if "portal" in value:
        import aws_sdk_workspaces_web.types.portal

        out["portal"] = aws_sdk_workspaces_web.types.portal.serialize_json(
            value["portal"]
        )
    return out


def deserialize_json(data: dict) -> UpdatePortalResponse:
    out: UpdatePortalResponse = {}  # type: ignore[typeddict-item]
    if "portal" in data:
        import aws_sdk_workspaces_web.types.portal

        out["portal"] = aws_sdk_workspaces_web.types.portal.deserialize_json(
            data["portal"]
        )
    return out
