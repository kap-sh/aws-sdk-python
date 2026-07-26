"""Generated from Smithy shape ``com.amazonaws.codeconnections#RepositoryLinkList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codeconnections.types.repository_link_info

RepositoryLinkList: TypeAlias = list[
    "capo_codeconnections.types.repository_link_info.RepositoryLinkInfo"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RepositoryLinkList) -> list:
    import capo_codeconnections.types.repository_link_info

    out: list = []
    for item in value:
        out.append(
            capo_codeconnections.types.repository_link_info.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> RepositoryLinkList:
    import capo_codeconnections.types.repository_link_info

    out: RepositoryLinkList = []
    for item in data:
        out.append(
            capo_codeconnections.types.repository_link_info.deserialize_aws_json_1_0(
                item
            )
        )
    return out
