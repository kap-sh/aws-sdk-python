"""Generated from Smithy shape ``com.amazonaws.b2bi#InboundEdiOptions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_b2bi.types.x12_inbound_edi_options


class InboundEdiOptions(TypedDict):
    x12: NotRequired["aws_sdk_b2bi.types.x12_inbound_edi_options.X12InboundEdiOptions"]
    """<p>A structure that contains X12-specific options for processing inbound X12 EDI files.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InboundEdiOptions) -> dict:
    out: dict = {}
    if "x12" in value:
        import aws_sdk_b2bi.types.x12_inbound_edi_options

        out["x12"] = aws_sdk_b2bi.types.x12_inbound_edi_options.serialize_aws_json_1_0(
            value["x12"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> InboundEdiOptions:
    out: InboundEdiOptions = {}  # type: ignore[typeddict-item]
    if "x12" in data:
        import aws_sdk_b2bi.types.x12_inbound_edi_options

        out["x12"] = (
            aws_sdk_b2bi.types.x12_inbound_edi_options.deserialize_aws_json_1_0(
                data["x12"]
            )
        )
    return out
