"""Generated from Smithy shape ``com.amazonaws.outposts#CreateRenewalInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_outposts.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_outposts.types.auto_fill_idempotency_token
    import aws_sdk_outposts.types.outpost_identifier
    import aws_sdk_outposts.types.payment_option
    import aws_sdk_outposts.types.payment_term


class CreateRenewalInput(TypedDict):
    payment_option: "aws_sdk_outposts.types.payment_option.PaymentOption"
    """<p>The payment option.</p>"""
    payment_term: "aws_sdk_outposts.types.payment_term.PaymentTerm"
    """<p>The payment term.</p>"""
    outpost_identifier: "aws_sdk_outposts.types.outpost_identifier.OutpostIdentifier"
    """<p>The ID or ARN of the Outpost.</p>"""
    client_token: NotRequired[
        "aws_sdk_outposts.types.auto_fill_idempotency_token.AutoFillIdempotencyToken"
    ]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateRenewalInput) -> dict:
    out: dict = {}
    import aws_sdk_outposts.types.payment_option

    out["PaymentOption"] = aws_sdk_outposts.types.payment_option.serialize_json(
        value["payment_option"]
    )
    import aws_sdk_outposts.types.payment_term

    out["PaymentTerm"] = aws_sdk_outposts.types.payment_term.serialize_json(
        value["payment_term"]
    )
    out["OutpostIdentifier"] = value["outpost_identifier"]
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateRenewalInput:
    out: CreateRenewalInput = {}  # type: ignore[typeddict-item]
    if "PaymentOption" in data:
        import aws_sdk_outposts.types.payment_option

        out["payment_option"] = aws_sdk_outposts.types.payment_option.deserialize_json(
            data["PaymentOption"]
        )
    else:
        raise DeserializationError("CreateRenewalInput.payment_option required")
    if "PaymentTerm" in data:
        import aws_sdk_outposts.types.payment_term

        out["payment_term"] = aws_sdk_outposts.types.payment_term.deserialize_json(
            data["PaymentTerm"]
        )
    else:
        raise DeserializationError("CreateRenewalInput.payment_term required")
    if "OutpostIdentifier" in data:
        out["outpost_identifier"] = data["OutpostIdentifier"]
    else:
        raise DeserializationError("CreateRenewalInput.outpost_identifier required")
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    return out
