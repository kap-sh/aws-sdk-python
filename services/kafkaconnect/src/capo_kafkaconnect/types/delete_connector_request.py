"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#DeleteConnectorRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafkaconnect.types.__string


class DeleteConnectorRequest(TypedDict, closed=True):
    connector_arn: "capo_kafkaconnect.types.__string.__string"
    """<p>The Amazon Resource Name (ARN) of the connector that you want to delete.</p>"""
    current_version: NotRequired["capo_kafkaconnect.types.__string.__string"]
    """<p>The current version of the connector that you want to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteConnectorRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteConnectorRequest:
    out: DeleteConnectorRequest = {}  # type: ignore[typeddict-item]
    return out
