"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#PutOriginEndpointPolicyRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_mediapackagev2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mediapackagev2.types.cdn_auth_configuration
    import aws_sdk_mediapackagev2.types.policy_text
    import aws_sdk_mediapackagev2.types.resource_name


class PutOriginEndpointPolicyRequest(TypedDict):
    channel_group_name: "aws_sdk_mediapackagev2.types.resource_name.ResourceName"
    """<p>The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region.</p>"""
    channel_name: "aws_sdk_mediapackagev2.types.resource_name.ResourceName"
    """<p>The name that describes the channel. The name is the primary identifier for the channel, and must be unique for your account in the AWS Region and channel group. </p>"""
    origin_endpoint_name: "aws_sdk_mediapackagev2.types.resource_name.ResourceName"
    """<p>The name that describes the origin endpoint. The name is the primary identifier for the origin endpoint, and and must be unique for your account in the AWS Region and channel. </p>"""
    policy: "aws_sdk_mediapackagev2.types.policy_text.PolicyText"
    """<p>The policy to attach to the specified origin endpoint.</p>"""
    cdn_auth_configuration: NotRequired[
        "aws_sdk_mediapackagev2.types.cdn_auth_configuration.CdnAuthConfiguration"
    ]
    """<p>The settings for using authorization headers between the MediaPackage endpoint and your CDN. </p> <p>For information about CDN authorization, see <a href=\"https://docs.aws.amazon.com/mediapackage/latest/userguide/cdn-auth.html\">CDN authorization in Elemental MediaPackage</a> in the MediaPackage user guide. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutOriginEndpointPolicyRequest) -> dict:
    out: dict = {}
    out["Policy"] = value["policy"]
    if "cdn_auth_configuration" in value:
        import aws_sdk_mediapackagev2.types.cdn_auth_configuration

        out["CdnAuthConfiguration"] = (
            aws_sdk_mediapackagev2.types.cdn_auth_configuration.serialize_json(
                value["cdn_auth_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> PutOriginEndpointPolicyRequest:
    out: PutOriginEndpointPolicyRequest = {}  # type: ignore[typeddict-item]
    if "Policy" in data:
        out["policy"] = data["Policy"]
    else:
        raise DeserializationError("PutOriginEndpointPolicyRequest.policy required")
    if "CdnAuthConfiguration" in data:
        import aws_sdk_mediapackagev2.types.cdn_auth_configuration

        out["cdn_auth_configuration"] = (
            aws_sdk_mediapackagev2.types.cdn_auth_configuration.deserialize_json(
                data["CdnAuthConfiguration"]
            )
        )
    return out
