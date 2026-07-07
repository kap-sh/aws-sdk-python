"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#ListComponentTypesFilter``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_iottwinmaker.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.boolean
    import aws_sdk_iottwinmaker.types.component_type_id
    import aws_sdk_iottwinmaker.types.string


class _ListComponentTypesFilter_extendsFrom(TypedDict, closed=True):
    extendsFrom: "aws_sdk_iottwinmaker.types.component_type_id.ComponentTypeId"


class _ListComponentTypesFilter_namespace(TypedDict, closed=True):
    namespace: "aws_sdk_iottwinmaker.types.string.String"


class _ListComponentTypesFilter_isAbstract(TypedDict, closed=True):
    isAbstract: "aws_sdk_iottwinmaker.types.boolean.Boolean"


ListComponentTypesFilter: TypeAlias = (
    _ListComponentTypesFilter_extendsFrom
    | _ListComponentTypesFilter_namespace
    | _ListComponentTypesFilter_isAbstract
)


# --- restJson1 ser/de ---
def serialize_json(value: ListComponentTypesFilter) -> dict:
    if "extendsFrom" in value:
        return {"extendsFrom": value["extendsFrom"]}
    elif "namespace" in value:
        return {"namespace": value["namespace"]}
    elif "isAbstract" in value:
        return {"isAbstract": value["isAbstract"]}
    else:
        raise SerializationError("ListComponentTypesFilter: no variant present")


def deserialize_json(data: dict) -> ListComponentTypesFilter:
    if "extendsFrom" in data:
        return {"extendsFrom": data["extendsFrom"]}
    elif "namespace" in data:
        return {"namespace": data["namespace"]}
    elif "isAbstract" in data:
        return {"isAbstract": data["isAbstract"]}
    else:
        raise DeserializationError(
            "ListComponentTypesFilter: no recognized variant key"
        )
