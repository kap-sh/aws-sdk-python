"""Generated from Smithy shape ``com.amazonaws.transfer#CreateAccessResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_transfer.errors import DeserializationError

if TYPE_CHECKING:
    import capo_transfer.types.external_id
    import capo_transfer.types.server_id


class CreateAccessResponse(TypedDict, closed=True):
    server_id: "capo_transfer.types.server_id.ServerId"
    """<p>The identifier of the server that the user is attached to.</p>"""
    external_id: "capo_transfer.types.external_id.ExternalId"
    """<p>The external identifier of the group whose users have access to your Amazon S3 or Amazon EFS resources over the enabled protocols using Transfer Family.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateAccessResponse) -> dict:
    out: dict = {}
    out["ServerId"] = value["server_id"]
    out["ExternalId"] = value["external_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateAccessResponse:
    out: CreateAccessResponse = {}  # type: ignore[typeddict-item]
    if "ServerId" in data:
        out["server_id"] = data["ServerId"]
    else:
        raise DeserializationError("CreateAccessResponse.server_id required")
    if "ExternalId" in data:
        out["external_id"] = data["ExternalId"]
    else:
        raise DeserializationError("CreateAccessResponse.external_id required")
    return out
