"""Generated from Smithy shape ``com.amazonaws.ec2#AssociateAddressResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.string


class AssociateAddressResult(TypedDict, closed=True):
    association_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID that represents the association of the Elastic IP address with an instance.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AssociateAddressResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "association_id" in value:
        pairs.append((f"{prefix}.AssociationId", str(value["association_id"])))


def deserialize_ec2_query(el: Element) -> AssociateAddressResult:
    out: AssociateAddressResult = {}  # type: ignore[typeddict-item]
    child_association_id = el.find("AssociationId")
    if child_association_id is not None:
        out["association_id"] = str(child_association_id.text or "")
    return out
