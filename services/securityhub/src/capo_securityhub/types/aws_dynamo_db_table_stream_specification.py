"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsDynamoDbTableStreamSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.boolean
    import capo_securityhub.types.non_empty_string


class AwsDynamoDbTableStreamSpecification(TypedDict, closed=True):
    stream_enabled: NotRequired["capo_securityhub.types.boolean.Boolean"]
    """<p>Indicates whether DynamoDB Streams is enabled on the table.</p>"""
    stream_view_type: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>Determines the information that is written to the table.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsDynamoDbTableStreamSpecification) -> dict:
    out: dict = {}
    if "stream_enabled" in value:
        out["StreamEnabled"] = value["stream_enabled"]
    if "stream_view_type" in value:
        out["StreamViewType"] = value["stream_view_type"]
    return out


def deserialize_json(data: dict) -> AwsDynamoDbTableStreamSpecification:
    out: AwsDynamoDbTableStreamSpecification = {}  # type: ignore[typeddict-item]
    if "StreamEnabled" in data:
        out["stream_enabled"] = data["StreamEnabled"]
    if "StreamViewType" in data:
        out["stream_view_type"] = data["StreamViewType"]
    return out
