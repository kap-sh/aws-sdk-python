"""Generated from Smithy shape ``com.amazonaws.outposts#CreateOrderInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_outposts.errors import DeserializationError

if TYPE_CHECKING:
    import capo_outposts.types.line_item_request_list_definition
    import capo_outposts.types.outpost_identifier
    import capo_outposts.types.payment_option
    import capo_outposts.types.payment_term


class CreateOrderInput(TypedDict, closed=True):
    outpost_identifier: "capo_outposts.types.outpost_identifier.OutpostIdentifier"
    """<p> The ID or the Amazon Resource Name (ARN) of the Outpost. </p>"""
    line_items: NotRequired[
        "capo_outposts.types.line_item_request_list_definition.LineItemRequestListDefinition"
    ]
    """<p>The line items that make up the order.</p>"""
    payment_option: "capo_outposts.types.payment_option.PaymentOption"
    """<p>The payment option.</p>"""
    payment_term: NotRequired["capo_outposts.types.payment_term.PaymentTerm"]
    """<p>The payment terms.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateOrderInput) -> dict:
    out: dict = {}
    out["OutpostIdentifier"] = value["outpost_identifier"]
    if "line_items" in value:
        import capo_outposts.types.line_item_request_list_definition

        out["LineItems"] = (
            capo_outposts.types.line_item_request_list_definition.serialize_json(
                value["line_items"]
            )
        )
    import capo_outposts.types.payment_option

    out["PaymentOption"] = capo_outposts.types.payment_option.serialize_json(
        value["payment_option"]
    )
    if "payment_term" in value:
        import capo_outposts.types.payment_term

        out["PaymentTerm"] = capo_outposts.types.payment_term.serialize_json(
            value["payment_term"]
        )
    return out


def deserialize_json(data: dict) -> CreateOrderInput:
    out: CreateOrderInput = {}  # type: ignore[typeddict-item]
    if "OutpostIdentifier" in data:
        out["outpost_identifier"] = data["OutpostIdentifier"]
    else:
        raise DeserializationError("CreateOrderInput.outpost_identifier required")
    if "LineItems" in data:
        import capo_outposts.types.line_item_request_list_definition

        out["line_items"] = (
            capo_outposts.types.line_item_request_list_definition.deserialize_json(
                data["LineItems"]
            )
        )
    if "PaymentOption" in data:
        import capo_outposts.types.payment_option

        out["payment_option"] = capo_outposts.types.payment_option.deserialize_json(
            data["PaymentOption"]
        )
    else:
        raise DeserializationError("CreateOrderInput.payment_option required")
    if "PaymentTerm" in data:
        import capo_outposts.types.payment_term

        out["payment_term"] = capo_outposts.types.payment_term.deserialize_json(
            data["PaymentTerm"]
        )
    return out
