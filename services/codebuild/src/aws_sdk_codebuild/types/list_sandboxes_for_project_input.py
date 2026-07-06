"""Generated from Smithy shape ``com.amazonaws.codebuild#ListSandboxesForProjectInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_codebuild.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codebuild.types.non_empty_string
    import aws_sdk_codebuild.types.page_size
    import aws_sdk_codebuild.types.sensitive_string
    import aws_sdk_codebuild.types.sort_order_type


class ListSandboxesForProjectInput(TypedDict, closed=True):
    project_name: "aws_sdk_codebuild.types.non_empty_string.NonEmptyString"
    """<p>The CodeBuild project name.</p>"""
    max_results: NotRequired["aws_sdk_codebuild.types.page_size.PageSize"]
    """<p>The maximum number of sandbox records to be retrieved.</p>"""
    sort_order: NotRequired["aws_sdk_codebuild.types.sort_order_type.SortOrderType"]
    """<p>The order in which sandbox records should be retrieved.</p>"""
    next_token: NotRequired["aws_sdk_codebuild.types.sensitive_string.SensitiveString"]
    """<p>The next token, if any, to get paginated results. You will get this value from previous execution of list sandboxes.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListSandboxesForProjectInput) -> dict:
    out: dict = {}
    out["projectName"] = value["project_name"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "sort_order" in value:
        import aws_sdk_codebuild.types.sort_order_type

        out["sortOrder"] = (
            aws_sdk_codebuild.types.sort_order_type.serialize_aws_json_1_1(
                value["sort_order"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListSandboxesForProjectInput:
    out: ListSandboxesForProjectInput = {}  # type: ignore[typeddict-item]
    if "projectName" in data:
        out["project_name"] = data["projectName"]
    else:
        raise DeserializationError("ListSandboxesForProjectInput.project_name required")
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "sortOrder" in data:
        import aws_sdk_codebuild.types.sort_order_type

        out["sort_order"] = (
            aws_sdk_codebuild.types.sort_order_type.deserialize_aws_json_1_1(
                data["sortOrder"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
