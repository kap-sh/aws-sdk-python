"""Generated from Smithy shape ``com.amazonaws.iotsitewise#PortalTypeEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.portal_tools


class PortalTypeEntry(TypedDict, closed=True):
    portal_tools: NotRequired["capo_iotsitewise.types.portal_tools.PortalTools"]
    """<p>The array of tools associated with the specified portal type. The possible values are <code>ASSISTANT</code> and <code>DASHBOARD</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PortalTypeEntry) -> dict:
    out: dict = {}
    if "portal_tools" in value:
        import capo_iotsitewise.types.portal_tools

        out["portalTools"] = capo_iotsitewise.types.portal_tools.serialize_json(
            value["portal_tools"]
        )
    return out


def deserialize_json(data: dict) -> PortalTypeEntry:
    out: PortalTypeEntry = {}  # type: ignore[typeddict-item]
    if "portalTools" in data:
        import capo_iotsitewise.types.portal_tools

        out["portal_tools"] = capo_iotsitewise.types.portal_tools.deserialize_json(
            data["portalTools"]
        )
    return out
