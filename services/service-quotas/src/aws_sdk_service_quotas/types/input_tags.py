"""Generated from Smithy shape ``com.amazonaws.servicequotas#InputTags``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_service_quotas.types.tag

InputTags: TypeAlias = list["aws_sdk_service_quotas.types.tag.Tag"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InputTags) -> list:
    import aws_sdk_service_quotas.types.tag

    out: list = []
    for item in value:
        out.append(aws_sdk_service_quotas.types.tag.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> InputTags:
    import aws_sdk_service_quotas.types.tag

    out: InputTags = []
    for item in data:
        out.append(aws_sdk_service_quotas.types.tag.deserialize_aws_json_1_1(item))
    return out
