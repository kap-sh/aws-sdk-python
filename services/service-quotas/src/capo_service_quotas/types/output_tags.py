"""Generated from Smithy shape ``com.amazonaws.servicequotas#OutputTags``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_service_quotas.types.tag

OutputTags: TypeAlias = list["capo_service_quotas.types.tag.Tag"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OutputTags) -> list:
    import capo_service_quotas.types.tag

    out: list = []
    for item in value:
        out.append(capo_service_quotas.types.tag.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> OutputTags:
    import capo_service_quotas.types.tag

    out: OutputTags = []
    for item in data:
        out.append(capo_service_quotas.types.tag.deserialize_aws_json_1_1(item))
    return out
