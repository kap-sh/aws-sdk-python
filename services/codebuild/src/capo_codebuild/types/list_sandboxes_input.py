"""Generated from Smithy shape ``com.amazonaws.codebuild#ListSandboxesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codebuild.types.page_size
    import capo_codebuild.types.sort_order_type
    import capo_codebuild.types.string


class ListSandboxesInput(TypedDict, closed=True):
    max_results: NotRequired["capo_codebuild.types.page_size.PageSize"]
    """<p>The maximum number of sandbox records to be retrieved.</p>"""
    sort_order: NotRequired["capo_codebuild.types.sort_order_type.SortOrderType"]
    """<p>The order in which sandbox records should be retrieved.</p>"""
    next_token: NotRequired["capo_codebuild.types.string.String"]
    """<p>The next token, if any, to get paginated results. You will get this value from previous execution of list sandboxes.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListSandboxesInput) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "sort_order" in value:
        import capo_codebuild.types.sort_order_type

        out["sortOrder"] = capo_codebuild.types.sort_order_type.serialize_aws_json_1_1(
            value["sort_order"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListSandboxesInput:
    out: ListSandboxesInput = {}  # type: ignore[typeddict-item]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "sortOrder" in data:
        import capo_codebuild.types.sort_order_type

        out["sort_order"] = (
            capo_codebuild.types.sort_order_type.deserialize_aws_json_1_1(
                data["sortOrder"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
