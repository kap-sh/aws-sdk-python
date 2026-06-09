"""Generated from Smithy shape ``com.amazonaws.ec2#RegisteredInstanceList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.registered_instance

RegisteredInstanceList: TypeAlias = list[
    "aws_sdk_ec2.types.registered_instance.RegisteredInstance"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: RegisteredInstanceList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.registered_instance

        aws_sdk_ec2.types.registered_instance.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> RegisteredInstanceList:
    import aws_sdk_ec2.types.registered_instance

    out: RegisteredInstanceList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_ec2.types.registered_instance.deserialize_ec2_query(child))
    return out
