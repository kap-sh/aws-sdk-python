"""Generated from Smithy shape ``com.amazonaws.fsx#FileCacheLustreDeploymentType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_fsx.errors import DeserializationError

FileCacheLustreDeploymentType: TypeAlias = Literal["CACHE_1",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("CACHE_1",))


def serialize_aws_json_1_1(value: FileCacheLustreDeploymentType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FileCacheLustreDeploymentType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown FileCacheLustreDeploymentType value: {data!r}"
        )
    return cast(FileCacheLustreDeploymentType, data)
