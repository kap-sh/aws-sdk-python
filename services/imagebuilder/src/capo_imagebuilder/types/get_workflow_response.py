"""Generated from Smithy shape ``com.amazonaws.imagebuilder#GetWorkflowResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.latest_version_references
    import capo_imagebuilder.types.workflow


class GetWorkflowResponse(TypedDict, closed=True):
    workflow: NotRequired["capo_imagebuilder.types.workflow.Workflow"]
    """<p>The workflow resource specified in the request.</p>"""
    latest_version_references: NotRequired[
        "capo_imagebuilder.types.latest_version_references.LatestVersionReferences"
    ]
    """<p>The resource ARNs with different wildcard variations of semantic versioning.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetWorkflowResponse) -> dict:
    out: dict = {}
    if "workflow" in value:
        import capo_imagebuilder.types.workflow

        out["workflow"] = capo_imagebuilder.types.workflow.serialize_json(
            value["workflow"]
        )
    if "latest_version_references" in value:
        import capo_imagebuilder.types.latest_version_references

        out["latestVersionReferences"] = (
            capo_imagebuilder.types.latest_version_references.serialize_json(
                value["latest_version_references"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetWorkflowResponse:
    out: GetWorkflowResponse = {}  # type: ignore[typeddict-item]
    if "workflow" in data:
        import capo_imagebuilder.types.workflow

        out["workflow"] = capo_imagebuilder.types.workflow.deserialize_json(
            data["workflow"]
        )
    if "latestVersionReferences" in data:
        import capo_imagebuilder.types.latest_version_references

        out["latest_version_references"] = (
            capo_imagebuilder.types.latest_version_references.deserialize_json(
                data["latestVersionReferences"]
            )
        )
    return out
