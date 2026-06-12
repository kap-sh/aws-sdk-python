"""Generated from Smithy shape ``com.amazonaws.organizations#TerminateResponsibilityTransferRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_organizations.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_organizations.types.responsibility_transfer_id
    import aws_sdk_organizations.types.timestamp


class TerminateResponsibilityTransferRequest(TypedDict):
    id: "aws_sdk_organizations.types.responsibility_transfer_id.ResponsibilityTransferId"
    """<p>ID for the transfer.</p>"""
    end_timestamp: NotRequired["aws_sdk_organizations.types.timestamp.Timestamp"]
    """<p>Timestamp when the responsibility transfer is to end.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TerminateResponsibilityTransferRequest) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    if "end_timestamp" in value:
        import aws_sdk_organizations.types.timestamp

        out["EndTimestamp"] = (
            aws_sdk_organizations.types.timestamp.serialize_aws_json_1_1(
                value["end_timestamp"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TerminateResponsibilityTransferRequest:
    out: TerminateResponsibilityTransferRequest = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("TerminateResponsibilityTransferRequest.id required")
    if "EndTimestamp" in data:
        import aws_sdk_organizations.types.timestamp

        out["end_timestamp"] = (
            aws_sdk_organizations.types.timestamp.deserialize_aws_json_1_1(
                data["EndTimestamp"]
            )
        )
    return out
