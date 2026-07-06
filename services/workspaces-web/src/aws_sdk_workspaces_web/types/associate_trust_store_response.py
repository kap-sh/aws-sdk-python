"""Generated from Smithy shape ``com.amazonaws.workspacesweb#AssociateTrustStoreResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_workspaces_web.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workspaces_web.types.arn


class AssociateTrustStoreResponse(TypedDict, closed=True):
    portal_arn: "aws_sdk_workspaces_web.types.arn.ARN"
    """<p>The ARN of the web portal.</p>"""
    trust_store_arn: "aws_sdk_workspaces_web.types.arn.ARN"
    """<p>The ARN of the trust store.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateTrustStoreResponse) -> dict:
    out: dict = {}
    out["portalArn"] = value["portal_arn"]
    out["trustStoreArn"] = value["trust_store_arn"]
    return out


def deserialize_json(data: dict) -> AssociateTrustStoreResponse:
    out: AssociateTrustStoreResponse = {}  # type: ignore[typeddict-item]
    if "portalArn" in data:
        out["portal_arn"] = data["portalArn"]
    else:
        raise DeserializationError("AssociateTrustStoreResponse.portal_arn required")
    if "trustStoreArn" in data:
        out["trust_store_arn"] = data["trustStoreArn"]
    else:
        raise DeserializationError(
            "AssociateTrustStoreResponse.trust_store_arn required"
        )
    return out
