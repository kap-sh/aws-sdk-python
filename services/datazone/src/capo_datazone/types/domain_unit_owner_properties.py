"""Generated from Smithy shape ``com.amazonaws.datazone#DomainUnitOwnerProperties``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_datazone.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_datazone.types.domain_unit_group_properties
    import capo_datazone.types.domain_unit_user_properties


class _DomainUnitOwnerProperties_user(TypedDict, closed=True):
    user: "capo_datazone.types.domain_unit_user_properties.DomainUnitUserProperties"


class _DomainUnitOwnerProperties_group(TypedDict, closed=True):
    group: "capo_datazone.types.domain_unit_group_properties.DomainUnitGroupProperties"


DomainUnitOwnerProperties: TypeAlias = (
    _DomainUnitOwnerProperties_user | _DomainUnitOwnerProperties_group
)


# --- restJson1 ser/de ---
def serialize_json(value: DomainUnitOwnerProperties) -> dict:
    if "user" in value:
        import capo_datazone.types.domain_unit_user_properties

        return {
            "user": capo_datazone.types.domain_unit_user_properties.serialize_json(
                value["user"]
            )
        }
    elif "group" in value:
        import capo_datazone.types.domain_unit_group_properties

        return {
            "group": capo_datazone.types.domain_unit_group_properties.serialize_json(
                value["group"]
            )
        }
    else:
        raise SerializationError("DomainUnitOwnerProperties: no variant present")


def deserialize_json(data: dict) -> DomainUnitOwnerProperties:
    if "user" in data:
        import capo_datazone.types.domain_unit_user_properties

        return {
            "user": capo_datazone.types.domain_unit_user_properties.deserialize_json(
                data["user"]
            )
        }
    elif "group" in data:
        import capo_datazone.types.domain_unit_group_properties

        return {
            "group": capo_datazone.types.domain_unit_group_properties.deserialize_json(
                data["group"]
            )
        }
    else:
        raise DeserializationError(
            "DomainUnitOwnerProperties: no recognized variant key"
        )
