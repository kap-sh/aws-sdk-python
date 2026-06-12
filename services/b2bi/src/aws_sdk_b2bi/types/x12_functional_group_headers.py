"""Generated from Smithy shape ``com.amazonaws.b2bi#X12FunctionalGroupHeaders``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_b2bi.types.x12_application_receiver_code
    import aws_sdk_b2bi.types.x12_application_sender_code
    import aws_sdk_b2bi.types.x12_responsible_agency_code


class X12FunctionalGroupHeaders(TypedDict):
    application_sender_code: NotRequired[
        "aws_sdk_b2bi.types.x12_application_sender_code.X12ApplicationSenderCode"
    ]
    """<p>A value representing the code used to identify the party transmitting a message, at position GS-02.</p>"""
    application_receiver_code: NotRequired[
        "aws_sdk_b2bi.types.x12_application_receiver_code.X12ApplicationReceiverCode"
    ]
    """<p>A value representing the code used to identify the party receiving a message, at position GS-03.</p>"""
    responsible_agency_code: NotRequired[
        "aws_sdk_b2bi.types.x12_responsible_agency_code.X12ResponsibleAgencyCode"
    ]
    """<p>A code that identifies the issuer of the standard, at position GS-07.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: X12FunctionalGroupHeaders) -> dict:
    out: dict = {}
    if "application_sender_code" in value:
        out["applicationSenderCode"] = value["application_sender_code"]
    if "application_receiver_code" in value:
        out["applicationReceiverCode"] = value["application_receiver_code"]
    if "responsible_agency_code" in value:
        out["responsibleAgencyCode"] = value["responsible_agency_code"]
    return out


def deserialize_aws_json_1_0(data: dict) -> X12FunctionalGroupHeaders:
    out: X12FunctionalGroupHeaders = {}  # type: ignore[typeddict-item]
    if "applicationSenderCode" in data:
        out["application_sender_code"] = data["applicationSenderCode"]
    if "applicationReceiverCode" in data:
        out["application_receiver_code"] = data["applicationReceiverCode"]
    if "responsibleAgencyCode" in data:
        out["responsible_agency_code"] = data["responsibleAgencyCode"]
    return out
