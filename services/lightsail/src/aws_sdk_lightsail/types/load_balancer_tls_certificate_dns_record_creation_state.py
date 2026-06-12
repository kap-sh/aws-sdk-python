"""Generated from Smithy shape ``com.amazonaws.lightsail#LoadBalancerTlsCertificateDnsRecordCreationState``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.load_balancer_tls_certificate_dns_record_creation_state_code
    import aws_sdk_lightsail.types.string


class LoadBalancerTlsCertificateDnsRecordCreationState(TypedDict):
    code: NotRequired[
        "aws_sdk_lightsail.types.load_balancer_tls_certificate_dns_record_creation_state_code.LoadBalancerTlsCertificateDnsRecordCreationStateCode"
    ]
    """<p>The status code for the automated DNS record creation.</p> <p>Following are the possible values:</p> <ul> <li> <p> <code>SUCCEEDED</code> - The validation records were successfully added.</p> </li> <li> <p> <code>STARTED</code> - The automatic DNS record creation has started.</p> </li> <li> <p> <code>FAILED</code> - The validation record addition failed.</p> </li> </ul>"""
    message: NotRequired["aws_sdk_lightsail.types.string.string"]
    """<p>The message that describes the reason for the status code.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: LoadBalancerTlsCertificateDnsRecordCreationState,
) -> dict:
    out: dict = {}
    if "code" in value:
        import aws_sdk_lightsail.types.load_balancer_tls_certificate_dns_record_creation_state_code

        out["code"] = (
            aws_sdk_lightsail.types.load_balancer_tls_certificate_dns_record_creation_state_code.serialize_aws_json_1_1(
                value["code"]
            )
        )
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> LoadBalancerTlsCertificateDnsRecordCreationState:
    out: LoadBalancerTlsCertificateDnsRecordCreationState = {}  # type: ignore[typeddict-item]
    if "code" in data:
        import aws_sdk_lightsail.types.load_balancer_tls_certificate_dns_record_creation_state_code

        out["code"] = (
            aws_sdk_lightsail.types.load_balancer_tls_certificate_dns_record_creation_state_code.deserialize_aws_json_1_1(
                data["code"]
            )
        )
    if "message" in data:
        out["message"] = data["message"]
    return out
