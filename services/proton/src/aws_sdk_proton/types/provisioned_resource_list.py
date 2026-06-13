"""Generated from Smithy shape ``com.amazonaws.proton#ProvisionedResourceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_proton.types.provisioned_resource

ProvisionedResourceList: TypeAlias = list[
    "aws_sdk_proton.types.provisioned_resource.ProvisionedResource"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ProvisionedResourceList) -> list:
    import aws_sdk_proton.types.provisioned_resource

    out: list = []
    for item in value:
        out.append(
            aws_sdk_proton.types.provisioned_resource.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ProvisionedResourceList:
    import aws_sdk_proton.types.provisioned_resource

    out: ProvisionedResourceList = []
    for item in data:
        out.append(
            aws_sdk_proton.types.provisioned_resource.deserialize_aws_json_1_0(item)
        )
    return out
