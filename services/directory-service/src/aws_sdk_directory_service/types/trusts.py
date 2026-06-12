"""Generated from Smithy shape ``com.amazonaws.directoryservice#Trusts``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_directory_service.types.trust

Trusts: TypeAlias = list["aws_sdk_directory_service.types.trust.Trust"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Trusts) -> list:
    import aws_sdk_directory_service.types.trust

    out: list = []
    for item in value:
        out.append(aws_sdk_directory_service.types.trust.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Trusts:
    import aws_sdk_directory_service.types.trust

    out: Trusts = []
    for item in data:
        out.append(aws_sdk_directory_service.types.trust.deserialize_aws_json_1_1(item))
    return out
