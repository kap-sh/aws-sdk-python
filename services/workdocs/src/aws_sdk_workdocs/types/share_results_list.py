"""Generated from Smithy shape ``com.amazonaws.workdocs#ShareResultsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_workdocs.types.share_result

ShareResultsList: TypeAlias = list["aws_sdk_workdocs.types.share_result.ShareResult"]


# --- restJson1 ser/de ---
def serialize_json(value: ShareResultsList) -> list:
    import aws_sdk_workdocs.types.share_result

    out: list = []
    for item in value:
        out.append(aws_sdk_workdocs.types.share_result.serialize_json(item))
    return out


def deserialize_json(data: list) -> ShareResultsList:
    import aws_sdk_workdocs.types.share_result

    out: ShareResultsList = []
    for item in data:
        out.append(aws_sdk_workdocs.types.share_result.deserialize_json(item))
    return out
