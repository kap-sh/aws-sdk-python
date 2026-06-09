"""Generated from Smithy shape ``com.amazonaws.ec2#ResourceTypeRequestList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.resource_type_request

ResourceTypeRequestList: TypeAlias = list[
    "aws_sdk_ec2.types.resource_type_request.ResourceTypeRequest"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ResourceTypeRequestList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.resource_type_request

        aws_sdk_ec2.types.resource_type_request.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> ResourceTypeRequestList:
    import aws_sdk_ec2.types.resource_type_request

    out: ResourceTypeRequestList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_ec2.types.resource_type_request.deserialize_ec2_query(child))
    return out
