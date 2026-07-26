"""Generated from Smithy shape ``com.amazonaws.b2bi#X12InboundEdiOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_b2bi.types.x12_acknowledgment_options


class X12InboundEdiOptions(TypedDict, closed=True):
    acknowledgment_options: NotRequired[
        "capo_b2bi.types.x12_acknowledgment_options.X12AcknowledgmentOptions"
    ]
    """<p>Specifies acknowledgment options for inbound X12 EDI files. These options control how functional and technical acknowledgments are handled.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: X12InboundEdiOptions) -> dict:
    out: dict = {}
    if "acknowledgment_options" in value:
        import capo_b2bi.types.x12_acknowledgment_options

        out["acknowledgmentOptions"] = (
            capo_b2bi.types.x12_acknowledgment_options.serialize_aws_json_1_0(
                value["acknowledgment_options"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> X12InboundEdiOptions:
    out: X12InboundEdiOptions = {}  # type: ignore[typeddict-item]
    if "acknowledgmentOptions" in data:
        import capo_b2bi.types.x12_acknowledgment_options

        out["acknowledgment_options"] = (
            capo_b2bi.types.x12_acknowledgment_options.deserialize_aws_json_1_0(
                data["acknowledgmentOptions"]
            )
        )
    return out
