"""Generated from Smithy shape ``com.amazonaws.rtbfabric#LinkAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rtbfabric.types.customer_provided_id
    import capo_rtbfabric.types.responder_error_masking


class LinkAttributes(TypedDict, closed=True):
    responder_error_masking: NotRequired[
        "capo_rtbfabric.types.responder_error_masking.ResponderErrorMasking"
    ]
    """<p>Describes the masking for HTTP error codes.</p>"""
    customer_provided_id: NotRequired[
        "capo_rtbfabric.types.customer_provided_id.CustomerProvidedId"
    ]
    """<p>The customer-provided unique identifier of the link.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LinkAttributes) -> dict:
    out: dict = {}
    if "responder_error_masking" in value:
        import capo_rtbfabric.types.responder_error_masking

        out["responderErrorMasking"] = (
            capo_rtbfabric.types.responder_error_masking.serialize_json(
                value["responder_error_masking"]
            )
        )
    if "customer_provided_id" in value:
        out["customerProvidedId"] = value["customer_provided_id"]
    return out


def deserialize_json(data: dict) -> LinkAttributes:
    out: LinkAttributes = {}  # type: ignore[typeddict-item]
    if "responderErrorMasking" in data:
        import capo_rtbfabric.types.responder_error_masking

        out["responder_error_masking"] = (
            capo_rtbfabric.types.responder_error_masking.deserialize_json(
                data["responderErrorMasking"]
            )
        )
    if "customerProvidedId" in data:
        out["customer_provided_id"] = data["customerProvidedId"]
    return out
