"""Generated from Smithy shape ``com.amazonaws.apprunner#CustomDomainList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_apprunner.types.custom_domain

CustomDomainList: TypeAlias = list["capo_apprunner.types.custom_domain.CustomDomain"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CustomDomainList) -> list:
    import capo_apprunner.types.custom_domain

    out: list = []
    for item in value:
        out.append(capo_apprunner.types.custom_domain.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> CustomDomainList:
    import capo_apprunner.types.custom_domain

    out: CustomDomainList = []
    for item in data:
        out.append(capo_apprunner.types.custom_domain.deserialize_aws_json_1_0(item))
    return out
