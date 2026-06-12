"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancing#SourceSecurityGroup``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elastic_load_balancing._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_load_balancing.types.security_group_name
    import aws_sdk_elastic_load_balancing.types.security_group_owner_alias


class SourceSecurityGroup(TypedDict):
    owner_alias: NotRequired[
        "aws_sdk_elastic_load_balancing.types.security_group_owner_alias.SecurityGroupOwnerAlias"
    ]
    """<p>The owner of the security group.</p>"""
    group_name: NotRequired[
        "aws_sdk_elastic_load_balancing.types.security_group_name.SecurityGroupName"
    ]
    """<p>The name of the security group.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: SourceSecurityGroup, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "owner_alias" in value:
        pairs.append((f"{prefix}.OwnerAlias", str(value["owner_alias"])))
    if "group_name" in value:
        pairs.append((f"{prefix}.GroupName", str(value["group_name"])))


def deserialize_query(el: Element) -> SourceSecurityGroup:
    out: SourceSecurityGroup = {}  # type: ignore[typeddict-item]
    child_owner_alias = el.find("OwnerAlias")
    if child_owner_alias is not None:
        out["owner_alias"] = str(child_owner_alias.text or "")
    child_group_name = el.find("GroupName")
    if child_group_name is not None:
        out["group_name"] = str(child_group_name.text or "")
    return out
