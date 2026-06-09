"""Generated from Smithy shape ``com.amazonaws.ec2#KeyPairList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.key_pair_info

KeyPairList: TypeAlias = list["aws_sdk_ec2.types.key_pair_info.KeyPairInfo"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: KeyPairList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.key_pair_info

        aws_sdk_ec2.types.key_pair_info.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> KeyPairList:
    import aws_sdk_ec2.types.key_pair_info

    out: KeyPairList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_ec2.types.key_pair_info.deserialize_ec2_query(child))
    return out
