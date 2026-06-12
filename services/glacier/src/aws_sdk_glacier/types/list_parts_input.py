"""Generated from Smithy shape ``com.amazonaws.glacier#ListPartsInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glacier.types.string


class ListPartsInput(TypedDict):
    account_id: "aws_sdk_glacier.types.string.string"
    """<p>The <code>AccountId</code> value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '<code>-</code>' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID. </p>"""
    vault_name: "aws_sdk_glacier.types.string.string"
    """<p>The name of the vault.</p>"""
    upload_id: "aws_sdk_glacier.types.string.string"
    """<p>The upload ID of the multipart upload.</p>"""
    marker: NotRequired["aws_sdk_glacier.types.string.string"]
    """<p>An opaque string used for pagination. This value specifies the part at which the listing of parts should begin. Get the marker value from the response of a previous List Parts response. You need only include the marker if you are continuing the pagination of results started in a previous List Parts request.</p>"""
    limit: NotRequired["int"]
    """<p>The maximum number of parts to be returned. The default limit is 50. The number of parts returned might be fewer than the specified limit, but the number of returned parts never exceeds the limit.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPartsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListPartsInput:
    out: ListPartsInput = {}  # type: ignore[typeddict-item]
    return out
