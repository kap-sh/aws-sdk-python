"""Generated from Smithy shape ``com.amazonaws.lightsail#SendContactMethodVerificationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_lightsail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.contact_method_verification_protocol


class SendContactMethodVerificationRequest(TypedDict, closed=True):
    protocol: "aws_sdk_lightsail.types.contact_method_verification_protocol.ContactMethodVerificationProtocol"
    """<p>The protocol to verify, such as <code>Email</code> or <code>SMS</code> (text messaging).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SendContactMethodVerificationRequest) -> dict:
    out: dict = {}
    import aws_sdk_lightsail.types.contact_method_verification_protocol

    out["protocol"] = (
        aws_sdk_lightsail.types.contact_method_verification_protocol.serialize_aws_json_1_1(
            value["protocol"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> SendContactMethodVerificationRequest:
    out: SendContactMethodVerificationRequest = {}  # type: ignore[typeddict-item]
    if "protocol" in data:
        import aws_sdk_lightsail.types.contact_method_verification_protocol

        out["protocol"] = (
            aws_sdk_lightsail.types.contact_method_verification_protocol.deserialize_aws_json_1_1(
                data["protocol"]
            )
        )
    else:
        raise DeserializationError(
            "SendContactMethodVerificationRequest.protocol required"
        )
    return out
