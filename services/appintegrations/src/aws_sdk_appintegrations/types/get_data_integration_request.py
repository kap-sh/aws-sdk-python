"""Generated from Smithy shape ``com.amazonaws.appintegrations#GetDataIntegrationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_appintegrations.types.identifier


class GetDataIntegrationRequest(TypedDict, closed=True):
    identifier: "aws_sdk_appintegrations.types.identifier.Identifier"
    """<p>A unique identifier.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDataIntegrationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetDataIntegrationRequest:
    out: GetDataIntegrationRequest = {}  # type: ignore[typeddict-item]
    return out
