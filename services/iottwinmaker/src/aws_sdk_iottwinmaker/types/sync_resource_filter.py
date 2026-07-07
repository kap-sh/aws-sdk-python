"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#SyncResourceFilter``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_iottwinmaker.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.id
    import aws_sdk_iottwinmaker.types.sync_resource_state
    import aws_sdk_iottwinmaker.types.sync_resource_type


class _SyncResourceFilter_state(TypedDict, closed=True):
    state: "aws_sdk_iottwinmaker.types.sync_resource_state.SyncResourceState"


class _SyncResourceFilter_resourceType(TypedDict, closed=True):
    resourceType: "aws_sdk_iottwinmaker.types.sync_resource_type.SyncResourceType"


class _SyncResourceFilter_resourceId(TypedDict, closed=True):
    resourceId: "aws_sdk_iottwinmaker.types.id.Id"


class _SyncResourceFilter_externalId(TypedDict, closed=True):
    externalId: "aws_sdk_iottwinmaker.types.id.Id"


SyncResourceFilter: TypeAlias = (
    _SyncResourceFilter_state
    | _SyncResourceFilter_resourceType
    | _SyncResourceFilter_resourceId
    | _SyncResourceFilter_externalId
)


# --- restJson1 ser/de ---
def serialize_json(value: SyncResourceFilter) -> dict:
    if "state" in value:
        return {"state": value["state"]}
    elif "resourceType" in value:
        return {"resourceType": value["resourceType"]}
    elif "resourceId" in value:
        return {"resourceId": value["resourceId"]}
    elif "externalId" in value:
        return {"externalId": value["externalId"]}
    else:
        raise SerializationError("SyncResourceFilter: no variant present")


def deserialize_json(data: dict) -> SyncResourceFilter:
    if "state" in data:
        return {"state": data["state"]}
    elif "resourceType" in data:
        return {"resourceType": data["resourceType"]}
    elif "resourceId" in data:
        return {"resourceId": data["resourceId"]}
    elif "externalId" in data:
        return {"externalId": data["externalId"]}
    else:
        raise DeserializationError("SyncResourceFilter: no recognized variant key")
