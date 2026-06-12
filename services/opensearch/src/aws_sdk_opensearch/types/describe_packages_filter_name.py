"""Generated from Smithy shape ``com.amazonaws.opensearch#DescribePackagesFilterName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_opensearch.errors import DeserializationError

DescribePackagesFilterName: TypeAlias = Literal[
    "PackageID",
    "PackageName",
    "PackageStatus",
    "PackageType",
    "EngineVersion",
    "PackageOwner",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PackageID",
        "PackageName",
        "PackageStatus",
        "PackageType",
        "EngineVersion",
        "PackageOwner",
    )
)


def serialize_json(value: DescribePackagesFilterName) -> str:
    return value


def deserialize_json(data: str) -> DescribePackagesFilterName:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown DescribePackagesFilterName value: {data!r}"
        )
    return cast(DescribePackagesFilterName, data)
