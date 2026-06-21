"""Generated from Smithy shape ``com.amazonaws.ecr#SigningRepositoryFilterType``."""

from typing import Literal, TypeAlias, cast

"""<p>The type of filter to use when determining which repositories should have their images automatically signed.</p>"""
SigningRepositoryFilterType: TypeAlias = Literal["WILDCARD_MATCH",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SigningRepositoryFilterType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SigningRepositoryFilterType:
    return cast(SigningRepositoryFilterType, data)
