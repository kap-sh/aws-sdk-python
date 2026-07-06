"""Generated from Smithy shape ``com.amazonaws.workspacesweb#CreateTrustStoreResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_workspaces_web.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workspaces_web.types.arn


class CreateTrustStoreResponse(TypedDict, closed=True):
    trust_store_arn: "aws_sdk_workspaces_web.types.arn.ARN"
    """<p>The ARN of the trust store.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateTrustStoreResponse) -> dict:
    out: dict = {}
    out["trustStoreArn"] = value["trust_store_arn"]
    return out


def deserialize_json(data: dict) -> CreateTrustStoreResponse:
    out: CreateTrustStoreResponse = {}  # type: ignore[typeddict-item]
    if "trustStoreArn" in data:
        out["trust_store_arn"] = data["trustStoreArn"]
    else:
        raise DeserializationError("CreateTrustStoreResponse.trust_store_arn required")
    return out
