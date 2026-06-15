"""Generated from Smithy shape ``com.amazonaws.b2bi#X12InterchangeControlHeaders``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_b2bi.types.x12_acknowledgment_requested_code
    import aws_sdk_b2bi.types.x12_id_qualifier
    import aws_sdk_b2bi.types.x12_receiver_id
    import aws_sdk_b2bi.types.x12_repetition_separator
    import aws_sdk_b2bi.types.x12_sender_id
    import aws_sdk_b2bi.types.x12_usage_indicator_code


class X12InterchangeControlHeaders(TypedDict):
    sender_id_qualifier: NotRequired[
        "aws_sdk_b2bi.types.x12_id_qualifier.X12IdQualifier"
    ]
    """<p>Located at position ISA-05 in the header. Qualifier for the sender ID. Together, the ID and qualifier uniquely identify the sending trading partner.</p>"""
    sender_id: NotRequired["aws_sdk_b2bi.types.x12_sender_id.X12SenderId"]
    """<p>Located at position ISA-06 in the header. This value (along with the <code>senderIdQualifier</code>) identifies the sender of the interchange. </p>"""
    receiver_id_qualifier: NotRequired[
        "aws_sdk_b2bi.types.x12_id_qualifier.X12IdQualifier"
    ]
    """<p>Located at position ISA-07 in the header. Qualifier for the receiver ID. Together, the ID and qualifier uniquely identify the receiving trading partner.</p>"""
    receiver_id: NotRequired["aws_sdk_b2bi.types.x12_receiver_id.X12ReceiverId"]
    """<p>Located at position ISA-08 in the header. This value (along with the <code>receiverIdQualifier</code>) identifies the intended recipient of the interchange. </p>"""
    repetition_separator: NotRequired[
        "aws_sdk_b2bi.types.x12_repetition_separator.X12RepetitionSeparator"
    ]
    r"""<p>Located at position ISA-11 in the header. This string makes it easier when you need to group similar adjacent element values together without using extra segments.</p> <note> <p>This parameter is only honored for version greater than 401 (<code>VERSION_4010</code> and higher).</p> <p>For versions less than 401, this field is called <a href=\"https://www.stedi.com/edi/x12-004010/segment/ISA#ISA-11\">StandardsId</a>, in which case our service sets the value to <code>U</code>.</p> </note>"""
    acknowledgment_requested_code: NotRequired[
        "aws_sdk_b2bi.types.x12_acknowledgment_requested_code.X12AcknowledgmentRequestedCode"
    ]
    r"""<p>Located at position ISA-14 in the header. The value \"1\" indicates that the sender is requesting an interchange acknowledgment at receipt of the interchange. The value \"0\" is used otherwise.</p>"""
    usage_indicator_code: NotRequired[
        "aws_sdk_b2bi.types.x12_usage_indicator_code.X12UsageIndicatorCode"
    ]
    """<p>Located at position ISA-15 in the header. Specifies how this interchange is being used:</p> <ul> <li> <p> <code>T</code> indicates this interchange is for testing.</p> </li> <li> <p> <code>P</code> indicates this interchange is for production.</p> </li> <li> <p> <code>I</code> indicates this interchange is informational.</p> </li> </ul>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: X12InterchangeControlHeaders) -> dict:
    out: dict = {}
    if "sender_id_qualifier" in value:
        out["senderIdQualifier"] = value["sender_id_qualifier"]
    if "sender_id" in value:
        out["senderId"] = value["sender_id"]
    if "receiver_id_qualifier" in value:
        out["receiverIdQualifier"] = value["receiver_id_qualifier"]
    if "receiver_id" in value:
        out["receiverId"] = value["receiver_id"]
    if "repetition_separator" in value:
        out["repetitionSeparator"] = value["repetition_separator"]
    if "acknowledgment_requested_code" in value:
        out["acknowledgmentRequestedCode"] = value["acknowledgment_requested_code"]
    if "usage_indicator_code" in value:
        out["usageIndicatorCode"] = value["usage_indicator_code"]
    return out


def deserialize_aws_json_1_0(data: dict) -> X12InterchangeControlHeaders:
    out: X12InterchangeControlHeaders = {}  # type: ignore[typeddict-item]
    if "senderIdQualifier" in data:
        out["sender_id_qualifier"] = data["senderIdQualifier"]
    if "senderId" in data:
        out["sender_id"] = data["senderId"]
    if "receiverIdQualifier" in data:
        out["receiver_id_qualifier"] = data["receiverIdQualifier"]
    if "receiverId" in data:
        out["receiver_id"] = data["receiverId"]
    if "repetitionSeparator" in data:
        out["repetition_separator"] = data["repetitionSeparator"]
    if "acknowledgmentRequestedCode" in data:
        out["acknowledgment_requested_code"] = data["acknowledgmentRequestedCode"]
    if "usageIndicatorCode" in data:
        out["usage_indicator_code"] = data["usageIndicatorCode"]
    return out
