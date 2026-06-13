"""Generated from Smithy shape ``com.amazonaws.omics#VersionDeleteErrorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_omics.types.version_delete_error

VersionDeleteErrorList: TypeAlias = list[
    "aws_sdk_omics.types.version_delete_error.VersionDeleteError"
]


# --- restJson1 ser/de ---
def serialize_json(value: VersionDeleteErrorList) -> list:
    import aws_sdk_omics.types.version_delete_error

    out: list = []
    for item in value:
        out.append(aws_sdk_omics.types.version_delete_error.serialize_json(item))
    return out


def deserialize_json(data: list) -> VersionDeleteErrorList:
    import aws_sdk_omics.types.version_delete_error

    out: VersionDeleteErrorList = []
    for item in data:
        out.append(aws_sdk_omics.types.version_delete_error.deserialize_json(item))
    return out
