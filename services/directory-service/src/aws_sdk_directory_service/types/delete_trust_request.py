"""Generated from Smithy shape ``com.amazonaws.directoryservice#DeleteTrustRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_directory_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_directory_service.types.delete_associated_conditional_forwarder
    import aws_sdk_directory_service.types.trust_id


class DeleteTrustRequest(TypedDict):
    trust_id: "aws_sdk_directory_service.types.trust_id.TrustId"
    """<p>The Trust ID of the trust relationship to be deleted.</p>"""
    delete_associated_conditional_forwarder: "aws_sdk_directory_service.types.delete_associated_conditional_forwarder.DeleteAssociatedConditionalForwarder"
    """<p>Delete a conditional forwarder as part of a DeleteTrustRequest.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteTrustRequest) -> dict:
    out: dict = {}
    out["TrustId"] = value["trust_id"]
    out["DeleteAssociatedConditionalForwarder"] = value.get(
        "delete_associated_conditional_forwarder", False
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteTrustRequest:
    out: DeleteTrustRequest = {}  # type: ignore[typeddict-item]
    if "TrustId" in data:
        out["trust_id"] = data["TrustId"]
    else:
        raise DeserializationError("DeleteTrustRequest.trust_id required")
    if "DeleteAssociatedConditionalForwarder" in data:
        out["delete_associated_conditional_forwarder"] = data[
            "DeleteAssociatedConditionalForwarder"
        ]
    else:
        out["delete_associated_conditional_forwarder"] = False
    return out
