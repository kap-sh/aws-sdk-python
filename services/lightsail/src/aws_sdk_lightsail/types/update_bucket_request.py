"""Generated from Smithy shape ``com.amazonaws.lightsail#UpdateBucketRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_lightsail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.access_rules
    import aws_sdk_lightsail.types.bucket_access_log_config
    import aws_sdk_lightsail.types.bucket_cors_config
    import aws_sdk_lightsail.types.bucket_name
    import aws_sdk_lightsail.types.non_empty_string
    import aws_sdk_lightsail.types.partner_id_list


class UpdateBucketRequest(TypedDict, closed=True):
    bucket_name: "aws_sdk_lightsail.types.bucket_name.BucketName"
    """<p>The name of the bucket to update.</p>"""
    access_rules: NotRequired["aws_sdk_lightsail.types.access_rules.AccessRules"]
    """<p>An object that sets the public accessibility of objects in the specified bucket.</p>"""
    versioning: NotRequired["aws_sdk_lightsail.types.non_empty_string.NonEmptyString"]
    """<p>Specifies whether to enable or suspend versioning of objects in the bucket.</p> <p>The following options can be specified:</p> <ul> <li> <p> <code>Enabled</code> - Enables versioning of objects in the specified bucket.</p> </li> <li> <p> <code>Suspended</code> - Suspends versioning of objects in the specified bucket. Existing object versions are retained.</p> </li> </ul>"""
    readonly_access_accounts: NotRequired[
        "aws_sdk_lightsail.types.partner_id_list.PartnerIdList"
    ]
    """<p>An array of strings to specify the Amazon Web Services account IDs that can access the bucket.</p> <p>You can give a maximum of 10 Amazon Web Services accounts access to a bucket.</p>"""
    access_log_config: NotRequired[
        "aws_sdk_lightsail.types.bucket_access_log_config.BucketAccessLogConfig"
    ]
    """<p>An object that describes the access log configuration for the bucket.</p>"""
    cors: NotRequired["aws_sdk_lightsail.types.bucket_cors_config.BucketCorsConfig"]
    r"""<p>Sets the cross-origin resource sharing (CORS) configuration for your bucket. If a CORS configuration exists, it is replaced with the specified configuration. For AWS CLI operations, this parameter can also be passed as a file. For more information, see <a href=\"https://docs.aws.amazon.com/lightsail/latest/userguide/configure-cors.html\">Configuring cross-origin resource sharing (CORS)</a>.</p> <note> <p>CORS information is only returned in a response when you update the CORS policy.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateBucketRequest) -> dict:
    out: dict = {}
    out["bucketName"] = value["bucket_name"]
    if "access_rules" in value:
        import aws_sdk_lightsail.types.access_rules

        out["accessRules"] = (
            aws_sdk_lightsail.types.access_rules.serialize_aws_json_1_1(
                value["access_rules"]
            )
        )
    if "versioning" in value:
        out["versioning"] = value["versioning"]
    if "readonly_access_accounts" in value:
        import aws_sdk_lightsail.types.partner_id_list

        out["readonlyAccessAccounts"] = (
            aws_sdk_lightsail.types.partner_id_list.serialize_aws_json_1_1(
                value["readonly_access_accounts"]
            )
        )
    if "access_log_config" in value:
        import aws_sdk_lightsail.types.bucket_access_log_config

        out["accessLogConfig"] = (
            aws_sdk_lightsail.types.bucket_access_log_config.serialize_aws_json_1_1(
                value["access_log_config"]
            )
        )
    if "cors" in value:
        import aws_sdk_lightsail.types.bucket_cors_config

        out["cors"] = aws_sdk_lightsail.types.bucket_cors_config.serialize_aws_json_1_1(
            value["cors"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateBucketRequest:
    out: UpdateBucketRequest = {}  # type: ignore[typeddict-item]
    if "bucketName" in data:
        out["bucket_name"] = data["bucketName"]
    else:
        raise DeserializationError("UpdateBucketRequest.bucket_name required")
    if "accessRules" in data:
        import aws_sdk_lightsail.types.access_rules

        out["access_rules"] = (
            aws_sdk_lightsail.types.access_rules.deserialize_aws_json_1_1(
                data["accessRules"]
            )
        )
    if "versioning" in data:
        out["versioning"] = data["versioning"]
    if "readonlyAccessAccounts" in data:
        import aws_sdk_lightsail.types.partner_id_list

        out["readonly_access_accounts"] = (
            aws_sdk_lightsail.types.partner_id_list.deserialize_aws_json_1_1(
                data["readonlyAccessAccounts"]
            )
        )
    if "accessLogConfig" in data:
        import aws_sdk_lightsail.types.bucket_access_log_config

        out["access_log_config"] = (
            aws_sdk_lightsail.types.bucket_access_log_config.deserialize_aws_json_1_1(
                data["accessLogConfig"]
            )
        )
    if "cors" in data:
        import aws_sdk_lightsail.types.bucket_cors_config

        out["cors"] = (
            aws_sdk_lightsail.types.bucket_cors_config.deserialize_aws_json_1_1(
                data["cors"]
            )
        )
    return out
