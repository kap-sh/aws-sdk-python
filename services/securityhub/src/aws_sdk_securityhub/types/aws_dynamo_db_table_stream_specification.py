"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsDynamoDbTableStreamSpecification``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.boolean
    import aws_sdk_securityhub.types.non_empty_string


class AwsDynamoDbTableStreamSpecification(TypedDict):
    stream_enabled: NotRequired["aws_sdk_securityhub.types.boolean.Boolean"]
    """<p>Indicates whether DynamoDB Streams is enabled on the table.</p>"""
    stream_view_type: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
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
