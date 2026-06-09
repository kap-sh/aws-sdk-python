"""Generated from Smithy shape ``com.amazonaws.ec2#ActiveInstanceSet``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.active_instance

ActiveInstanceSet: TypeAlias = list["aws_sdk_ec2.types.active_instance.ActiveInstance"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ActiveInstanceSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.active_instance

        aws_sdk_ec2.types.active_instance.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> ActiveInstanceSet:
    import aws_sdk_ec2.types.active_instance

    out: ActiveInstanceSet = []
    for child in parent.findall(tag):
        out.append(aws_sdk_ec2.types.active_instance.deserialize_ec2_query(child))
    return out
