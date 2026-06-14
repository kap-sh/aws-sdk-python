"""Generated from Smithy shape ``com.amazonaws.workspacesweb#AssociateTrustStoreRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_workspaces_web.types.arn


class AssociateTrustStoreRequest(TypedDict):
    portal_arn: "aws_sdk_workspaces_web.types.arn.ARN"
    """<p>The ARN of the web portal.</p>"""
    trust_store_arn: "aws_sdk_workspaces_web.types.arn.ARN"
    """<p>The ARN of the trust store.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateTrustStoreRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> AssociateTrustStoreRequest:
    out: AssociateTrustStoreRequest = {}  # type: ignore[typeddict-item]
    return out
