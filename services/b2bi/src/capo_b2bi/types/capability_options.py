"""Generated from Smithy shape ``com.amazonaws.b2bi#CapabilityOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_b2bi.types.inbound_edi_options
    import capo_b2bi.types.outbound_edi_options


class CapabilityOptions(TypedDict, closed=True):
    outbound_edi: NotRequired["capo_b2bi.types.outbound_edi_options.OutboundEdiOptions"]
    """<p>A structure that contains the outbound EDI options.</p>"""
    inbound_edi: NotRequired["capo_b2bi.types.inbound_edi_options.InboundEdiOptions"]
    """<p>A structure that contains the inbound EDI options for the capability.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CapabilityOptions) -> dict:
    out: dict = {}
    if "outbound_edi" in value:
        import capo_b2bi.types.outbound_edi_options

        out["outboundEdi"] = (
            capo_b2bi.types.outbound_edi_options.serialize_aws_json_1_0(
                value["outbound_edi"]
            )
        )
    if "inbound_edi" in value:
        import capo_b2bi.types.inbound_edi_options

        out["inboundEdi"] = capo_b2bi.types.inbound_edi_options.serialize_aws_json_1_0(
            value["inbound_edi"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CapabilityOptions:
    out: CapabilityOptions = {}  # type: ignore[typeddict-item]
    if "outboundEdi" in data:
        import capo_b2bi.types.outbound_edi_options

        out["outbound_edi"] = (
            capo_b2bi.types.outbound_edi_options.deserialize_aws_json_1_0(
                data["outboundEdi"]
            )
        )
    if "inboundEdi" in data:
        import capo_b2bi.types.inbound_edi_options

        out["inbound_edi"] = (
            capo_b2bi.types.inbound_edi_options.deserialize_aws_json_1_0(
                data["inboundEdi"]
            )
        )
    return out
