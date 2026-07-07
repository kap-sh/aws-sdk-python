"""Generated from Smithy shape ``com.amazonaws.kafka#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kafka.types.__list_of__string
    import aws_sdk_kafka.types.__string


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "aws_sdk_kafka.types.__string.__string"
    """<p>The Amazon Resource Name (ARN) that uniquely identifies the resource that's associated with the tags.</p>"""
    tag_keys: NotRequired["aws_sdk_kafka.types.__list_of__string.__listOf__string"]
    """<p>Tag keys must be unique for a given cluster. In addition, the following restrictions apply:</p> <ul> <li> <p>Each tag key must be unique. If you add a tag with a key that's already in use, your new tag overwrites the existing key-value pair. </p> </li> <li> <p>You can't start a tag key with aws: because this prefix is reserved for use by AWS. AWS creates tags that begin with this prefix on your behalf, but you can't edit or delete them.</p> </li> <li> <p>Tag keys must be between 1 and 128 Unicode characters in length.</p> </li> <li> <p>Tag keys must consist of the following characters: Unicode letters, digits, white space, and the following special characters: _ . / = + - @.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    return out
