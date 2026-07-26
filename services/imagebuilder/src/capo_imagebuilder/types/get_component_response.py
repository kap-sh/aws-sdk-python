"""Generated from Smithy shape ``com.amazonaws.imagebuilder#GetComponentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.component
    import capo_imagebuilder.types.latest_version_references
    import capo_imagebuilder.types.non_empty_string


class GetComponentResponse(TypedDict, closed=True):
    request_id: NotRequired["capo_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>The request ID that uniquely identifies this request.</p>"""
    component: NotRequired["capo_imagebuilder.types.component.Component"]
    """<p>The component object specified in the request.</p>"""
    latest_version_references: NotRequired[
        "capo_imagebuilder.types.latest_version_references.LatestVersionReferences"
    ]
    """<p>The resource ARNs with different wildcard variations of semantic versioning.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetComponentResponse) -> dict:
    out: dict = {}
    if "request_id" in value:
        out["requestId"] = value["request_id"]
    if "component" in value:
        import capo_imagebuilder.types.component

        out["component"] = capo_imagebuilder.types.component.serialize_json(
            value["component"]
        )
    if "latest_version_references" in value:
        import capo_imagebuilder.types.latest_version_references

        out["latestVersionReferences"] = (
            capo_imagebuilder.types.latest_version_references.serialize_json(
                value["latest_version_references"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetComponentResponse:
    out: GetComponentResponse = {}  # type: ignore[typeddict-item]
    if "requestId" in data:
        out["request_id"] = data["requestId"]
    if "component" in data:
        import capo_imagebuilder.types.component

        out["component"] = capo_imagebuilder.types.component.deserialize_json(
            data["component"]
        )
    if "latestVersionReferences" in data:
        import capo_imagebuilder.types.latest_version_references

        out["latest_version_references"] = (
            capo_imagebuilder.types.latest_version_references.deserialize_json(
                data["latestVersionReferences"]
            )
        )
    return out
