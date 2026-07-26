"""Generated from Smithy shape ``com.amazonaws.securityhub#GetConnectorV2Request``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string


class GetConnectorV2Request(TypedDict, closed=True):
    connector_id: "capo_securityhub.types.non_empty_string.NonEmptyString"
    """<p>The UUID of the connectorV2 to identify connectorV2 resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetConnectorV2Request) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetConnectorV2Request:
    out: GetConnectorV2Request = {}  # type: ignore[typeddict-item]
    return out
