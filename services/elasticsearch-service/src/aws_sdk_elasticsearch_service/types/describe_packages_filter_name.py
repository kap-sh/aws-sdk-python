"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#DescribePackagesFilterName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_elasticsearch_service.errors import DeserializationError

DescribePackagesFilterName: TypeAlias = Literal[
    "PackageID",
    "PackageName",
    "PackageStatus",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PackageID",
        "PackageName",
        "PackageStatus",
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
