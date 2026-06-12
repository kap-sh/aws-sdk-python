"""Generated from Smithy shape ``com.amazonaws.directoryservice#RemoteDomainNames``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_directory_service.types.remote_domain_name

RemoteDomainNames: TypeAlias = list[
    "aws_sdk_directory_service.types.remote_domain_name.RemoteDomainName"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RemoteDomainNames) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> RemoteDomainNames:
    return list(data)
