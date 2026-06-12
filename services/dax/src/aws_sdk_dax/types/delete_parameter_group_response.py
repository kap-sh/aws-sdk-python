"""Generated from Smithy shape ``com.amazonaws.dax#DeleteParameterGroupResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dax.types.string


class DeleteParameterGroupResponse(TypedDict):
    deletion_message: NotRequired["aws_sdk_dax.types.string.String"]
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
