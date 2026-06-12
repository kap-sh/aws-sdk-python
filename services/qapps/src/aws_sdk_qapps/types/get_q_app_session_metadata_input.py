"""Generated from Smithy shape ``com.amazonaws.qapps#GetQAppSessionMetadataInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_qapps.types.instance_id
    import aws_sdk_qapps.types.uuid


class GetQAppSessionMetadataInput(TypedDict):
    instance_id: "aws_sdk_qapps.types.instance_id.InstanceId"
    """<p>The unique identifier of the Amazon Q Business application environment instance.</p>"""
    session_id: "aws_sdk_qapps.types.uuid.UUID"
    """<p>The unique identifier of the Q App session.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetQAppSessionMetadataInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetQAppSessionMetadataInput:
    out: GetQAppSessionMetadataInput = {}  # type: ignore[typeddict-item]
    return out
