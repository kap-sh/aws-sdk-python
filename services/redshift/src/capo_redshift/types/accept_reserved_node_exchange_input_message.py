"""Generated from Smithy shape ``com.amazonaws.redshift#AcceptReservedNodeExchangeInputMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.string


class AcceptReservedNodeExchangeInputMessage(TypedDict, closed=True):
    reserved_node_id: NotRequired["capo_redshift.types.string.String"]
    """<p>A string representing the node identifier of the DC1 Reserved Node to be exchanged.</p>"""
    target_reserved_node_offering_id: NotRequired["capo_redshift.types.string.String"]
    """<p>The unique identifier of the DC2 Reserved Node offering to be used for the exchange. You can obtain the value for the parameter by calling <a>GetReservedNodeExchangeOfferings</a> </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: AcceptReservedNodeExchangeInputMessage,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "reserved_node_id" in value:
        pairs.append((f"{prefix}.ReservedNodeId", str(value["reserved_node_id"])))
    if "target_reserved_node_offering_id" in value:
        pairs.append(
            (
                f"{prefix}.TargetReservedNodeOfferingId",
                str(value["target_reserved_node_offering_id"]),
            )
        )


def deserialize_query(el: Element) -> AcceptReservedNodeExchangeInputMessage:
    out: AcceptReservedNodeExchangeInputMessage = {}  # type: ignore[typeddict-item]
    child_reserved_node_id = el.find("ReservedNodeId")
    if child_reserved_node_id is not None:
        out["reserved_node_id"] = str(child_reserved_node_id.text or "")
    child_target_reserved_node_offering_id = el.find("TargetReservedNodeOfferingId")
    if child_target_reserved_node_offering_id is not None:
        out["target_reserved_node_offering_id"] = str(
            child_target_reserved_node_offering_id.text or ""
        )
    return out
