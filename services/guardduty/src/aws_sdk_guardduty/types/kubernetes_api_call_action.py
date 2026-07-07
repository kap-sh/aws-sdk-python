"""Generated from Smithy shape ``com.amazonaws.guardduty#KubernetesApiCallAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.integer
    import aws_sdk_guardduty.types.remote_ip_details
    import aws_sdk_guardduty.types.source_ips
    import aws_sdk_guardduty.types.string


class KubernetesApiCallAction(TypedDict, closed=True):
    request_uri: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The Kubernetes API request URI.</p>"""
    verb: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The Kubernetes API request HTTP verb.</p>"""
    resource: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The resource component in the Kubernetes API call action.</p>"""
    subresource: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The name of the sub-resource in the Kubernetes API call action.</p>"""
    namespace: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The name of the namespace where the Kubernetes API call action takes place.</p>"""
    resource_name: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The name of the resource in the Kubernetes API call action.</p>"""
    source_ips: NotRequired["aws_sdk_guardduty.types.source_ips.SourceIps"]
    """<p>The IP of the Kubernetes API caller and the IPs of any proxies or load balancers between the caller and the API endpoint.</p>"""
    user_agent: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The user agent of the caller of the Kubernetes API.</p>"""
    remote_ip_details: NotRequired[
        "aws_sdk_guardduty.types.remote_ip_details.RemoteIpDetails"
    ]
    status_code: NotRequired["aws_sdk_guardduty.types.integer.Integer"]
    """<p>The resulting HTTP response code of the Kubernetes API call action.</p>"""
    parameters: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>Parameters related to the Kubernetes API call action.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KubernetesApiCallAction) -> dict:
    out: dict = {}
    if "request_uri" in value:
        out["requestUri"] = value["request_uri"]
    if "verb" in value:
        out["verb"] = value["verb"]
    if "resource" in value:
        out["resource"] = value["resource"]
    if "subresource" in value:
        out["subresource"] = value["subresource"]
    if "namespace" in value:
        out["namespace"] = value["namespace"]
    if "resource_name" in value:
        out["resourceName"] = value["resource_name"]
    if "source_ips" in value:
        import aws_sdk_guardduty.types.source_ips

        out["sourceIPs"] = aws_sdk_guardduty.types.source_ips.serialize_json(
            value["source_ips"]
        )
    if "user_agent" in value:
        out["userAgent"] = value["user_agent"]
    if "remote_ip_details" in value:
        import aws_sdk_guardduty.types.remote_ip_details

        out["remoteIpDetails"] = (
            aws_sdk_guardduty.types.remote_ip_details.serialize_json(
                value["remote_ip_details"]
            )
        )
    if "status_code" in value:
        out["statusCode"] = value["status_code"]
    if "parameters" in value:
        out["parameters"] = value["parameters"]
    return out


def deserialize_json(data: dict) -> KubernetesApiCallAction:
    out: KubernetesApiCallAction = {}  # type: ignore[typeddict-item]
    if "requestUri" in data:
        out["request_uri"] = data["requestUri"]
    if "verb" in data:
        out["verb"] = data["verb"]
    if "resource" in data:
        out["resource"] = data["resource"]
    if "subresource" in data:
        out["subresource"] = data["subresource"]
    if "namespace" in data:
        out["namespace"] = data["namespace"]
    if "resourceName" in data:
        out["resource_name"] = data["resourceName"]
    if "sourceIPs" in data:
        import aws_sdk_guardduty.types.source_ips

        out["source_ips"] = aws_sdk_guardduty.types.source_ips.deserialize_json(
            data["sourceIPs"]
        )
    if "userAgent" in data:
        out["user_agent"] = data["userAgent"]
    if "remoteIpDetails" in data:
        import aws_sdk_guardduty.types.remote_ip_details

        out["remote_ip_details"] = (
            aws_sdk_guardduty.types.remote_ip_details.deserialize_json(
                data["remoteIpDetails"]
            )
        )
    if "statusCode" in data:
        out["status_code"] = data["statusCode"]
    if "parameters" in data:
        out["parameters"] = data["parameters"]
    return out
