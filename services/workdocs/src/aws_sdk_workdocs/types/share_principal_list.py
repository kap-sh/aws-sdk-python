"""Generated from Smithy shape ``com.amazonaws.workdocs#SharePrincipalList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_workdocs.types.share_principal

SharePrincipalList: TypeAlias = list[
    "aws_sdk_workdocs.types.share_principal.SharePrincipal"
]


# --- restJson1 ser/de ---
def serialize_json(value: SharePrincipalList) -> list:
    import aws_sdk_workdocs.types.share_principal

    out: list = []
    for item in value:
        out.append(aws_sdk_workdocs.types.share_principal.serialize_json(item))
    return out


def deserialize_json(data: list) -> SharePrincipalList:
    import aws_sdk_workdocs.types.share_principal

    out: SharePrincipalList = []
    for item in data:
        out.append(aws_sdk_workdocs.types.share_principal.deserialize_json(item))
    return out
