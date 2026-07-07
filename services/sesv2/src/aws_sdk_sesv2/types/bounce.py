"""Generated from Smithy shape ``com.amazonaws.sesv2#Bounce``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.bounce_sub_type
    import aws_sdk_sesv2.types.bounce_type
    import aws_sdk_sesv2.types.diagnostic_code


class Bounce(TypedDict, closed=True):
    bounce_type: NotRequired["aws_sdk_sesv2.types.bounce_type.BounceType"]
    """<p>The type of the bounce, as determined by SES. Can be one of <code>UNDETERMINED</code>, <code>TRANSIENT</code>, or <code>PERMANENT</code> </p>"""
    bounce_sub_type: NotRequired["aws_sdk_sesv2.types.bounce_sub_type.BounceSubType"]
    """<p>The subtype of the bounce, as determined by SES.</p>"""
    diagnostic_code: NotRequired["aws_sdk_sesv2.types.diagnostic_code.DiagnosticCode"]
    """<p>The status code issued by the reporting Message Transfer Authority (MTA). This field only appears if a delivery status notification (DSN) was attached to the bounce and the <code>Diagnostic-Code</code> was provided in the DSN. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Bounce) -> dict:
    out: dict = {}
    if "bounce_type" in value:
        import aws_sdk_sesv2.types.bounce_type

        out["BounceType"] = aws_sdk_sesv2.types.bounce_type.serialize_json(
            value["bounce_type"]
        )
    if "bounce_sub_type" in value:
        out["BounceSubType"] = value["bounce_sub_type"]
    if "diagnostic_code" in value:
        out["DiagnosticCode"] = value["diagnostic_code"]
    return out


def deserialize_json(data: dict) -> Bounce:
    out: Bounce = {}  # type: ignore[typeddict-item]
    if "BounceType" in data:
        import aws_sdk_sesv2.types.bounce_type

        out["bounce_type"] = aws_sdk_sesv2.types.bounce_type.deserialize_json(
            data["BounceType"]
        )
    if "BounceSubType" in data:
        out["bounce_sub_type"] = data["BounceSubType"]
    if "DiagnosticCode" in data:
        out["diagnostic_code"] = data["DiagnosticCode"]
    return out
