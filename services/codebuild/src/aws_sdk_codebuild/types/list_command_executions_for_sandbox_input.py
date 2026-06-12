"""Generated from Smithy shape ``com.amazonaws.codebuild#ListCommandExecutionsForSandboxInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_codebuild.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codebuild.types.non_empty_string
    import aws_sdk_codebuild.types.page_size
    import aws_sdk_codebuild.types.sensitive_string
    import aws_sdk_codebuild.types.sort_order_type


class ListCommandExecutionsForSandboxInput(TypedDict):
    sandbox_id: "aws_sdk_codebuild.types.non_empty_string.NonEmptyString"
    """<p>A <code>sandboxId</code> or <code>sandboxArn</code>.</p>"""
    max_results: NotRequired["aws_sdk_codebuild.types.page_size.PageSize"]
    """<p>The maximum number of sandbox records to be retrieved.</p>"""
    sort_order: NotRequired["aws_sdk_codebuild.types.sort_order_type.SortOrderType"]
    """<p>The order in which sandbox records should be retrieved.</p>"""
    next_token: NotRequired["aws_sdk_codebuild.types.sensitive_string.SensitiveString"]
    """<p>The next token, if any, to get paginated results. You will get this value from previous execution of list sandboxes.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListCommandExecutionsForSandboxInput) -> dict:
    out: dict = {}
    out["sandboxId"] = value["sandbox_id"]
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


def deserialize_aws_json_1_1(data: dict) -> ListCommandExecutionsForSandboxInput:
    out: ListCommandExecutionsForSandboxInput = {}  # type: ignore[typeddict-item]
    if "sandboxId" in data:
        out["sandbox_id"] = data["sandboxId"]
    else:
        raise DeserializationError(
            "ListCommandExecutionsForSandboxInput.sandbox_id required"
        )
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
