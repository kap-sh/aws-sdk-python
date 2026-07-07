"""Generated from Smithy shape ``com.amazonaws.workspacesweb#GetTrustStoreRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_workspaces_web.types.arn


class GetTrustStoreRequest(TypedDict, closed=True):
    trust_store_arn: "aws_sdk_workspaces_web.types.arn.ARN"
    """<p>The ARN of the trust store.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTrustStoreRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetTrustStoreRequest:
    out: GetTrustStoreRequest = {}  # type: ignore[typeddict-item]
    return out
