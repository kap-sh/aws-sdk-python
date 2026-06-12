"""Generated from Smithy shape ``com.amazonaws.b2bi#X12InboundEdiOptions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_b2bi.types.x12_acknowledgment_options


class X12InboundEdiOptions(TypedDict):
    acknowledgment_options: NotRequired[
        "aws_sdk_b2bi.types.x12_acknowledgment_options.X12AcknowledgmentOptions"
    ]
    """<p>Specifies acknowledgment options for inbound X12 EDI files. These options control how functional and technical acknowledgments are handled.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: X12InboundEdiOptions) -> dict:
    out: dict = {}
    if "acknowledgment_options" in value:
        import aws_sdk_b2bi.types.x12_acknowledgment_options

        out["acknowledgmentOptions"] = (
            aws_sdk_b2bi.types.x12_acknowledgment_options.serialize_aws_json_1_0(
                value["acknowledgment_options"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> X12InboundEdiOptions:
    out: X12InboundEdiOptions = {}  # type: ignore[typeddict-item]
    if "acknowledgmentOptions" in data:
        import aws_sdk_b2bi.types.x12_acknowledgment_options

        out["acknowledgment_options"] = (
            aws_sdk_b2bi.types.x12_acknowledgment_options.deserialize_aws_json_1_0(
                data["acknowledgmentOptions"]
            )
        )
    return out
