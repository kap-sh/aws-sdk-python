"""Generated from Smithy shape ``com.amazonaws.ec2#AlternatePathHintList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.alternate_path_hint

AlternatePathHintList: TypeAlias = list[
    "aws_sdk_ec2.types.alternate_path_hint.AlternatePathHint"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AlternatePathHintList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.alternate_path_hint

        aws_sdk_ec2.types.alternate_path_hint.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> AlternatePathHintList:
    import aws_sdk_ec2.types.alternate_path_hint

    out: AlternatePathHintList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_ec2.types.alternate_path_hint.deserialize_ec2_query(child))
    return out
