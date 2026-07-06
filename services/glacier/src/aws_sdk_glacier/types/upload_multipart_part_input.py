"""Generated from Smithy shape ``com.amazonaws.glacier#UploadMultipartPartInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glacier.types.stream
    import aws_sdk_glacier.types.string


class UploadMultipartPartInput(TypedDict, closed=True):
    account_id: "aws_sdk_glacier.types.string.string"
    """<p>The <code>AccountId</code> value is the AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single '<code>-</code>' (hyphen), in which case Amazon Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, do not include any hyphens ('-') in the ID. </p>"""
    vault_name: "aws_sdk_glacier.types.string.string"
    """<p>The name of the vault.</p>"""
    upload_id: "aws_sdk_glacier.types.string.string"
    """<p>The upload ID of the multipart upload.</p>"""
    checksum: NotRequired["aws_sdk_glacier.types.string.string"]
    """<p>The SHA256 tree hash of the data being uploaded.</p>"""
    range: NotRequired["aws_sdk_glacier.types.string.string"]
    """<p>Identifies the range of bytes in the assembled archive that will be uploaded in this part. Amazon Glacier uses this information to assemble the archive in the proper sequence. The format of this header follows RFC 2616. An example header is Content-Range:bytes 0-4194303/*.</p>"""
    body: "aws_sdk_glacier.types.stream.Stream"
    """<p>The data to upload.</p>"""
