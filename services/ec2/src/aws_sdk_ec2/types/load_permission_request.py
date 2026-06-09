"""Generated from Smithy shape ``com.amazonaws.ec2#LoadPermissionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.permission_group
    import aws_sdk_ec2.types.string


class LoadPermissionRequest(TypedDict):
    group: NotRequired["aws_sdk_ec2.types.permission_group.PermissionGroup"]
    """<p>The name of the group.</p>"""
    user_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Web Services account ID.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: LoadPermissionRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "group" in value:
        import aws_sdk_ec2.types.permission_group

        aws_sdk_ec2.types.permission_group.serialize_ec2_query(
            value["group"], pairs, f"{prefix}.Group"
        )
    if "user_id" in value:
        pairs.append((f"{prefix}.UserId", str(value["user_id"])))


def deserialize_ec2_query(el: Element) -> LoadPermissionRequest:
    out: LoadPermissionRequest = {}  # type: ignore[typeddict-item]
    child_group = el.find("Group")
    if child_group is not None:
        import aws_sdk_ec2.types.permission_group

        out["group"] = aws_sdk_ec2.types.permission_group.deserialize_ec2_query(
            child_group
        )
    child_user_id = el.find("UserId")
    if child_user_id is not None:
        out["user_id"] = str(child_user_id.text or "")
    return out
