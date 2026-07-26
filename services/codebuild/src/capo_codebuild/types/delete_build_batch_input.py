"""Generated from Smithy shape ``com.amazonaws.codebuild#DeleteBuildBatchInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_codebuild.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codebuild.types.non_empty_string


class DeleteBuildBatchInput(TypedDict, closed=True):
    id: "capo_codebuild.types.non_empty_string.NonEmptyString"
    """<p>The identifier of the batch build to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteBuildBatchInput) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteBuildBatchInput:
    out: DeleteBuildBatchInput = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("DeleteBuildBatchInput.id required")
    return out
