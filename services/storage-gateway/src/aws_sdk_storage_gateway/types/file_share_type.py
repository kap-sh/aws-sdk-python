"""Generated from Smithy shape ``com.amazonaws.storagegateway#FileShareType``."""

from typing import Literal, TypeAlias, cast

"""<p>The type of the file share.</p>"""
FileShareType: TypeAlias = Literal[
    "NFS",
    "SMB",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FileShareType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FileShareType:
    return cast(FileShareType, data)
