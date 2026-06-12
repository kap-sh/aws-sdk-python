"""Generated from Smithy shape ``com.amazonaws.servicequotas#OutputTags``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_service_quotas.types.tag

OutputTags: TypeAlias = list["aws_sdk_service_quotas.types.tag.Tag"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OutputTags) -> list:
    import aws_sdk_service_quotas.types.tag

    out: list = []
    for item in value:
        out.append(aws_sdk_service_quotas.types.tag.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> OutputTags:
    import aws_sdk_service_quotas.types.tag

    out: OutputTags = []
    for item in data:
        out.append(aws_sdk_service_quotas.types.tag.deserialize_aws_json_1_1(item))
    return out
