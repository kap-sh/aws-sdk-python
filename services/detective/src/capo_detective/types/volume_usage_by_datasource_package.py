"""Generated from Smithy shape ``com.amazonaws.detective#VolumeUsageByDatasourcePackage``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_detective.types.datasource_package
    import capo_detective.types.datasource_package_usage_info

VolumeUsageByDatasourcePackage: TypeAlias = dict[
    "capo_detective.types.datasource_package.DatasourcePackage",
    "capo_detective.types.datasource_package_usage_info.DatasourcePackageUsageInfo",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: VolumeUsageByDatasourcePackage) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_detective.types.datasource_package
        import capo_detective.types.datasource_package_usage_info

        out[capo_detective.types.datasource_package.serialize_json(key)] = (
            capo_detective.types.datasource_package_usage_info.serialize_json(value)
        )
    return out


def deserialize_json(data: dict) -> VolumeUsageByDatasourcePackage:
    out: VolumeUsageByDatasourcePackage = {}
    for key, value in data.items():
        import capo_detective.types.datasource_package
        import capo_detective.types.datasource_package_usage_info

        out[capo_detective.types.datasource_package.deserialize_json(key)] = (
            capo_detective.types.datasource_package_usage_info.deserialize_json(value)
        )
    return out
