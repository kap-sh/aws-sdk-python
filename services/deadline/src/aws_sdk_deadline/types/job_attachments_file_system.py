"""Generated from Smithy shape ``com.amazonaws.deadline#JobAttachmentsFileSystem``."""

from typing import Literal, TypeAlias, cast

JobAttachmentsFileSystem: TypeAlias = Literal[
    "COPIED",
    "VIRTUAL",
]


# --- restJson1 ser/de ---
def serialize_json(value: JobAttachmentsFileSystem) -> str:
    return value


def deserialize_json(data: str) -> JobAttachmentsFileSystem:
    return cast(JobAttachmentsFileSystem, data)
