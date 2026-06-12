"""Generated from Smithy shape ``com.amazonaws.connect#ResourceTagsSearchCriteria``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.tag_search_condition


class ResourceTagsSearchCriteria(TypedDict):
    tag_search_condition: NotRequired[
        "aws_sdk_connect.types.tag_search_condition.TagSearchCondition"
    ]
    """<p>The search criteria to be used to return tags.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceTagsSearchCriteria) -> dict:
    out: dict = {}
    if "tag_search_condition" in value:
        import aws_sdk_connect.types.tag_search_condition

        out["TagSearchCondition"] = (
            aws_sdk_connect.types.tag_search_condition.serialize_json(
                value["tag_search_condition"]
            )
        )
    return out


def deserialize_json(data: dict) -> ResourceTagsSearchCriteria:
    out: ResourceTagsSearchCriteria = {}  # type: ignore[typeddict-item]
    if "TagSearchCondition" in data:
        import aws_sdk_connect.types.tag_search_condition

        out["tag_search_condition"] = (
            aws_sdk_connect.types.tag_search_condition.deserialize_json(
                data["TagSearchCondition"]
            )
        )
    return out
