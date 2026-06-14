"""Generated from Smithy shape ``com.amazonaws.workspacesweb#UpdatePortalRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workspaces_web.types.arn
    import aws_sdk_workspaces_web.types.authentication_type
    import aws_sdk_workspaces_web.types.display_name
    import aws_sdk_workspaces_web.types.instance_type
    import aws_sdk_workspaces_web.types.max_concurrent_sessions
    import aws_sdk_workspaces_web.types.portal_custom_domain


class UpdatePortalRequest(TypedDict):
    portal_arn: "aws_sdk_workspaces_web.types.arn.ARN"
    """<p>The ARN of the web portal.</p>"""
    display_name: NotRequired["aws_sdk_workspaces_web.types.display_name.DisplayName"]
    """<p>The name of the web portal. This is not visible to users who log into the web portal.</p>"""
    authentication_type: NotRequired[
        "aws_sdk_workspaces_web.types.authentication_type.AuthenticationType"
    ]
    """<p>The type of authentication integration points used when signing into the web portal. Defaults to <code>Standard</code>.</p> <p> <code>Standard</code> web portals are authenticated directly through your identity provider. You need to call <code>CreateIdentityProvider</code> to integrate your identity provider with your web portal. User and group access to your web portal is controlled through your identity provider.</p> <p> <code>IAM Identity Center</code> web portals are authenticated through IAM Identity Center. Identity sources (including external identity provider integration), plus user and group access to your web portal, can be configured in the IAM Identity Center.</p>"""
    instance_type: NotRequired[
        "aws_sdk_workspaces_web.types.instance_type.InstanceType"
    ]
    """<p>The type and resources of the underlying instance.</p>"""
    max_concurrent_sessions: NotRequired[
        "aws_sdk_workspaces_web.types.max_concurrent_sessions.MaxConcurrentSessions"
    ]
    """<p>The maximum number of concurrent sessions for the portal.</p>"""
    portal_custom_domain: NotRequired[
        "aws_sdk_workspaces_web.types.portal_custom_domain.PortalCustomDomain"
    ]
    """<p>The custom domain of the web portal that users access in order to start streaming sessions. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatePortalRequest) -> dict:
    out: dict = {}
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "authentication_type" in value:
        out["authenticationType"] = value["authentication_type"]
    if "instance_type" in value:
        out["instanceType"] = value["instance_type"]
    if "max_concurrent_sessions" in value:
        out["maxConcurrentSessions"] = value["max_concurrent_sessions"]
    if "portal_custom_domain" in value:
        out["portalCustomDomain"] = value["portal_custom_domain"]
    return out


def deserialize_json(data: dict) -> UpdatePortalRequest:
    out: UpdatePortalRequest = {}  # type: ignore[typeddict-item]
    if "displayName" in data:
        out["display_name"] = data["displayName"]
    if "authenticationType" in data:
        out["authentication_type"] = data["authenticationType"]
    if "instanceType" in data:
        out["instance_type"] = data["instanceType"]
    if "maxConcurrentSessions" in data:
        out["max_concurrent_sessions"] = data["maxConcurrentSessions"]
    if "portalCustomDomain" in data:
        out["portal_custom_domain"] = data["portalCustomDomain"]
    return out
