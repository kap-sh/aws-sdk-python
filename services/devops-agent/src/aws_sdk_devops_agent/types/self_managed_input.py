"""Generated from Smithy shape ``com.amazonaws.devopsagent#SelfManagedInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.certificate_string
    import aws_sdk_devops_agent.types.resource_configuration_arn


class SelfManagedInput(TypedDict):
    resource_configuration_id: (
        "aws_sdk_devops_agent.types.resource_configuration_arn.ResourceConfigurationArn"
    )
    """<p>The ID or ARN of the resource configuration.</p>"""
    certificate: NotRequired[
        "aws_sdk_devops_agent.types.certificate_string.CertificateString"
    ]
    """<p>Certificate for the Private Connection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SelfManagedInput) -> dict:
    out: dict = {}
    out["resourceConfigurationId"] = value["resource_configuration_id"]
    if "certificate" in value:
        out["certificate"] = value["certificate"]
    return out


def deserialize_json(data: dict) -> SelfManagedInput:
    out: SelfManagedInput = {}  # type: ignore[typeddict-item]
    if "resourceConfigurationId" in data:
        out["resource_configuration_id"] = data["resourceConfigurationId"]
    else:
        raise DeserializationError(
            "SelfManagedInput.resource_configuration_id required"
        )
    if "certificate" in data:
        out["certificate"] = data["certificate"]
    return out
