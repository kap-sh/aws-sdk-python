"""Generated from Smithy shape ``com.amazonaws.lightsail#AccessKey``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.access_key_last_used
    import aws_sdk_lightsail.types.iam_access_key_id
    import aws_sdk_lightsail.types.iso_date
    import aws_sdk_lightsail.types.non_empty_string
    import aws_sdk_lightsail.types.status_type


class AccessKey(TypedDict, closed=True):
    access_key_id: NotRequired[
        "aws_sdk_lightsail.types.iam_access_key_id.IAMAccessKeyId"
    ]
    """<p>The ID of the access key.</p>"""
    secret_access_key: NotRequired[
        "aws_sdk_lightsail.types.non_empty_string.NonEmptyString"
    ]
    """<p>The secret access key used to sign requests.</p> <p>You should store the secret access key in a safe location. We recommend that you delete the access key if the secret access key is compromised.</p>"""
    status: NotRequired["aws_sdk_lightsail.types.status_type.StatusType"]
    """<p>The status of the access key.</p> <p>A status of <code>Active</code> means that the key is valid, while <code>Inactive</code> means it is not.</p>"""
    created_at: NotRequired["aws_sdk_lightsail.types.iso_date.IsoDate"]
    """<p>The timestamp when the access key was created.</p>"""
    last_used: NotRequired[
        "aws_sdk_lightsail.types.access_key_last_used.AccessKeyLastUsed"
    ]
    r"""<p>An object that describes the last time the access key was used.</p> <note> <p>This object does not include data in the response of a <a href=\"https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_CreateBucketAccessKey.html\">CreateBucketAccessKey</a> action. If the access key has not been used, the <code>region</code> and <code>serviceName</code> values are <code>N/A</code>, and the <code>lastUsedDate</code> value is null.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AccessKey) -> dict:
    out: dict = {}
    if "access_key_id" in value:
        out["accessKeyId"] = value["access_key_id"]
    if "secret_access_key" in value:
        out["secretAccessKey"] = value["secret_access_key"]
    if "status" in value:
        import aws_sdk_lightsail.types.status_type

        out["status"] = aws_sdk_lightsail.types.status_type.serialize_aws_json_1_1(
            value["status"]
        )
    if "created_at" in value:
        import aws_sdk_lightsail.types.iso_date

        out["createdAt"] = aws_sdk_lightsail.types.iso_date.serialize_aws_json_1_1(
            value["created_at"]
        )
    if "last_used" in value:
        import aws_sdk_lightsail.types.access_key_last_used

        out["lastUsed"] = (
            aws_sdk_lightsail.types.access_key_last_used.serialize_aws_json_1_1(
                value["last_used"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AccessKey:
    out: AccessKey = {}  # type: ignore[typeddict-item]
    if "accessKeyId" in data:
        out["access_key_id"] = data["accessKeyId"]
    if "secretAccessKey" in data:
        out["secret_access_key"] = data["secretAccessKey"]
    if "status" in data:
        import aws_sdk_lightsail.types.status_type

        out["status"] = aws_sdk_lightsail.types.status_type.deserialize_aws_json_1_1(
            data["status"]
        )
    if "createdAt" in data:
        import aws_sdk_lightsail.types.iso_date

        out["created_at"] = aws_sdk_lightsail.types.iso_date.deserialize_aws_json_1_1(
            data["createdAt"]
        )
    if "lastUsed" in data:
        import aws_sdk_lightsail.types.access_key_last_used

        out["last_used"] = (
            aws_sdk_lightsail.types.access_key_last_used.deserialize_aws_json_1_1(
                data["lastUsed"]
            )
        )
    return out
