"""Generated from Smithy shape ``com.amazonaws.interconnect#AttachPointDescriptorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_interconnect.types.attach_point_descriptor

AttachPointDescriptorList: TypeAlias = list[
    "aws_sdk_interconnect.types.attach_point_descriptor.AttachPointDescriptor"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AttachPointDescriptorList) -> list:
    import aws_sdk_interconnect.types.attach_point_descriptor

    out: list = []
    for item in value:
        out.append(
            aws_sdk_interconnect.types.attach_point_descriptor.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> AttachPointDescriptorList:
    import aws_sdk_interconnect.types.attach_point_descriptor

    out: AttachPointDescriptorList = []
    for item in data:
        out.append(
            aws_sdk_interconnect.types.attach_point_descriptor.deserialize_aws_json_1_0(
                item
            )
        )
    return out
