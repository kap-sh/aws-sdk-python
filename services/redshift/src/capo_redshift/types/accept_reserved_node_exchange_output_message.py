"""Generated from Smithy shape ``com.amazonaws.redshift#AcceptReservedNodeExchangeOutputMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.reserved_node


class AcceptReservedNodeExchangeOutputMessage(TypedDict, closed=True):
    exchanged_reserved_node: NotRequired[
        "capo_redshift.types.reserved_node.ReservedNode"
    ]
    """<p></p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: AcceptReservedNodeExchangeOutputMessage,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "exchanged_reserved_node" in value:
        import capo_redshift.types.reserved_node

        capo_redshift.types.reserved_node.serialize_query(
            value["exchanged_reserved_node"], pairs, f"{prefix}.ExchangedReservedNode"
        )


def deserialize_query(el: Element) -> AcceptReservedNodeExchangeOutputMessage:
    out: AcceptReservedNodeExchangeOutputMessage = {}  # type: ignore[typeddict-item]
    child_exchanged_reserved_node = el.find("ExchangedReservedNode")
    if child_exchanged_reserved_node is not None:
        import capo_redshift.types.reserved_node

        out["exchanged_reserved_node"] = (
            capo_redshift.types.reserved_node.deserialize_query(
                child_exchanged_reserved_node
            )
        )
    return out
