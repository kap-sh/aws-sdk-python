"""Generated from Smithy shape ``com.amazonaws.codeartifact#UpstreamRepositoryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codeartifact.types.upstream_repository

UpstreamRepositoryList: TypeAlias = list[
    "aws_sdk_codeartifact.types.upstream_repository.UpstreamRepository"
]


# --- restJson1 ser/de ---
def serialize_json(value: UpstreamRepositoryList) -> list:
    import aws_sdk_codeartifact.types.upstream_repository

    out: list = []
    for item in value:
        out.append(aws_sdk_codeartifact.types.upstream_repository.serialize_json(item))
    return out


def deserialize_json(data: list) -> UpstreamRepositoryList:
    import aws_sdk_codeartifact.types.upstream_repository

    out: UpstreamRepositoryList = []
    for item in data:
        out.append(
            aws_sdk_codeartifact.types.upstream_repository.deserialize_json(item)
        )
    return out
