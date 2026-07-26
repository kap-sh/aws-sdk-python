"""Generated from Smithy shape ``com.amazonaws.b2bi#X12Envelope``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_b2bi.types.wrap_options
    import capo_b2bi.types.x12_outbound_edi_headers


class X12Envelope(TypedDict, closed=True):
    common: NotRequired[
        "capo_b2bi.types.x12_outbound_edi_headers.X12OutboundEdiHeaders"
    ]
    """<p>A container for the X12 outbound EDI headers.</p>"""
    wrap_options: NotRequired["capo_b2bi.types.wrap_options.WrapOptions"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: X12Envelope) -> dict:
    out: dict = {}
    if "common" in value:
        import capo_b2bi.types.x12_outbound_edi_headers

        out["common"] = capo_b2bi.types.x12_outbound_edi_headers.serialize_aws_json_1_0(
            value["common"]
        )
    if "wrap_options" in value:
        import capo_b2bi.types.wrap_options

        out["wrapOptions"] = capo_b2bi.types.wrap_options.serialize_aws_json_1_0(
            value["wrap_options"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> X12Envelope:
    out: X12Envelope = {}  # type: ignore[typeddict-item]
    if "common" in data:
        import capo_b2bi.types.x12_outbound_edi_headers

        out["common"] = (
            capo_b2bi.types.x12_outbound_edi_headers.deserialize_aws_json_1_0(
                data["common"]
            )
        )
    if "wrapOptions" in data:
        import capo_b2bi.types.wrap_options

        out["wrap_options"] = capo_b2bi.types.wrap_options.deserialize_aws_json_1_0(
            data["wrapOptions"]
        )
    return out
