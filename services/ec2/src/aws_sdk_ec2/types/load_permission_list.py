"""Generated from Smithy shape ``com.amazonaws.ec2#LoadPermissionList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.load_permission

LoadPermissionList: TypeAlias = list["aws_sdk_ec2.types.load_permission.LoadPermission"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: LoadPermissionList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.load_permission

        aws_sdk_ec2.types.load_permission.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> LoadPermissionList:
    import aws_sdk_ec2.types.load_permission

    out: LoadPermissionList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_ec2.types.load_permission.deserialize_ec2_query(child))
    return out
