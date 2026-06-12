"""Generated from Smithy shape ``com.amazonaws.codeartifact#UpstreamRepositoryInfoList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codeartifact.types.upstream_repository_info

UpstreamRepositoryInfoList: TypeAlias = list[
    "aws_sdk_codeartifact.types.upstream_repository_info.UpstreamRepositoryInfo"
]


# --- restJson1 ser/de ---
def serialize_json(value: UpstreamRepositoryInfoList) -> list:
    import aws_sdk_codeartifact.types.upstream_repository_info

    out: list = []
    for item in value:
        out.append(
            aws_sdk_codeartifact.types.upstream_repository_info.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> UpstreamRepositoryInfoList:
    import aws_sdk_codeartifact.types.upstream_repository_info

    out: UpstreamRepositoryInfoList = []
    for item in data:
        out.append(
            aws_sdk_codeartifact.types.upstream_repository_info.deserialize_json(item)
        )
    return out
