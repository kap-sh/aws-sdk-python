"""Generated from Smithy shape ``com.amazonaws.iotsitewise#Resource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.portal_resource
    import capo_iotsitewise.types.project_resource


class Resource(TypedDict, closed=True):
    portal: NotRequired["capo_iotsitewise.types.portal_resource.PortalResource"]
    """<p>A portal resource.</p>"""
    project: NotRequired["capo_iotsitewise.types.project_resource.ProjectResource"]
    """<p>A project resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Resource) -> dict:
    out: dict = {}
    if "portal" in value:
        import capo_iotsitewise.types.portal_resource

        out["portal"] = capo_iotsitewise.types.portal_resource.serialize_json(
            value["portal"]
        )
    if "project" in value:
        import capo_iotsitewise.types.project_resource

        out["project"] = capo_iotsitewise.types.project_resource.serialize_json(
            value["project"]
        )
    return out


def deserialize_json(data: dict) -> Resource:
    out: Resource = {}  # type: ignore[typeddict-item]
    if "portal" in data:
        import capo_iotsitewise.types.portal_resource

        out["portal"] = capo_iotsitewise.types.portal_resource.deserialize_json(
            data["portal"]
        )
    if "project" in data:
        import capo_iotsitewise.types.project_resource

        out["project"] = capo_iotsitewise.types.project_resource.deserialize_json(
            data["project"]
        )
    return out
