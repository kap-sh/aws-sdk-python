"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsDynamoDbTableKeySchema``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class AwsDynamoDbTableKeySchema(TypedDict, closed=True):
    attribute_name: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The name of the key schema attribute.</p>"""
    key_type: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The type of key used for the key schema attribute. Valid values are <code>HASH</code> or <code>RANGE</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsDynamoDbTableKeySchema) -> dict:
    out: dict = {}
    if "attribute_name" in value:
        out["AttributeName"] = value["attribute_name"]
    if "key_type" in value:
        out["KeyType"] = value["key_type"]
    return out


def deserialize_json(data: dict) -> AwsDynamoDbTableKeySchema:
    out: AwsDynamoDbTableKeySchema = {}  # type: ignore[typeddict-item]
    if "AttributeName" in data:
        out["attribute_name"] = data["AttributeName"]
    if "KeyType" in data:
        out["key_type"] = data["KeyType"]
    return out
