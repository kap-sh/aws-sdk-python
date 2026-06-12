"""Generated from Smithy shape ``com.amazonaws.lightsail#SetResourceAccessForBucketRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_lightsail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.bucket_name
    import aws_sdk_lightsail.types.resource_bucket_access
    import aws_sdk_lightsail.types.resource_name


class SetResourceAccessForBucketRequest(TypedDict):
    resource_name: "aws_sdk_lightsail.types.resource_name.ResourceName"
    """<p>The name of the Lightsail instance for which to set bucket access. The instance must be in a running or stopped state.</p>"""
    bucket_name: "aws_sdk_lightsail.types.bucket_name.BucketName"
    """<p>The name of the bucket for which to set access to another Lightsail resource.</p>"""
    access: "aws_sdk_lightsail.types.resource_bucket_access.ResourceBucketAccess"
    """<p>The access setting.</p> <p>The following access settings are available:</p> <ul> <li> <p> <code>allow</code> - Allows access to the bucket and its objects.</p> </li> <li> <p> <code>deny</code> - Denies access to the bucket and its objects. Use this setting to remove access for a resource previously set to <code>allow</code>.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SetResourceAccessForBucketRequest) -> dict:
    out: dict = {}
    out["resourceName"] = value["resource_name"]
    out["bucketName"] = value["bucket_name"]
    import aws_sdk_lightsail.types.resource_bucket_access

    out["access"] = (
        aws_sdk_lightsail.types.resource_bucket_access.serialize_aws_json_1_1(
            value["access"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> SetResourceAccessForBucketRequest:
    out: SetResourceAccessForBucketRequest = {}  # type: ignore[typeddict-item]
    if "resourceName" in data:
        out["resource_name"] = data["resourceName"]
    else:
        raise DeserializationError(
            "SetResourceAccessForBucketRequest.resource_name required"
        )
    if "bucketName" in data:
        out["bucket_name"] = data["bucketName"]
    else:
        raise DeserializationError(
            "SetResourceAccessForBucketRequest.bucket_name required"
        )
    if "access" in data:
        import aws_sdk_lightsail.types.resource_bucket_access

        out["access"] = (
            aws_sdk_lightsail.types.resource_bucket_access.deserialize_aws_json_1_1(
                data["access"]
            )
        )
    else:
        raise DeserializationError("SetResourceAccessForBucketRequest.access required")
    return out
