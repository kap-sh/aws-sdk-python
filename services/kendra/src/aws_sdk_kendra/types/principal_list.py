"""Generated from Smithy shape ``com.amazonaws.kendra#PrincipalList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kendra.types.principal

PrincipalList: TypeAlias = list["aws_sdk_kendra.types.principal.Principal"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PrincipalList) -> list:
    import aws_sdk_kendra.types.principal

    out: list = []
    for item in value:
        out.append(aws_sdk_kendra.types.principal.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> PrincipalList:
    import aws_sdk_kendra.types.principal

    out: PrincipalList = []
    for item in data:
        out.append(aws_sdk_kendra.types.principal.deserialize_aws_json_1_1(item))
    return out
