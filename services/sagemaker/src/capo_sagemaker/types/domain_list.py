"""Generated from Smithy shape ``com.amazonaws.sagemaker#DomainList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.domain_details

DomainList: TypeAlias = list["capo_sagemaker.types.domain_details.DomainDetails"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DomainList) -> list:
    import capo_sagemaker.types.domain_details

    out: list = []
    for item in value:
        out.append(capo_sagemaker.types.domain_details.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> DomainList:
    import capo_sagemaker.types.domain_details

    out: DomainList = []
    for item in data:
        out.append(capo_sagemaker.types.domain_details.deserialize_aws_json_1_1(item))
    return out
