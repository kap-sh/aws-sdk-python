"""Generated from Smithy shape ``com.amazonaws.kendra#PrincipalList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kendra.types.principal

PrincipalList: TypeAlias = list["capo_kendra.types.principal.Principal"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PrincipalList) -> list:
    import capo_kendra.types.principal

    out: list = []
    for item in value:
        out.append(capo_kendra.types.principal.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> PrincipalList:
    import capo_kendra.types.principal

    out: PrincipalList = []
    for item in data:
        out.append(capo_kendra.types.principal.deserialize_aws_json_1_1(item))
    return out
