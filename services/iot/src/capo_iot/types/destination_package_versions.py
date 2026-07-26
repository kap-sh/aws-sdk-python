"""Generated from Smithy shape ``com.amazonaws.iot#DestinationPackageVersions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot.types.package_version_arn

DestinationPackageVersions: TypeAlias = list[
    "capo_iot.types.package_version_arn.PackageVersionArn"
]


# --- restJson1 ser/de ---
def serialize_json(value: DestinationPackageVersions) -> list:
    return list(value)


def deserialize_json(data: list) -> DestinationPackageVersions:
    return list(data)
