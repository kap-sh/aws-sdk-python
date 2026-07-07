"""Generated from Smithy shape ``com.amazonaws.lightsail#LoadBalancerTlsCertificateSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.boolean
    import aws_sdk_lightsail.types.resource_name


class LoadBalancerTlsCertificateSummary(TypedDict, closed=True):
    name: NotRequired["aws_sdk_lightsail.types.resource_name.ResourceName"]
    """<p>The name of the SSL/TLS certificate.</p>"""
    is_attached: NotRequired["aws_sdk_lightsail.types.boolean.boolean"]
    """<p>When <code>true</code>, the SSL/TLS certificate is attached to the Lightsail load balancer.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LoadBalancerTlsCertificateSummary) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "is_attached" in value:
        out["isAttached"] = value["is_attached"]
    return out


def deserialize_aws_json_1_1(data: dict) -> LoadBalancerTlsCertificateSummary:
    out: LoadBalancerTlsCertificateSummary = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "isAttached" in data:
        out["is_attached"] = data["isAttached"]
    return out
