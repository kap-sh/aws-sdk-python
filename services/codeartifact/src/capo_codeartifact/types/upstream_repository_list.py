"""Generated from Smithy shape ``com.amazonaws.codeartifact#UpstreamRepositoryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codeartifact.types.upstream_repository

UpstreamRepositoryList: TypeAlias = list[
    "capo_codeartifact.types.upstream_repository.UpstreamRepository"
]


# --- restJson1 ser/de ---
def serialize_json(value: UpstreamRepositoryList) -> list:
    import capo_codeartifact.types.upstream_repository

    out: list = []
    for item in value:
        out.append(capo_codeartifact.types.upstream_repository.serialize_json(item))
    return out


def deserialize_json(data: list) -> UpstreamRepositoryList:
    import capo_codeartifact.types.upstream_repository

    out: UpstreamRepositoryList = []
    for item in data:
        out.append(capo_codeartifact.types.upstream_repository.deserialize_json(item))
    return out
