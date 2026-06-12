"""Generated from Smithy shape ``com.amazonaws.sagemaker#DeleteContextRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.context_name


class DeleteContextRequest(TypedDict):
    context_name: NotRequired["aws_sdk_sagemaker.types.context_name.ContextName"]
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
