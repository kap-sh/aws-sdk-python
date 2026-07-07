"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#IotTwinMakerSourceConfigurationFilter``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_iottwinmaker.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.filter_by_component_type
    import aws_sdk_iottwinmaker.types.filter_by_entity


class _IotTwinMakerSourceConfigurationFilter_filterByComponentType(
    TypedDict, closed=True
):
    filterByComponentType: (
        "aws_sdk_iottwinmaker.types.filter_by_component_type.FilterByComponentType"
    )


class _IotTwinMakerSourceConfigurationFilter_filterByEntity(TypedDict, closed=True):
    filterByEntity: "aws_sdk_iottwinmaker.types.filter_by_entity.FilterByEntity"


IotTwinMakerSourceConfigurationFilter: TypeAlias = (
    _IotTwinMakerSourceConfigurationFilter_filterByComponentType
    | _IotTwinMakerSourceConfigurationFilter_filterByEntity
)


# --- restJson1 ser/de ---
def serialize_json(value: IotTwinMakerSourceConfigurationFilter) -> dict:
    if "filterByComponentType" in value:
        import aws_sdk_iottwinmaker.types.filter_by_component_type

        return {
            "filterByComponentType": aws_sdk_iottwinmaker.types.filter_by_component_type.serialize_json(
                value["filterByComponentType"]
            )
        }
    elif "filterByEntity" in value:
        import aws_sdk_iottwinmaker.types.filter_by_entity

        return {
            "filterByEntity": aws_sdk_iottwinmaker.types.filter_by_entity.serialize_json(
                value["filterByEntity"]
            )
        }
    else:
        raise SerializationError(
            "IotTwinMakerSourceConfigurationFilter: no variant present"
        )


def deserialize_json(data: dict) -> IotTwinMakerSourceConfigurationFilter:
    if "filterByComponentType" in data:
        import aws_sdk_iottwinmaker.types.filter_by_component_type

        return {
            "filterByComponentType": aws_sdk_iottwinmaker.types.filter_by_component_type.deserialize_json(
                data["filterByComponentType"]
            )
        }
    elif "filterByEntity" in data:
        import aws_sdk_iottwinmaker.types.filter_by_entity

        return {
            "filterByEntity": aws_sdk_iottwinmaker.types.filter_by_entity.deserialize_json(
                data["filterByEntity"]
            )
        }
    else:
        raise DeserializationError(
            "IotTwinMakerSourceConfigurationFilter: no recognized variant key"
        )
