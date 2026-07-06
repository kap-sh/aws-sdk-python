"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#ListScenesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.next_token
    import aws_sdk_iottwinmaker.types.scene_summaries


class ListScenesResponse(TypedDict, closed=True):
    scene_summaries: NotRequired[
        "aws_sdk_iottwinmaker.types.scene_summaries.SceneSummaries"
    ]
    """<p>A list of objects that contain information about the scenes.</p>"""
    next_token: NotRequired["aws_sdk_iottwinmaker.types.next_token.NextToken"]
    """<p>The string that specifies the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListScenesResponse) -> dict:
    out: dict = {}
    if "scene_summaries" in value:
        import aws_sdk_iottwinmaker.types.scene_summaries

        out["sceneSummaries"] = (
            aws_sdk_iottwinmaker.types.scene_summaries.serialize_json(
                value["scene_summaries"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListScenesResponse:
    out: ListScenesResponse = {}  # type: ignore[typeddict-item]
    if "sceneSummaries" in data:
        import aws_sdk_iottwinmaker.types.scene_summaries

        out["scene_summaries"] = (
            aws_sdk_iottwinmaker.types.scene_summaries.deserialize_json(
                data["sceneSummaries"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
