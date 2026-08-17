"""Generated from Smithy shape ``com.amazonaws.ecr#SigningRepositoryFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecr.types.signing_repository_filter

SigningRepositoryFilterList: TypeAlias = list[
    "capo_ecr.types.signing_repository_filter.SigningRepositoryFilter"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SigningRepositoryFilterList) -> list:
    import capo_ecr.types.signing_repository_filter

    out: list = []
    for item in value:
        out.append(
            capo_ecr.types.signing_repository_filter.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> SigningRepositoryFilterList:
    import capo_ecr.types.signing_repository_filter

    out: SigningRepositoryFilterList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_ecr.types.signing_repository_filter.deserialize_aws_json_1_1(item)
        )
    return out
