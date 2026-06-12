"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ListLifecycleExecutionsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.lifecycle_executions_list
    import aws_sdk_imagebuilder.types.pagination_token


class ListLifecycleExecutionsResponse(TypedDict):
    lifecycle_executions: NotRequired[
        "aws_sdk_imagebuilder.types.lifecycle_executions_list.LifecycleExecutionsList"
    ]
    """<p>A list of lifecycle runtime instances for the specified resource.</p>"""
    next_token: NotRequired[
        "aws_sdk_imagebuilder.types.pagination_token.PaginationToken"
    ]
    """<p>The next token used for paginated responses. When this field isn't empty, there are additional elements that the service hasn't included in this request. Use this token with the next request to retrieve additional objects.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListLifecycleExecutionsResponse) -> dict:
    out: dict = {}
    if "lifecycle_executions" in value:
        import aws_sdk_imagebuilder.types.lifecycle_executions_list

        out["lifecycleExecutions"] = (
            aws_sdk_imagebuilder.types.lifecycle_executions_list.serialize_json(
                value["lifecycle_executions"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListLifecycleExecutionsResponse:
    out: ListLifecycleExecutionsResponse = {}  # type: ignore[typeddict-item]
    if "lifecycleExecutions" in data:
        import aws_sdk_imagebuilder.types.lifecycle_executions_list

        out["lifecycle_executions"] = (
            aws_sdk_imagebuilder.types.lifecycle_executions_list.deserialize_json(
                data["lifecycleExecutions"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
