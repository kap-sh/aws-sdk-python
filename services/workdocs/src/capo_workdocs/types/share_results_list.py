"""Generated from Smithy shape ``com.amazonaws.workdocs#ShareResultsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workdocs.types.share_result

ShareResultsList: TypeAlias = list["capo_workdocs.types.share_result.ShareResult"]


# --- restJson1 ser/de ---
def serialize_json(value: ShareResultsList) -> list:
    import capo_workdocs.types.share_result

    out: list = []
    for item in value:
        out.append(capo_workdocs.types.share_result.serialize_json(item))
    return out


def deserialize_json(data: list) -> ShareResultsList:
    import capo_workdocs.types.share_result

    out: ShareResultsList = []
    for item in data:
        out.append(capo_workdocs.types.share_result.deserialize_json(item))
    return out
