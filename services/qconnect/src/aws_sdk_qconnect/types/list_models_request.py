"""Generated from Smithy shape ``com.amazonaws.qconnect#ListModelsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.ai_prompt_type
    import aws_sdk_qconnect.types.max_results
    import aws_sdk_qconnect.types.model_lifecycle
    import aws_sdk_qconnect.types.next_token
    import aws_sdk_qconnect.types.uuid_or_arn


class ListModelsRequest(TypedDict):
    assistant_id: "aws_sdk_qconnect.types.uuid_or_arn.UuidOrArn"
    """<p>The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN. The assistant's region determines which models are available.</p>"""
    ai_prompt_type: NotRequired["aws_sdk_qconnect.types.ai_prompt_type.AIPromptType"]
    """<p>The type of the AI Prompt to filter models by. When specified, only models that support the given AI Prompt type are returned.</p>"""
    model_lifecycle: NotRequired[
        "aws_sdk_qconnect.types.model_lifecycle.ModelLifecycle"
    ]
    """<p>The lifecycle status of models to filter by. When specified, only models with the given lifecycle status are returned.</p>"""
    next_token: NotRequired["aws_sdk_qconnect.types.next_token.NextToken"]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>"""
    max_results: NotRequired["aws_sdk_qconnect.types.max_results.MaxResults"]
    """<p>The maximum number of results to return per page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListModelsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListModelsRequest:
    out: ListModelsRequest = {}  # type: ignore[typeddict-item]
    return out
