"""Generated from Smithy shape ``com.amazonaws.codepipeline#PollingServicePrincipalList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codepipeline.types.service_principal

PollingServicePrincipalList: TypeAlias = list[
    "capo_codepipeline.types.service_principal.ServicePrincipal"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PollingServicePrincipalList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> PollingServicePrincipalList:
    return list(data)
