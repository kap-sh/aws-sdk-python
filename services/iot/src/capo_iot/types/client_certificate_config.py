"""Generated from Smithy shape ``com.amazonaws.iot#ClientCertificateConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.client_certificate_callback_arn


class ClientCertificateConfig(TypedDict, closed=True):
    client_certificate_callback_arn: NotRequired[
        "capo_iot.types.client_certificate_callback_arn.ClientCertificateCallbackArn"
    ]
    """<p>The ARN of the Lambda function that IoT invokes after mutual TLS authentication during the connection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ClientCertificateConfig) -> dict:
    out: dict = {}
    if "client_certificate_callback_arn" in value:
        out["clientCertificateCallbackArn"] = value["client_certificate_callback_arn"]
    return out


def deserialize_json(data: dict) -> ClientCertificateConfig:
    out: ClientCertificateConfig = {}  # type: ignore[typeddict-item]
    if "clientCertificateCallbackArn" in data:
        out["client_certificate_callback_arn"] = data["clientCertificateCallbackArn"]
    return out
