"""Generated from Smithy shape ``com.amazonaws.codecatalyst#ProjectListFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codecatalyst.types.project_list_filter

ProjectListFilters: TypeAlias = list[
    "capo_codecatalyst.types.project_list_filter.ProjectListFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: ProjectListFilters) -> list:
    import capo_codecatalyst.types.project_list_filter

    out: list = []
    for item in value:
        out.append(capo_codecatalyst.types.project_list_filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> ProjectListFilters:
    import capo_codecatalyst.types.project_list_filter

    out: ProjectListFilters = []
    for item in data:
        out.append(capo_codecatalyst.types.project_list_filter.deserialize_json(item))
    return out
