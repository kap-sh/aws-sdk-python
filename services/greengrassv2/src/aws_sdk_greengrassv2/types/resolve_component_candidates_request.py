"""Generated from Smithy shape ``com.amazonaws.greengrassv2#ResolveComponentCandidatesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_greengrassv2.types.component_candidate_list
    import aws_sdk_greengrassv2.types.component_platform


class ResolveComponentCandidatesRequest(TypedDict):
    platform: NotRequired[
        "aws_sdk_greengrassv2.types.component_platform.ComponentPlatform"
    ]
    """<p>The platform to use to resolve compatible components.</p>"""
    component_candidates: NotRequired[
        "aws_sdk_greengrassv2.types.component_candidate_list.ComponentCandidateList"
    ]
    """<p>The list of components to resolve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResolveComponentCandidatesRequest) -> dict:
    out: dict = {}
    if "platform" in value:
        import aws_sdk_greengrassv2.types.component_platform

        out["platform"] = aws_sdk_greengrassv2.types.component_platform.serialize_json(
            value["platform"]
        )
    if "component_candidates" in value:
        import aws_sdk_greengrassv2.types.component_candidate_list

        out["componentCandidates"] = (
            aws_sdk_greengrassv2.types.component_candidate_list.serialize_json(
                value["component_candidates"]
            )
        )
    return out


def deserialize_json(data: dict) -> ResolveComponentCandidatesRequest:
    out: ResolveComponentCandidatesRequest = {}  # type: ignore[typeddict-item]
    if "platform" in data:
        import aws_sdk_greengrassv2.types.component_platform

        out["platform"] = (
            aws_sdk_greengrassv2.types.component_platform.deserialize_json(
                data["platform"]
            )
        )
    if "componentCandidates" in data:
        import aws_sdk_greengrassv2.types.component_candidate_list

        out["component_candidates"] = (
            aws_sdk_greengrassv2.types.component_candidate_list.deserialize_json(
                data["componentCandidates"]
            )
        )
    return out
