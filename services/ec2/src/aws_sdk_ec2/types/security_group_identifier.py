"""Generated from Smithy shape ``com.amazonaws.ec2#SecurityGroupIdentifier``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class SecurityGroupIdentifier(TypedDict):
    group_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the security group.</p>"""
    group_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The name of the security group.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: SecurityGroupIdentifier, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "group_id" in value:
        pairs.append((f"{prefix}.GroupId", str(value["group_id"])))
    if "group_name" in value:
        pairs.append((f"{prefix}.GroupName", str(value["group_name"])))


def deserialize_ec2_query(el: Element) -> SecurityGroupIdentifier:
    out: SecurityGroupIdentifier = {}  # type: ignore[typeddict-item]
    child_group_id = el.find("GroupId")
    if child_group_id is not None:
        out["group_id"] = str(child_group_id.text or "")
    child_group_name = el.find("GroupName")
    if child_group_name is not None:
        out["group_name"] = str(child_group_name.text or "")
    return out
