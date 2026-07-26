"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsS3ObjectDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string


class AwsS3ObjectDetails(TypedDict, closed=True):
    last_modified: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    r"""<p>Indicates when the object was last modified.</p> <p>For more information about the validation and formatting of timestamp fields in Security Hub CSPM, see <a href=\"https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps\">Timestamps</a>.</p>"""
    e_tag: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The opaque identifier assigned by a web server to a specific version of a resource found at a URL.</p>"""
    version_id: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The version of the object.</p>"""
    content_type: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>A standard MIME type describing the format of the object data.</p>"""
    server_side_encryption: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>If the object is stored using server-side encryption, the value of the server-side encryption algorithm used when storing this object in Amazon S3.</p>"""
    ssekms_key_id: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The identifier of the KMS symmetric customer managed key that was used for the object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsS3ObjectDetails) -> dict:
    out: dict = {}
    if "last_modified" in value:
        out["LastModified"] = value["last_modified"]
    if "e_tag" in value:
        out["ETag"] = value["e_tag"]
    if "version_id" in value:
        out["VersionId"] = value["version_id"]
    if "content_type" in value:
        out["ContentType"] = value["content_type"]
    if "server_side_encryption" in value:
        out["ServerSideEncryption"] = value["server_side_encryption"]
    if "ssekms_key_id" in value:
        out["SSEKMSKeyId"] = value["ssekms_key_id"]
    return out


def deserialize_json(data: dict) -> AwsS3ObjectDetails:
    out: AwsS3ObjectDetails = {}  # type: ignore[typeddict-item]
    if "LastModified" in data:
        out["last_modified"] = data["LastModified"]
    if "ETag" in data:
        out["e_tag"] = data["ETag"]
    if "VersionId" in data:
        out["version_id"] = data["VersionId"]
    if "ContentType" in data:
        out["content_type"] = data["ContentType"]
    if "ServerSideEncryption" in data:
        out["server_side_encryption"] = data["ServerSideEncryption"]
    if "SSEKMSKeyId" in data:
        out["ssekms_key_id"] = data["SSEKMSKeyId"]
    return out
