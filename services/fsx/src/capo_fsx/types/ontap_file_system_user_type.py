"""Generated from Smithy shape ``com.amazonaws.fsx#OntapFileSystemUserType``."""

from typing import Literal, TypeAlias, cast

OntapFileSystemUserType: TypeAlias = Literal[
    "UNIX",
    "WINDOWS",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OntapFileSystemUserType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OntapFileSystemUserType:
    return cast(OntapFileSystemUserType, data)
