"""Generated from Smithy shape ``com.amazonaws.devopsagent#UpdatePrivateConnectionCertificateInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.certificate_string
    import aws_sdk_devops_agent.types.private_connection_name


class UpdatePrivateConnectionCertificateInput(TypedDict, closed=True):
    name: "aws_sdk_devops_agent.types.private_connection_name.PrivateConnectionName"
    """<p>The name of the Private Connection.</p>"""
    certificate: "aws_sdk_devops_agent.types.certificate_string.CertificateString"
    """<p>The new certificate for the Private Connection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatePrivateConnectionCertificateInput) -> dict:
    out: dict = {}
    out["certificate"] = value["certificate"]
    return out


def deserialize_json(data: dict) -> UpdatePrivateConnectionCertificateInput:
    out: UpdatePrivateConnectionCertificateInput = {}  # type: ignore[typeddict-item]
    if "certificate" in data:
        out["certificate"] = data["certificate"]
    else:
        raise DeserializationError(
            "UpdatePrivateConnectionCertificateInput.certificate required"
        )
    return out
