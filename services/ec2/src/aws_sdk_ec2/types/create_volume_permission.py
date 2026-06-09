"""Generated from Smithy shape ``com.amazonaws.ec2#CreateVolumePermission``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.permission_group
    import aws_sdk_ec2.types.string


class CreateVolumePermission(TypedDict):
    user_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Amazon Web Services account to be added or removed.</p>"""
    group: NotRequired["aws_sdk_ec2.types.permission_group.PermissionGroup"]
    """<p>The group to be added or removed. The possible value is <code>all</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateVolumePermission, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "user_id" in value:
        pairs.append((f"{prefix}.UserId", str(value["user_id"])))
    if "group" in value:
        import aws_sdk_ec2.types.permission_group

        aws_sdk_ec2.types.permission_group.serialize_ec2_query(
            value["group"], pairs, f"{prefix}.Group"
        )


def deserialize_ec2_query(el: Element) -> CreateVolumePermission:
    out: CreateVolumePermission = {}  # type: ignore[typeddict-item]
    child_user_id = el.find("UserId")
    if child_user_id is not None:
        out["user_id"] = str(child_user_id.text or "")
    child_group = el.find("Group")
    if child_group is not None:
        import aws_sdk_ec2.types.permission_group

        out["group"] = aws_sdk_ec2.types.permission_group.deserialize_ec2_query(
            child_group
        )
    return out
