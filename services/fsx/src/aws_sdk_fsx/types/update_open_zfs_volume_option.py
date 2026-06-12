"""Generated from Smithy shape ``com.amazonaws.fsx#UpdateOpenZFSVolumeOption``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_fsx.errors import DeserializationError

UpdateOpenZFSVolumeOption: TypeAlias = Literal[
    "DELETE_INTERMEDIATE_SNAPSHOTS",
    "DELETE_CLONED_VOLUMES",
    "DELETE_INTERMEDIATE_DATA",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DELETE_INTERMEDIATE_SNAPSHOTS",
        "DELETE_CLONED_VOLUMES",
        "DELETE_INTERMEDIATE_DATA",
    )
)


def serialize_aws_json_1_1(value: UpdateOpenZFSVolumeOption) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> UpdateOpenZFSVolumeOption:
    if data not in _VALUES:
        raise DeserializationError(f"unknown UpdateOpenZFSVolumeOption value: {data!r}")
    return cast(UpdateOpenZFSVolumeOption, data)
