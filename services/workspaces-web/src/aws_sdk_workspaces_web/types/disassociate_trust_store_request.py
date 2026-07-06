"""Generated from Smithy shape ``com.amazonaws.workspacesweb#DisassociateTrustStoreRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_workspaces_web.types.arn


class DisassociateTrustStoreRequest(TypedDict, closed=True):
    portal_arn: "aws_sdk_workspaces_web.types.arn.ARN"
    """<p>The ARN of the web portal.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisassociateTrustStoreRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DisassociateTrustStoreRequest:
    out: DisassociateTrustStoreRequest = {}  # type: ignore[typeddict-item]
    return out
