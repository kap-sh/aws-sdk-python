"""Generated from Smithy shape ``com.amazonaws.fsx#RestoreOpenZFSVolumeOption``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_fsx.errors import DeserializationError

RestoreOpenZFSVolumeOption: TypeAlias = Literal[
    "DELETE_INTERMEDIATE_SNAPSHOTS",
    "DELETE_CLONED_VOLUMES",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DELETE_INTERMEDIATE_SNAPSHOTS",
        "DELETE_CLONED_VOLUMES",
    )
)


def serialize_aws_json_1_1(value: RestoreOpenZFSVolumeOption) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RestoreOpenZFSVolumeOption:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown RestoreOpenZFSVolumeOption value: {data!r}"
        )
    return cast(RestoreOpenZFSVolumeOption, data)
