"""Generated from Smithy shape ``com.amazonaws.omics#VersionDeleteErrorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_omics.types.version_delete_error

VersionDeleteErrorList: TypeAlias = list[
    "capo_omics.types.version_delete_error.VersionDeleteError"
]


# --- restJson1 ser/de ---
def serialize_json(value: VersionDeleteErrorList) -> list:
    import capo_omics.types.version_delete_error

    out: list = []
    for item in value:
        out.append(capo_omics.types.version_delete_error.serialize_json(item))
    return out


def deserialize_json(data: list) -> VersionDeleteErrorList:
    import capo_omics.types.version_delete_error

    out: VersionDeleteErrorList = []
    for item in data:
        out.append(capo_omics.types.version_delete_error.deserialize_json(item))
    return out
