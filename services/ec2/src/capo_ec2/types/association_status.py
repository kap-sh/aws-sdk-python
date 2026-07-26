"""Generated from Smithy shape ``com.amazonaws.ec2#AssociationStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.association_status_code
    import capo_ec2.types.string


class AssociationStatus(TypedDict, closed=True):
    code: NotRequired["capo_ec2.types.association_status_code.AssociationStatusCode"]
    """<p>The state of the target network association.</p>"""
    message: NotRequired["capo_ec2.types.string.String"]
    """<p>A message about the status of the target network association, if applicable.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AssociationStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "code" in value:
        import capo_ec2.types.association_status_code

        capo_ec2.types.association_status_code.serialize_ec2_query(
            value["code"], pairs, f"{prefix}.Code"
        )
    if "message" in value:
        pairs.append((f"{prefix}.Message", str(value["message"])))


def deserialize_ec2_query(el: Element) -> AssociationStatus:
    out: AssociationStatus = {}  # type: ignore[typeddict-item]
    child_code = el.find("Code")
    if child_code is not None:
        import capo_ec2.types.association_status_code

        out["code"] = capo_ec2.types.association_status_code.deserialize_ec2_query(
            child_code
        )
    child_message = el.find("Message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out
