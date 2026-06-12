"""Generated from Smithy shape ``com.amazonaws.connect#SignInDistributionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.sign_in_distribution

SignInDistributionList: TypeAlias = list[
    "aws_sdk_connect.types.sign_in_distribution.SignInDistribution"
]


# --- restJson1 ser/de ---
def serialize_json(value: SignInDistributionList) -> list:
    import aws_sdk_connect.types.sign_in_distribution

    out: list = []
    for item in value:
        out.append(aws_sdk_connect.types.sign_in_distribution.serialize_json(item))
    return out


def deserialize_json(data: list) -> SignInDistributionList:
    import aws_sdk_connect.types.sign_in_distribution

    out: SignInDistributionList = []
    for item in data:
        out.append(aws_sdk_connect.types.sign_in_distribution.deserialize_json(item))
    return out
