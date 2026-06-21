"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#AwsMemberBusinessTitle``."""

from typing import Literal, TypeAlias, cast

AwsMemberBusinessTitle: TypeAlias = Literal[
    "AWSSalesRep",
    "AWSAccountOwner",
    "WWPSPDM",
    "PDM",
    "PSM",
    "ISVSM",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AwsMemberBusinessTitle) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> AwsMemberBusinessTitle:
    return cast(AwsMemberBusinessTitle, data)
