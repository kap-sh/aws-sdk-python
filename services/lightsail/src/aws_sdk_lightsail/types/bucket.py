"""Generated from Smithy shape ``com.amazonaws.lightsail#Bucket``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.access_receiver_list
    import aws_sdk_lightsail.types.access_rules
    import aws_sdk_lightsail.types.boolean
    import aws_sdk_lightsail.types.bucket_access_log_config
    import aws_sdk_lightsail.types.bucket_cors_config
    import aws_sdk_lightsail.types.bucket_name
    import aws_sdk_lightsail.types.bucket_state
    import aws_sdk_lightsail.types.iso_date
    import aws_sdk_lightsail.types.non_empty_string
    import aws_sdk_lightsail.types.partner_id_list
    import aws_sdk_lightsail.types.resource_location
    import aws_sdk_lightsail.types.tag_list


class Bucket(TypedDict):
    resource_type: NotRequired[
        "aws_sdk_lightsail.types.non_empty_string.NonEmptyString"
    ]
    """<p>The Lightsail resource type of the bucket.</p>"""
    access_rules: NotRequired["aws_sdk_lightsail.types.access_rules.AccessRules"]
    """<p>An object that describes the access rules of the bucket.</p>"""
    arn: NotRequired["aws_sdk_lightsail.types.non_empty_string.NonEmptyString"]
    """<p>The Amazon Resource Name (ARN) of the bucket.</p>"""
    bundle_id: NotRequired["aws_sdk_lightsail.types.non_empty_string.NonEmptyString"]
    """<p>The ID of the bundle currently applied to the bucket.</p> <p>A bucket bundle specifies the monthly cost, storage space, and data transfer quota for a bucket.</p> <p>Use the <a href=\"https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_UpdateBucketBundle.html\">UpdateBucketBundle</a> action to change the bundle of a bucket.</p>"""
    created_at: NotRequired["aws_sdk_lightsail.types.iso_date.IsoDate"]
    """<p>The timestamp when the distribution was created.</p>"""
    url: NotRequired["aws_sdk_lightsail.types.non_empty_string.NonEmptyString"]
    """<p>The URL of the bucket.</p>"""
    location: NotRequired["aws_sdk_lightsail.types.resource_location.ResourceLocation"]
    """<p>An object that describes the location of the bucket, such as the Amazon Web Services Region and Availability Zone.</p>"""
    name: NotRequired["aws_sdk_lightsail.types.bucket_name.BucketName"]
    """<p>The name of the bucket.</p>"""
    support_code: NotRequired["aws_sdk_lightsail.types.non_empty_string.NonEmptyString"]
    """<p>The support code for a bucket. Include this code in your email to support when you have questions about a Lightsail bucket. This code enables our support team to look up your Lightsail information more easily.</p>"""
    tags: NotRequired["aws_sdk_lightsail.types.tag_list.TagList"]
    """<p>The tag keys and optional values for the bucket. For more information, see <a href=\"https://lightsail.aws.amazon.com/ls/docs/en/articles/amazon-lightsail-tags\">Tags in Amazon Lightsail</a> in the <i>Amazon Lightsail Developer Guide</i>.</p>"""
    object_versioning: NotRequired[
        "aws_sdk_lightsail.types.non_empty_string.NonEmptyString"
    ]
    """<p>Indicates whether object versioning is enabled for the bucket.</p> <p>The following options can be configured:</p> <ul> <li> <p> <code>Enabled</code> - Object versioning is enabled.</p> </li> <li> <p> <code>Suspended</code> - Object versioning was previously enabled but is currently suspended. Existing object versions are retained.</p> </li> <li> <p> <code>NeverEnabled</code> - Object versioning has never been enabled.</p> </li> </ul>"""
    able_to_update_bundle: NotRequired["aws_sdk_lightsail.types.boolean.boolean"]
    """<p>Indicates whether the bundle that is currently applied to a bucket can be changed to another bundle.</p> <p>You can update a bucket's bundle only one time within a monthly Amazon Web Services billing cycle.</p> <p>Use the <a href=\"https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_UpdateBucketBundle.html\">UpdateBucketBundle</a> action to change a bucket's bundle.</p>"""
    readonly_access_accounts: NotRequired[
        "aws_sdk_lightsail.types.partner_id_list.PartnerIdList"
    ]
    """<p>An array of strings that specify the Amazon Web Services account IDs that have read-only access to the bucket.</p>"""
    resources_receiving_access: NotRequired[
        "aws_sdk_lightsail.types.access_receiver_list.AccessReceiverList"
    ]
    """<p>An array of objects that describe Lightsail instances that have access to the bucket.</p> <p>Use the <a href=\"https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_SetResourceAccessForBucket.html\">SetResourceAccessForBucket</a> action to update the instances that have access to a bucket.</p>"""
    state: NotRequired["aws_sdk_lightsail.types.bucket_state.BucketState"]
    """<p>An object that describes the state of the bucket.</p>"""
    access_log_config: NotRequired[
        "aws_sdk_lightsail.types.bucket_access_log_config.BucketAccessLogConfig"
    ]
    """<p>An object that describes the access log configuration for the bucket.</p>"""
    cors: NotRequired["aws_sdk_lightsail.types.bucket_cors_config.BucketCorsConfig"]
    """<p>An array of cross-origin resource sharing (CORS) rules that identify origins and the HTTP methods that can be executed on your bucket. This field is only included in the response when CORS configuration is requested or when updating CORS configuration. For more information, see <a href=\"https://docs.aws.amazon.com/lightsail/latest/userguide/configure-cors.html\">Configuring cross-origin resource sharing (CORS)</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Bucket) -> dict:
    out: dict = {}
    if "resource_type" in value:
        out["resourceType"] = value["resource_type"]
    if "access_rules" in value:
        import aws_sdk_lightsail.types.access_rules

        out["accessRules"] = (
            aws_sdk_lightsail.types.access_rules.serialize_aws_json_1_1(
                value["access_rules"]
            )
        )
    if "arn" in value:
        out["arn"] = value["arn"]
    if "bundle_id" in value:
        out["bundleId"] = value["bundle_id"]
    if "created_at" in value:
        import aws_sdk_lightsail.types.iso_date

        out["createdAt"] = aws_sdk_lightsail.types.iso_date.serialize_aws_json_1_1(
            value["created_at"]
        )
    if "url" in value:
        out["url"] = value["url"]
    if "location" in value:
        import aws_sdk_lightsail.types.resource_location

        out["location"] = (
            aws_sdk_lightsail.types.resource_location.serialize_aws_json_1_1(
                value["location"]
            )
        )
    if "name" in value:
        out["name"] = value["name"]
    if "support_code" in value:
        out["supportCode"] = value["support_code"]
    if "tags" in value:
        import aws_sdk_lightsail.types.tag_list

        out["tags"] = aws_sdk_lightsail.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "object_versioning" in value:
        out["objectVersioning"] = value["object_versioning"]
    if "able_to_update_bundle" in value:
        out["ableToUpdateBundle"] = value["able_to_update_bundle"]
    if "readonly_access_accounts" in value:
        import aws_sdk_lightsail.types.partner_id_list

        out["readonlyAccessAccounts"] = (
            aws_sdk_lightsail.types.partner_id_list.serialize_aws_json_1_1(
                value["readonly_access_accounts"]
            )
        )
    if "resources_receiving_access" in value:
        import aws_sdk_lightsail.types.access_receiver_list

        out["resourcesReceivingAccess"] = (
            aws_sdk_lightsail.types.access_receiver_list.serialize_aws_json_1_1(
                value["resources_receiving_access"]
            )
        )
    if "state" in value:
        import aws_sdk_lightsail.types.bucket_state

        out["state"] = aws_sdk_lightsail.types.bucket_state.serialize_aws_json_1_1(
            value["state"]
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


def deserialize_aws_json_1_1(data: dict) -> Bucket:
    out: Bucket = {}  # type: ignore[typeddict-item]
    if "resourceType" in data:
        out["resource_type"] = data["resourceType"]
    if "accessRules" in data:
        import aws_sdk_lightsail.types.access_rules

        out["access_rules"] = (
            aws_sdk_lightsail.types.access_rules.deserialize_aws_json_1_1(
                data["accessRules"]
            )
        )
    if "arn" in data:
        out["arn"] = data["arn"]
    if "bundleId" in data:
        out["bundle_id"] = data["bundleId"]
    if "createdAt" in data:
        import aws_sdk_lightsail.types.iso_date

        out["created_at"] = aws_sdk_lightsail.types.iso_date.deserialize_aws_json_1_1(
            data["createdAt"]
        )
    if "url" in data:
        out["url"] = data["url"]
    if "location" in data:
        import aws_sdk_lightsail.types.resource_location

        out["location"] = (
            aws_sdk_lightsail.types.resource_location.deserialize_aws_json_1_1(
                data["location"]
            )
        )
    if "name" in data:
        out["name"] = data["name"]
    if "supportCode" in data:
        out["support_code"] = data["supportCode"]
    if "tags" in data:
        import aws_sdk_lightsail.types.tag_list

        out["tags"] = aws_sdk_lightsail.types.tag_list.deserialize_aws_json_1_1(
            data["tags"]
        )
    if "objectVersioning" in data:
        out["object_versioning"] = data["objectVersioning"]
    if "ableToUpdateBundle" in data:
        out["able_to_update_bundle"] = data["ableToUpdateBundle"]
    if "readonlyAccessAccounts" in data:
        import aws_sdk_lightsail.types.partner_id_list

        out["readonly_access_accounts"] = (
            aws_sdk_lightsail.types.partner_id_list.deserialize_aws_json_1_1(
                data["readonlyAccessAccounts"]
            )
        )
    if "resourcesReceivingAccess" in data:
        import aws_sdk_lightsail.types.access_receiver_list

        out["resources_receiving_access"] = (
            aws_sdk_lightsail.types.access_receiver_list.deserialize_aws_json_1_1(
                data["resourcesReceivingAccess"]
            )
        )
    if "state" in data:
        import aws_sdk_lightsail.types.bucket_state

        out["state"] = aws_sdk_lightsail.types.bucket_state.deserialize_aws_json_1_1(
            data["state"]
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
