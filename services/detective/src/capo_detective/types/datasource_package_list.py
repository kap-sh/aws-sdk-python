"""Generated from Smithy shape ``com.amazonaws.detective#DatasourcePackageList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_detective.types.datasource_package

DatasourcePackageList: TypeAlias = list[
    "capo_detective.types.datasource_package.DatasourcePackage"
]


# --- restJson1 ser/de ---
def serialize_json(value: DatasourcePackageList) -> list:
    import capo_detective.types.datasource_package

    out: list = []
    for item in value:
        out.append(capo_detective.types.datasource_package.serialize_json(item))
    return out


def deserialize_json(data: list) -> DatasourcePackageList:
    import capo_detective.types.datasource_package

    out: DatasourcePackageList = []
    for item in data:
        out.append(capo_detective.types.datasource_package.deserialize_json(item))
    return out
