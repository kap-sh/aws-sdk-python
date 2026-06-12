"""Generated from Smithy shape ``com.amazonaws.b2bi#X12Envelope``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_b2bi.types.wrap_options
    import aws_sdk_b2bi.types.x12_outbound_edi_headers


class X12Envelope(TypedDict):
    common: NotRequired[
        "aws_sdk_b2bi.types.x12_outbound_edi_headers.X12OutboundEdiHeaders"
    ]
    """<p>A container for the X12 outbound EDI headers.</p>"""
    wrap_options: NotRequired["aws_sdk_b2bi.types.wrap_options.WrapOptions"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: X12Envelope) -> dict:
    out: dict = {}
    if "common" in value:
        import aws_sdk_b2bi.types.x12_outbound_edi_headers

        out["common"] = (
            aws_sdk_b2bi.types.x12_outbound_edi_headers.serialize_aws_json_1_0(
                value["common"]
            )
        )
    if "wrap_options" in value:
        import aws_sdk_b2bi.types.wrap_options

        out["wrapOptions"] = aws_sdk_b2bi.types.wrap_options.serialize_aws_json_1_0(
            value["wrap_options"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> X12Envelope:
    out: X12Envelope = {}  # type: ignore[typeddict-item]
    if "common" in data:
        import aws_sdk_b2bi.types.x12_outbound_edi_headers

        out["common"] = (
            aws_sdk_b2bi.types.x12_outbound_edi_headers.deserialize_aws_json_1_0(
                data["common"]
            )
        )
    if "wrapOptions" in data:
        import aws_sdk_b2bi.types.wrap_options

        out["wrap_options"] = aws_sdk_b2bi.types.wrap_options.deserialize_aws_json_1_0(
            data["wrapOptions"]
        )
    return out
