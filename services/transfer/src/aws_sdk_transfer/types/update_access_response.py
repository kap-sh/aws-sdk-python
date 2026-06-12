"""Generated from Smithy shape ``com.amazonaws.transfer#UpdateAccessResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_transfer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_transfer.types.external_id
    import aws_sdk_transfer.types.server_id


class UpdateAccessResponse(TypedDict):
    server_id: "aws_sdk_transfer.types.server_id.ServerId"
    """<p>The identifier of the server that the user is attached to.</p>"""
    external_id: "aws_sdk_transfer.types.external_id.ExternalId"
    """<p>The external identifier of the group whose users have access to your Amazon S3 or Amazon EFS resources over the enabled protocols using Amazon Web ServicesTransfer Family.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateAccessResponse) -> dict:
    out: dict = {}
    out["ServerId"] = value["server_id"]
    out["ExternalId"] = value["external_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateAccessResponse:
    out: UpdateAccessResponse = {}  # type: ignore[typeddict-item]
    if "ServerId" in data:
        out["server_id"] = data["ServerId"]
    else:
        raise DeserializationError("UpdateAccessResponse.server_id required")
    if "ExternalId" in data:
        out["external_id"] = data["ExternalId"]
    else:
        raise DeserializationError("UpdateAccessResponse.external_id required")
    return out
