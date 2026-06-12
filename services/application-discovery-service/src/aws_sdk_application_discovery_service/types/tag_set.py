"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#TagSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_application_discovery_service.types.tag

TagSet: TypeAlias = list["aws_sdk_application_discovery_service.types.tag.Tag"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagSet) -> list:
    import aws_sdk_application_discovery_service.types.tag

    out: list = []
    for item in value:
        out.append(
            aws_sdk_application_discovery_service.types.tag.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> TagSet:
    import aws_sdk_application_discovery_service.types.tag

    out: TagSet = []
    for item in data:
        out.append(
            aws_sdk_application_discovery_service.types.tag.deserialize_aws_json_1_1(
                item
            )
        )
    return out
