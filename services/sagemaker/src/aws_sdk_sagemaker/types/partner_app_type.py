"""Generated from Smithy shape ``com.amazonaws.sagemaker#PartnerAppType``."""

from typing import Literal, TypeAlias, cast

PartnerAppType: TypeAlias = Literal[
    "lakera-guard",
    "comet",
    "deepchecks-llm-evaluation",
    "fiddler",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PartnerAppType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PartnerAppType:
    return cast(PartnerAppType, data)
