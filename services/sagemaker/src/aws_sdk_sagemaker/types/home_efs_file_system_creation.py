"""Generated from Smithy shape ``com.amazonaws.sagemaker#HomeEfsFileSystemCreation``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

"""<p>Indicates whether a home EFS file system is created for the domain.</p>"""
HomeEfsFileSystemCreation: TypeAlias = Literal[
    "Enabled",
    "Disabled",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Enabled",
        "Disabled",
    )
)


def serialize_aws_json_1_1(value: HomeEfsFileSystemCreation) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> HomeEfsFileSystemCreation:
    if data not in _VALUES:
        raise DeserializationError(f"unknown HomeEfsFileSystemCreation value: {data!r}")
    return cast(HomeEfsFileSystemCreation, data)
