"""Generated from Smithy shape ``com.amazonaws.workspacesweb#UpdateTrustStoreResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_workspaces_web.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workspaces_web.types.arn


class UpdateTrustStoreResponse(TypedDict):
    trust_store_arn: "aws_sdk_workspaces_web.types.arn.ARN"
    """<p>The ARN of the trust store.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateTrustStoreResponse) -> dict:
    out: dict = {}
    out["trustStoreArn"] = value["trust_store_arn"]
    return out


def deserialize_json(data: dict) -> UpdateTrustStoreResponse:
    out: UpdateTrustStoreResponse = {}  # type: ignore[typeddict-item]
    if "trustStoreArn" in data:
        out["trust_store_arn"] = data["trustStoreArn"]
    else:
        raise DeserializationError("UpdateTrustStoreResponse.trust_store_arn required")
    return out
