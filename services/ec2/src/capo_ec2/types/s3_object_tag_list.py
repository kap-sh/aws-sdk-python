"""Generated from Smithy shape ``com.amazonaws.ec2#S3ObjectTagList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.s3_object_tag

S3ObjectTagList: TypeAlias = list["capo_ec2.types.s3_object_tag.S3ObjectTag"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: S3ObjectTagList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.s3_object_tag

        capo_ec2.types.s3_object_tag.serialize_ec2_query(item, pairs, f"{prefix}.{n}")


def deserialize_ec2_query(el: Element) -> S3ObjectTagList:
    import capo_ec2.types.s3_object_tag

    out: S3ObjectTagList = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.s3_object_tag.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> S3ObjectTagList:
    import capo_ec2.types.s3_object_tag

    out: S3ObjectTagList = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.s3_object_tag.deserialize_ec2_query(child))
    return out
