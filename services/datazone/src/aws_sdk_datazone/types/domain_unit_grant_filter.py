"""Generated from Smithy shape ``com.amazonaws.datazone#DomainUnitGrantFilter``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_datazone.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.all_domain_units_grant_filter


class _DomainUnitGrantFilter_allDomainUnitsGrantFilter(TypedDict, closed=True):
    allDomainUnitsGrantFilter: (
        "aws_sdk_datazone.types.all_domain_units_grant_filter.AllDomainUnitsGrantFilter"
    )


DomainUnitGrantFilter: TypeAlias = _DomainUnitGrantFilter_allDomainUnitsGrantFilter


# --- restJson1 ser/de ---
def serialize_json(value: DomainUnitGrantFilter) -> dict:
    if "allDomainUnitsGrantFilter" in value:
        import aws_sdk_datazone.types.all_domain_units_grant_filter

        return {
            "allDomainUnitsGrantFilter": aws_sdk_datazone.types.all_domain_units_grant_filter.serialize_json(
                value["allDomainUnitsGrantFilter"]
            )
        }
    else:
        raise SerializationError("DomainUnitGrantFilter: no variant present")


def deserialize_json(data: dict) -> DomainUnitGrantFilter:
    if "allDomainUnitsGrantFilter" in data:
        import aws_sdk_datazone.types.all_domain_units_grant_filter

        return {
            "allDomainUnitsGrantFilter": aws_sdk_datazone.types.all_domain_units_grant_filter.deserialize_json(
                data["allDomainUnitsGrantFilter"]
            )
        }
    else:
        raise DeserializationError("DomainUnitGrantFilter: no recognized variant key")
