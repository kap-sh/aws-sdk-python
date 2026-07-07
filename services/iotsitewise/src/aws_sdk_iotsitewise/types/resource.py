"""Generated from Smithy shape ``com.amazonaws.iotsitewise#Resource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.portal_resource
    import aws_sdk_iotsitewise.types.project_resource


class Resource(TypedDict, closed=True):
    portal: NotRequired["aws_sdk_iotsitewise.types.portal_resource.PortalResource"]
    """<p>A portal resource.</p>"""
    project: NotRequired["aws_sdk_iotsitewise.types.project_resource.ProjectResource"]
    """<p>A project resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Resource) -> dict:
    out: dict = {}
    if "portal" in value:
        import aws_sdk_iotsitewise.types.portal_resource

        out["portal"] = aws_sdk_iotsitewise.types.portal_resource.serialize_json(
            value["portal"]
        )
    if "project" in value:
        import aws_sdk_iotsitewise.types.project_resource

        out["project"] = aws_sdk_iotsitewise.types.project_resource.serialize_json(
            value["project"]
        )
    return out


def deserialize_json(data: dict) -> Resource:
    out: Resource = {}  # type: ignore[typeddict-item]
    if "portal" in data:
        import aws_sdk_iotsitewise.types.portal_resource

        out["portal"] = aws_sdk_iotsitewise.types.portal_resource.deserialize_json(
            data["portal"]
        )
    if "project" in data:
        import aws_sdk_iotsitewise.types.project_resource

        out["project"] = aws_sdk_iotsitewise.types.project_resource.deserialize_json(
            data["project"]
        )
    return out
