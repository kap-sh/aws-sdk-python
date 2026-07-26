"""Generated from Smithy shape ``com.amazonaws.datazone#ProjectGrantFilter``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_datazone.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_datazone.types.domain_unit_filter_for_project


class _ProjectGrantFilter_domainUnitFilter(TypedDict, closed=True):
    domainUnitFilter: (
        "capo_datazone.types.domain_unit_filter_for_project.DomainUnitFilterForProject"
    )


ProjectGrantFilter: TypeAlias = _ProjectGrantFilter_domainUnitFilter


# --- restJson1 ser/de ---
def serialize_json(value: ProjectGrantFilter) -> dict:
    if "domainUnitFilter" in value:
        import capo_datazone.types.domain_unit_filter_for_project

        return {
            "domainUnitFilter": capo_datazone.types.domain_unit_filter_for_project.serialize_json(
                value["domainUnitFilter"]
            )
        }
    else:
        raise SerializationError("ProjectGrantFilter: no variant present")


def deserialize_json(data: dict) -> ProjectGrantFilter:
    if "domainUnitFilter" in data:
        import capo_datazone.types.domain_unit_filter_for_project

        return {
            "domainUnitFilter": capo_datazone.types.domain_unit_filter_for_project.deserialize_json(
                data["domainUnitFilter"]
            )
        }
    else:
        raise DeserializationError("ProjectGrantFilter: no recognized variant key")
