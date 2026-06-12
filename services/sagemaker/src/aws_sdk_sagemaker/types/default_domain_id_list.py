"""Generated from Smithy shape ``com.amazonaws.sagemaker#DefaultDomainIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.domain_id

DefaultDomainIdList: TypeAlias = list["aws_sdk_sagemaker.types.domain_id.DomainId"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DefaultDomainIdList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> DefaultDomainIdList:
    return list(data)
