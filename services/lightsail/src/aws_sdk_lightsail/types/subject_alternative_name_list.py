"""Generated from Smithy shape ``com.amazonaws.lightsail#SubjectAlternativeNameList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.domain_name

SubjectAlternativeNameList: TypeAlias = list[
    "aws_sdk_lightsail.types.domain_name.DomainName"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SubjectAlternativeNameList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> SubjectAlternativeNameList:
    return list(data)
