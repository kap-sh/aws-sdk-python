"""Generated from Smithy shape ``com.amazonaws.glue#ListBlueprintsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.generic_string
    import aws_sdk_glue.types.orchestration_page_size25
    import aws_sdk_glue.types.tags_map


class ListBlueprintsRequest(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_glue.types.generic_string.GenericString"]
    """<p>A continuation token, if this is a continuation request.</p>"""
    max_results: NotRequired[
        "aws_sdk_glue.types.orchestration_page_size25.OrchestrationPageSize25"
    ]
    """<p>The maximum size of a list to return.</p>"""
    tags: NotRequired["aws_sdk_glue.types.tags_map.TagsMap"]
    """<p>Filters the list by an Amazon Web Services resource tag.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListBlueprintsRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "tags" in value:
        import aws_sdk_glue.types.tags_map

        out["Tags"] = aws_sdk_glue.types.tags_map.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> ListBlueprintsRequest:
    out: ListBlueprintsRequest = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "Tags" in data:
        import aws_sdk_glue.types.tags_map

        out["tags"] = aws_sdk_glue.types.tags_map.deserialize_aws_json_1_1(data["Tags"])
    return out
