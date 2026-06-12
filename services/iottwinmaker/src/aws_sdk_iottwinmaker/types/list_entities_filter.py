"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#ListEntitiesFilter``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_iottwinmaker.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.component_type_id
    import aws_sdk_iottwinmaker.types.parent_entity_id
    import aws_sdk_iottwinmaker.types.string


class _ListEntitiesFilter_parentEntityId(TypedDict):
    parentEntityId: "aws_sdk_iottwinmaker.types.parent_entity_id.ParentEntityId"


class _ListEntitiesFilter_componentTypeId(TypedDict):
    componentTypeId: "aws_sdk_iottwinmaker.types.component_type_id.ComponentTypeId"


class _ListEntitiesFilter_externalId(TypedDict):
    externalId: "aws_sdk_iottwinmaker.types.string.String"


ListEntitiesFilter: TypeAlias = (
    _ListEntitiesFilter_parentEntityId
    | _ListEntitiesFilter_componentTypeId
    | _ListEntitiesFilter_externalId
)


# --- restJson1 ser/de ---
def serialize_json(value: ListEntitiesFilter) -> dict:
    if "parentEntityId" in value:
        return {"parentEntityId": value["parentEntityId"]}
    elif "componentTypeId" in value:
        return {"componentTypeId": value["componentTypeId"]}
    elif "externalId" in value:
        return {"externalId": value["externalId"]}
    else:
        raise SerializationError("ListEntitiesFilter: no variant present")


def deserialize_json(data: dict) -> ListEntitiesFilter:
    if "parentEntityId" in data:
        return {"parentEntityId": data["parentEntityId"]}
    elif "componentTypeId" in data:
        return {"componentTypeId": data["componentTypeId"]}
    elif "externalId" in data:
        return {"externalId": data["externalId"]}
    else:
        raise DeserializationError("ListEntitiesFilter: no recognized variant key")
