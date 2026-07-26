"""Generated from Smithy shape ``com.amazonaws.codeartifact#RepositoryExternalConnectionInfoList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codeartifact.types.repository_external_connection_info

RepositoryExternalConnectionInfoList: TypeAlias = list[
    "capo_codeartifact.types.repository_external_connection_info.RepositoryExternalConnectionInfo"
]


# --- restJson1 ser/de ---
def serialize_json(value: RepositoryExternalConnectionInfoList) -> list:
    import capo_codeartifact.types.repository_external_connection_info

    out: list = []
    for item in value:
        out.append(
            capo_codeartifact.types.repository_external_connection_info.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> RepositoryExternalConnectionInfoList:
    import capo_codeartifact.types.repository_external_connection_info

    out: RepositoryExternalConnectionInfoList = []
    for item in data:
        out.append(
            capo_codeartifact.types.repository_external_connection_info.deserialize_json(
                item
            )
        )
    return out
