"""Generated from Smithy shape ``com.amazonaws.codecommit#RepositoryNameIdPairList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.repository_name_id_pair

RepositoryNameIdPairList: TypeAlias = list[
    "aws_sdk_codecommit.types.repository_name_id_pair.RepositoryNameIdPair"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RepositoryNameIdPairList) -> list:
    import aws_sdk_codecommit.types.repository_name_id_pair

    out: list = []
    for item in value:
        out.append(
            aws_sdk_codecommit.types.repository_name_id_pair.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> RepositoryNameIdPairList:
    import aws_sdk_codecommit.types.repository_name_id_pair

    out: RepositoryNameIdPairList = []
    for item in data:
        out.append(
            aws_sdk_codecommit.types.repository_name_id_pair.deserialize_aws_json_1_1(
                item
            )
        )
    return out
