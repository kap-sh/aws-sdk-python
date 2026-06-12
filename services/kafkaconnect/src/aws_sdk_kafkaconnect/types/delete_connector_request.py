"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#DeleteConnectorRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kafkaconnect.types.__string


class DeleteConnectorRequest(TypedDict):
    connector_arn: "aws_sdk_kafkaconnect.types.__string.__string"
    """<p>The Amazon Resource Name (ARN) of the connector that you want to delete.</p>"""
    current_version: NotRequired["aws_sdk_kafkaconnect.types.__string.__string"]
    """<p>The current version of the connector that you want to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteConnectorRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteConnectorRequest:
    out: DeleteConnectorRequest = {}  # type: ignore[typeddict-item]
    return out
