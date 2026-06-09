"""Generated from Smithy shape ``com.amazonaws.ec2#AccessScopePathList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.access_scope_path

AccessScopePathList: TypeAlias = list[
    "aws_sdk_ec2.types.access_scope_path.AccessScopePath"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AccessScopePathList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.access_scope_path

        aws_sdk_ec2.types.access_scope_path.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> AccessScopePathList:
    import aws_sdk_ec2.types.access_scope_path

    out: AccessScopePathList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_ec2.types.access_scope_path.deserialize_ec2_query(child))
    return out
