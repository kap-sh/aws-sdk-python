"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#Resources``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_marketplace_agreement.types.resource

Resources: TypeAlias = list["aws_sdk_marketplace_agreement.types.resource.Resource"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Resources) -> list:
    import aws_sdk_marketplace_agreement.types.resource

    out: list = []
    for item in value:
        out.append(
            aws_sdk_marketplace_agreement.types.resource.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> Resources:
    import aws_sdk_marketplace_agreement.types.resource

    out: Resources = []
    for item in data:
        out.append(
            aws_sdk_marketplace_agreement.types.resource.deserialize_aws_json_1_0(item)
        )
    return out
