"""Generated from Smithy shape ``com.amazonaws.kendra#HierarchicalPrincipalList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kendra.types.hierarchical_principal

HierarchicalPrincipalList: TypeAlias = list[
    "aws_sdk_kendra.types.hierarchical_principal.HierarchicalPrincipal"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HierarchicalPrincipalList) -> list:
    import aws_sdk_kendra.types.hierarchical_principal

    out: list = []
    for item in value:
        out.append(
            aws_sdk_kendra.types.hierarchical_principal.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> HierarchicalPrincipalList:
    import aws_sdk_kendra.types.hierarchical_principal

    out: HierarchicalPrincipalList = []
    for item in data:
        out.append(
            aws_sdk_kendra.types.hierarchical_principal.deserialize_aws_json_1_1(item)
        )
    return out
