"""Generated from Smithy shape ``com.amazonaws.interconnect#DeleteConnectionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_interconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_interconnect.types.connection_id


class DeleteConnectionRequest(TypedDict):
    identifier: "aws_sdk_interconnect.types.connection_id.ConnectionId"
    """<p>The identifier of the <a>Connection</a> to be deleted. </p>"""
    client_token: NotRequired["str"]
    """<p>Idempotency token used for the request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteConnectionRequest) -> dict:
    out: dict = {}
    out["identifier"] = value["identifier"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteConnectionRequest:
    out: DeleteConnectionRequest = {}  # type: ignore[typeddict-item]
    if "identifier" in data:
        out["identifier"] = data["identifier"]
    else:
        raise DeserializationError("DeleteConnectionRequest.identifier required")
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
