"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#ListMetadataTransferJobsFilter``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_iottwinmaker.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.id
    import aws_sdk_iottwinmaker.types.metadata_transfer_job_state


class _ListMetadataTransferJobsFilter_workspaceId(TypedDict, closed=True):
    workspaceId: "aws_sdk_iottwinmaker.types.id.Id"


class _ListMetadataTransferJobsFilter_state(TypedDict, closed=True):
    state: "aws_sdk_iottwinmaker.types.metadata_transfer_job_state.MetadataTransferJobState"


ListMetadataTransferJobsFilter: TypeAlias = (
    _ListMetadataTransferJobsFilter_workspaceId | _ListMetadataTransferJobsFilter_state
)


# --- restJson1 ser/de ---
def serialize_json(value: ListMetadataTransferJobsFilter) -> dict:
    if "workspaceId" in value:
        return {"workspaceId": value["workspaceId"]}
    elif "state" in value:
        return {"state": value["state"]}
    else:
        raise SerializationError("ListMetadataTransferJobsFilter: no variant present")


def deserialize_json(data: dict) -> ListMetadataTransferJobsFilter:
    if "workspaceId" in data:
        return {"workspaceId": data["workspaceId"]}
    elif "state" in data:
        return {"state": data["state"]}
    else:
        raise DeserializationError(
            "ListMetadataTransferJobsFilter: no recognized variant key"
        )
