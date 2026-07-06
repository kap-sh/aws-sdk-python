"""Generated from Smithy shape ``com.amazonaws.organizations#DescribeResponsibilityTransferRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_organizations.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_organizations.types.responsibility_transfer_id


class DescribeResponsibilityTransferRequest(TypedDict, closed=True):
    id: "aws_sdk_organizations.types.responsibility_transfer_id.ResponsibilityTransferId"
    """<p>ID for the transfer.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeResponsibilityTransferRequest) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeResponsibilityTransferRequest:
    out: DescribeResponsibilityTransferRequest = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("DescribeResponsibilityTransferRequest.id required")
    return out
