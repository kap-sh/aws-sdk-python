"""Generated from Smithy shape ``com.amazonaws.b2bi#X12AcknowledgmentOptions``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_b2bi.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_b2bi.types.x12_functional_acknowledgment
    import aws_sdk_b2bi.types.x12_technical_acknowledgment


class X12AcknowledgmentOptions(TypedDict):
    functional_acknowledgment: (
        "aws_sdk_b2bi.types.x12_functional_acknowledgment.X12FunctionalAcknowledgment"
    )
    """<p>Specifies whether functional acknowledgments (997/999) should be generated for incoming X12 transactions. Valid values are <code>DO_NOT_GENERATE</code>, <code>GENERATE_ALL_SEGMENTS</code> and <code>GENERATE_WITHOUT_TRANSACTION_SET_RESPONSE_LOOP</code>.</p> <p>If you choose <code>GENERATE_WITHOUT_TRANSACTION_SET_RESPONSE_LOOP</code>, Amazon Web Services B2B Data Interchange skips the AK2_Loop when generating an acknowledgment document.</p>"""
    technical_acknowledgment: (
        "aws_sdk_b2bi.types.x12_technical_acknowledgment.X12TechnicalAcknowledgment"
    )
    """<p>Specifies whether technical acknowledgments (TA1) should be generated for incoming X12 interchanges. Valid values are <code>DO_NOT_GENERATE</code> and <code>GENERATE_ALL_SEGMENTS</code> and.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: X12AcknowledgmentOptions) -> dict:
    out: dict = {}
    import aws_sdk_b2bi.types.x12_functional_acknowledgment

    out["functionalAcknowledgment"] = (
        aws_sdk_b2bi.types.x12_functional_acknowledgment.serialize_aws_json_1_0(
            value["functional_acknowledgment"]
        )
    )
    import aws_sdk_b2bi.types.x12_technical_acknowledgment

    out["technicalAcknowledgment"] = (
        aws_sdk_b2bi.types.x12_technical_acknowledgment.serialize_aws_json_1_0(
            value["technical_acknowledgment"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> X12AcknowledgmentOptions:
    out: X12AcknowledgmentOptions = {}  # type: ignore[typeddict-item]
    if "functionalAcknowledgment" in data:
        import aws_sdk_b2bi.types.x12_functional_acknowledgment

        out["functional_acknowledgment"] = (
            aws_sdk_b2bi.types.x12_functional_acknowledgment.deserialize_aws_json_1_0(
                data["functionalAcknowledgment"]
            )
        )
    else:
        raise DeserializationError(
            "X12AcknowledgmentOptions.functional_acknowledgment required"
        )
    if "technicalAcknowledgment" in data:
        import aws_sdk_b2bi.types.x12_technical_acknowledgment

        out["technical_acknowledgment"] = (
            aws_sdk_b2bi.types.x12_technical_acknowledgment.deserialize_aws_json_1_0(
                data["technicalAcknowledgment"]
            )
        )
    else:
        raise DeserializationError(
            "X12AcknowledgmentOptions.technical_acknowledgment required"
        )
    return out
