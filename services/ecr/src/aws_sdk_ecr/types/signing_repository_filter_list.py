"""Generated from Smithy shape ``com.amazonaws.ecr#SigningRepositoryFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecr.types.signing_repository_filter

SigningRepositoryFilterList: TypeAlias = list[
    "aws_sdk_ecr.types.signing_repository_filter.SigningRepositoryFilter"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SigningRepositoryFilterList) -> list:
    import aws_sdk_ecr.types.signing_repository_filter

    out: list = []
    for item in value:
        out.append(
            aws_sdk_ecr.types.signing_repository_filter.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> SigningRepositoryFilterList:
    import aws_sdk_ecr.types.signing_repository_filter

    out: SigningRepositoryFilterList = []
    for item in data:
        out.append(
            aws_sdk_ecr.types.signing_repository_filter.deserialize_aws_json_1_1(item)
        )
    return out
