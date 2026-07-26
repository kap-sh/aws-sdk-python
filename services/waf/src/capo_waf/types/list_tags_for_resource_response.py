"""Generated from Smithy shape ``com.amazonaws.waf#ListTagsForResourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_waf.types.next_marker
    import capo_waf.types.tag_info_for_resource


class ListTagsForResourceResponse(TypedDict, closed=True):
    next_marker: NotRequired["capo_waf.types.next_marker.NextMarker"]
    """<p></p>"""
    tag_info_for_resource: NotRequired[
        "capo_waf.types.tag_info_for_resource.TagInfoForResource"
    ]
    """<p></p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTagsForResourceResponse) -> dict:
    out: dict = {}
    if "next_marker" in value:
        out["NextMarker"] = value["next_marker"]
    if "tag_info_for_resource" in value:
        import capo_waf.types.tag_info_for_resource

        out["TagInfoForResource"] = (
            capo_waf.types.tag_info_for_resource.serialize_aws_json_1_1(
                value["tag_info_for_resource"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTagsForResourceResponse:
    out: ListTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    if "NextMarker" in data:
        out["next_marker"] = data["NextMarker"]
    if "TagInfoForResource" in data:
        import capo_waf.types.tag_info_for_resource

        out["tag_info_for_resource"] = (
            capo_waf.types.tag_info_for_resource.deserialize_aws_json_1_1(
                data["TagInfoForResource"]
            )
        )
    return out
