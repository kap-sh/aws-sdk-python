"""Generated from Smithy shape ``com.amazonaws.ec2#ReplaceNetworkAclAssociationResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class ReplaceNetworkAclAssociationResult(TypedDict):
    new_association_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the new association.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ReplaceNetworkAclAssociationResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "new_association_id" in value:
        pairs.append((f"{prefix}.NewAssociationId", str(value["new_association_id"])))


def deserialize_ec2_query(el: Element) -> ReplaceNetworkAclAssociationResult:
    out: ReplaceNetworkAclAssociationResult = {}  # type: ignore[typeddict-item]
    child_new_association_id = el.find("NewAssociationId")
    if child_new_association_id is not None:
        out["new_association_id"] = str(child_new_association_id.text or "")
    return out
