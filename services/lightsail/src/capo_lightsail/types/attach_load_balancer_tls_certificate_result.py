"""Generated from Smithy shape ``com.amazonaws.lightsail#AttachLoadBalancerTlsCertificateResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.operation_list


class AttachLoadBalancerTlsCertificateResult(TypedDict, closed=True):
    operations: NotRequired["capo_lightsail.types.operation_list.OperationList"]
    """<p>An array of objects that describe the result of the action, such as the status of the request, the timestamp of the request, and the resources affected by the request.</p> <p>These SSL/TLS certificates are only usable by Lightsail load balancers. You can't get the certificate and use it for another purpose.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AttachLoadBalancerTlsCertificateResult) -> dict:
    out: dict = {}
    if "operations" in value:
        import capo_lightsail.types.operation_list

        out["operations"] = capo_lightsail.types.operation_list.serialize_aws_json_1_1(
            value["operations"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AttachLoadBalancerTlsCertificateResult:
    out: AttachLoadBalancerTlsCertificateResult = {}  # type: ignore[typeddict-item]
    if "operations" in data:
        import capo_lightsail.types.operation_list

        out["operations"] = (
            capo_lightsail.types.operation_list.deserialize_aws_json_1_1(
                data["operations"]
            )
        )
    return out
