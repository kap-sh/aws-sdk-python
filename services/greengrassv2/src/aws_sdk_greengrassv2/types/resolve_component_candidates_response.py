"""Generated from Smithy shape ``com.amazonaws.greengrassv2#ResolveComponentCandidatesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_greengrassv2.types.resolved_component_versions_list


class ResolveComponentCandidatesResponse(TypedDict):
    resolved_component_versions: NotRequired[
        "aws_sdk_greengrassv2.types.resolved_component_versions_list.ResolvedComponentVersionsList"
    ]
    """<p>A list of components that meet the requirements that you specify in the request. This list includes each component's recipe that you can use to install the component.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResolveComponentCandidatesResponse) -> dict:
    out: dict = {}
    if "resolved_component_versions" in value:
        import aws_sdk_greengrassv2.types.resolved_component_versions_list

        out["resolvedComponentVersions"] = (
            aws_sdk_greengrassv2.types.resolved_component_versions_list.serialize_json(
                value["resolved_component_versions"]
            )
        )
    return out


def deserialize_json(data: dict) -> ResolveComponentCandidatesResponse:
    out: ResolveComponentCandidatesResponse = {}  # type: ignore[typeddict-item]
    if "resolvedComponentVersions" in data:
        import aws_sdk_greengrassv2.types.resolved_component_versions_list

        out["resolved_component_versions"] = (
            aws_sdk_greengrassv2.types.resolved_component_versions_list.deserialize_json(
                data["resolvedComponentVersions"]
            )
        )
    return out
