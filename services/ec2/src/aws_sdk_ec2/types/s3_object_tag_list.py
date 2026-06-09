"""Generated from Smithy shape ``com.amazonaws.ec2#S3ObjectTagList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.s3_object_tag

S3ObjectTagList: TypeAlias = list["aws_sdk_ec2.types.s3_object_tag.S3ObjectTag"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: S3ObjectTagList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.s3_object_tag

        aws_sdk_ec2.types.s3_object_tag.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> S3ObjectTagList:
    import aws_sdk_ec2.types.s3_object_tag

    out: S3ObjectTagList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_ec2.types.s3_object_tag.deserialize_ec2_query(child))
    return out
