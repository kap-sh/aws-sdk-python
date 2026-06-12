"""Generated from Smithy shape ``com.amazonaws.lightsail#SetupDomainNameList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.setup_domain_name

SetupDomainNameList: TypeAlias = list[
    "aws_sdk_lightsail.types.setup_domain_name.SetupDomainName"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SetupDomainNameList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> SetupDomainNameList:
    return list(data)
