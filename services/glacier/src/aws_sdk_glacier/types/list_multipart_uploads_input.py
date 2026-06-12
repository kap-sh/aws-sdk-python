"""Generated from Smithy shape ``com.amazonaws.glacier#ListMultipartUploadsInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glacier.types.string


class ListMultipartUploadsInput(TypedDict):
    account_id: "aws_sdk_glacier.types.string.string"
    """<p>The <code>AccountId</code> value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '<code>-</code>' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID. </p>"""
    vault_name: "aws_sdk_glacier.types.string.string"
    """<p>The name of the vault.</p>"""
    limit: NotRequired["int"]
    """<p>Specifies the maximum number of uploads returned in the response body. If this value is not specified, the List Uploads operation returns up to 50 uploads.</p>"""
    marker: NotRequired["aws_sdk_glacier.types.string.string"]
    """<p>An opaque string used for pagination. This value specifies the upload at which the listing of uploads should begin. Get the marker value from a previous List Uploads response. You need only include the marker if you are continuing the pagination of results started in a previous List Uploads request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListMultipartUploadsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListMultipartUploadsInput:
    out: ListMultipartUploadsInput = {}  # type: ignore[typeddict-item]
    return out
