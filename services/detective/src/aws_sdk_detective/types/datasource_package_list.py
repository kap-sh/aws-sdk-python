"""Generated from Smithy shape ``com.amazonaws.detective#DatasourcePackageList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_detective.types.datasource_package

DatasourcePackageList: TypeAlias = list[
    "aws_sdk_detective.types.datasource_package.DatasourcePackage"
]


# --- restJson1 ser/de ---
def serialize_json(value: DatasourcePackageList) -> list:
    import aws_sdk_detective.types.datasource_package

    out: list = []
    for item in value:
        out.append(aws_sdk_detective.types.datasource_package.serialize_json(item))
    return out


def deserialize_json(data: list) -> DatasourcePackageList:
    import aws_sdk_detective.types.datasource_package

    out: DatasourcePackageList = []
    for item in data:
        out.append(aws_sdk_detective.types.datasource_package.deserialize_json(item))
    return out
