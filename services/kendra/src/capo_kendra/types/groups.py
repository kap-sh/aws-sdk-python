"""Generated from Smithy shape ``com.amazonaws.kendra#Groups``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kendra.types.principal_name

Groups: TypeAlias = list["capo_kendra.types.principal_name.PrincipalName"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Groups) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> Groups:
    return list(data)
