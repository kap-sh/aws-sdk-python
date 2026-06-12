"""Generated from Smithy shape ``com.amazonaws.transfer#CreateServerResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_transfer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_transfer.types.server_id


class CreateServerResponse(TypedDict):
    server_id: "aws_sdk_transfer.types.server_id.ServerId"
    """<p>The service-assigned identifier of the server that is created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateServerResponse) -> dict:
    out: dict = {}
    out["ServerId"] = value["server_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateServerResponse:
    out: CreateServerResponse = {}  # type: ignore[typeddict-item]
    if "ServerId" in data:
        out["server_id"] = data["ServerId"]
    else:
        raise DeserializationError("CreateServerResponse.server_id required")
    return out
