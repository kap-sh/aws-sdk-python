"""Generated from Smithy shape ``com.amazonaws.sagemaker#DeleteContextRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.context_name


class DeleteContextRequest(TypedDict, closed=True):
    context_name: NotRequired["capo_sagemaker.types.context_name.ContextName"]
    """<p>The name of the context to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteContextRequest) -> dict:
    out: dict = {}
    if "context_name" in value:
        out["ContextName"] = value["context_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteContextRequest:
    out: DeleteContextRequest = {}  # type: ignore[typeddict-item]
    if "ContextName" in data:
        out["context_name"] = data["ContextName"]
    return out
