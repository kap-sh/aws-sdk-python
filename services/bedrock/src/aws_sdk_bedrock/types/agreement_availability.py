"""Generated from Smithy shape ``com.amazonaws.bedrock#AgreementAvailability``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.agreement_status


class AgreementAvailability(TypedDict, closed=True):
    status: "aws_sdk_bedrock.types.agreement_status.AgreementStatus"
    """<p>Status of the agreement.</p>"""
    error_message: NotRequired["str"]
    """<p>Error message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AgreementAvailability) -> dict:
    out: dict = {}
    import aws_sdk_bedrock.types.agreement_status

    out["status"] = aws_sdk_bedrock.types.agreement_status.serialize_json(
        value["status"]
    )
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    return out


def deserialize_json(data: dict) -> AgreementAvailability:
    out: AgreementAvailability = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import aws_sdk_bedrock.types.agreement_status

        out["status"] = aws_sdk_bedrock.types.agreement_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("AgreementAvailability.status required")
    if "errorMessage" in data:
        out["error_message"] = data["errorMessage"]
    return out
