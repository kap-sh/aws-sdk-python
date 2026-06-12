"""Generated from Smithy shape ``com.amazonaws.transfer#DeleteAgreementRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_transfer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_transfer.types.agreement_id
    import aws_sdk_transfer.types.server_id


class DeleteAgreementRequest(TypedDict):
    agreement_id: "aws_sdk_transfer.types.agreement_id.AgreementId"
    """<p>A unique identifier for the agreement. This identifier is returned when you create an agreement.</p>"""
    server_id: "aws_sdk_transfer.types.server_id.ServerId"
    """<p>The server identifier associated with the agreement that you are deleting.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteAgreementRequest) -> dict:
    out: dict = {}
    out["AgreementId"] = value["agreement_id"]
    out["ServerId"] = value["server_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteAgreementRequest:
    out: DeleteAgreementRequest = {}  # type: ignore[typeddict-item]
    if "AgreementId" in data:
        out["agreement_id"] = data["AgreementId"]
    else:
        raise DeserializationError("DeleteAgreementRequest.agreement_id required")
    if "ServerId" in data:
        out["server_id"] = data["ServerId"]
    else:
        raise DeserializationError("DeleteAgreementRequest.server_id required")
    return out
