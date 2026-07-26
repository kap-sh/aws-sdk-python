"""Generated from Smithy shape ``com.amazonaws.dax#DeleteParameterGroupResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dax.types.string


class DeleteParameterGroupResponse(TypedDict, closed=True):
    deletion_message: NotRequired["capo_dax.types.string.String"]
    """<p>A user-specified message for this action (i.e., a reason for deleting the parameter group).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteParameterGroupResponse) -> dict:
    out: dict = {}
    if "deletion_message" in value:
        out["DeletionMessage"] = value["deletion_message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteParameterGroupResponse:
    out: DeleteParameterGroupResponse = {}  # type: ignore[typeddict-item]
    if "DeletionMessage" in data:
        out["deletion_message"] = data["DeletionMessage"]
    return out
