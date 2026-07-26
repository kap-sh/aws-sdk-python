"""Generated from Smithy shape ``com.amazonaws.organizations#UpdateResponsibilityTransferRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_organizations.errors import DeserializationError

if TYPE_CHECKING:
    import capo_organizations.types.responsibility_transfer_id
    import capo_organizations.types.responsibility_transfer_name


class UpdateResponsibilityTransferRequest(TypedDict, closed=True):
    id: "capo_organizations.types.responsibility_transfer_id.ResponsibilityTransferId"
    """<p>ID for the transfer.</p>"""
    name: "capo_organizations.types.responsibility_transfer_name.ResponsibilityTransferName"
    """<p>New name you want to assign to the transfer.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateResponsibilityTransferRequest) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    out["Name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateResponsibilityTransferRequest:
    out: UpdateResponsibilityTransferRequest = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("UpdateResponsibilityTransferRequest.id required")
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("UpdateResponsibilityTransferRequest.name required")
    return out
