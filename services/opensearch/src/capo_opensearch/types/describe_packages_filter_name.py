"""Generated from Smithy shape ``com.amazonaws.opensearch#DescribePackagesFilterName``."""

from typing import Literal, TypeAlias, cast

DescribePackagesFilterName: TypeAlias = Literal[
    "PackageID",
    "PackageName",
    "PackageStatus",
    "PackageType",
    "EngineVersion",
    "PackageOwner",
]


# --- restJson1 ser/de ---
def serialize_json(value: DescribePackagesFilterName) -> str:
    return value


def deserialize_json(data: str) -> DescribePackagesFilterName:
    return cast(DescribePackagesFilterName, data)
