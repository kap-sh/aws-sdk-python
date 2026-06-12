"""Generated from Smithy shape ``com.amazonaws.elastictranscoder#Permission``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_elastic_transcoder.types.access_controls
    import aws_sdk_elastic_transcoder.types.grantee
    import aws_sdk_elastic_transcoder.types.grantee_type


class Permission(TypedDict):
    grantee_type: NotRequired[
        "aws_sdk_elastic_transcoder.types.grantee_type.GranteeType"
    ]
    """<p>The type of value that appears in the Grantee object:</p> <ul> <li> <p> <code>Canonical</code>: Either the canonical user ID for an AWS account or an origin access identity for an Amazon CloudFront distribution.</p> <important> <p>A canonical user ID is not the same as an AWS account number.</p> </important> </li> <li> <p> <code>Email</code>: The registered email address of an AWS account.</p> </li> <li> <p> <code>Group</code>: One of the following predefined Amazon S3 groups: <code>AllUsers</code>, <code>AuthenticatedUsers</code>, or <code>LogDelivery</code>.</p> </li> </ul>"""
    grantee: NotRequired["aws_sdk_elastic_transcoder.types.grantee.Grantee"]
    """<p>The AWS user or group that you want to have access to transcoded files and playlists. To identify the user or group, you can specify the canonical user ID for an AWS account, an origin access identity for a CloudFront distribution, the registered email address of an AWS account, or a predefined Amazon S3 group.</p>"""
    access: NotRequired[
        "aws_sdk_elastic_transcoder.types.access_controls.AccessControls"
    ]
    """<p> The permission that you want to give to the AWS user that is listed in Grantee. Valid values include: </p> <ul> <li> <p> <code>READ</code>: The grantee can read the thumbnails and metadata for thumbnails that Elastic Transcoder adds to the Amazon S3 bucket.</p> </li> <li> <p> <code>READ_ACP</code>: The grantee can read the object ACL for thumbnails that Elastic Transcoder adds to the Amazon S3 bucket.</p> </li> <li> <p> <code>WRITE_ACP</code>: The grantee can write the ACL for the thumbnails that Elastic Transcoder adds to the Amazon S3 bucket.</p> </li> <li> <p> <code>FULL_CONTROL</code>: The grantee has READ, READ_ACP, and WRITE_ACP permissions for the thumbnails that Elastic Transcoder adds to the Amazon S3 bucket.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: Permission) -> dict:
    out: dict = {}
    if "grantee_type" in value:
        out["GranteeType"] = value["grantee_type"]
    if "grantee" in value:
        out["Grantee"] = value["grantee"]
    if "access" in value:
        import aws_sdk_elastic_transcoder.types.access_controls

        out["Access"] = aws_sdk_elastic_transcoder.types.access_controls.serialize_json(
            value["access"]
        )
    return out


def deserialize_json(data: dict) -> Permission:
    out: Permission = {}  # type: ignore[typeddict-item]
    if "GranteeType" in data:
        out["grantee_type"] = data["GranteeType"]
    if "Grantee" in data:
        out["grantee"] = data["Grantee"]
    if "Access" in data:
        import aws_sdk_elastic_transcoder.types.access_controls

        out["access"] = (
            aws_sdk_elastic_transcoder.types.access_controls.deserialize_json(
                data["Access"]
            )
        )
    return out
