"""Generated from Smithy shape ``com.amazonaws.securityhub#ExternalIntegrationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class ExternalIntegrationConfiguration(TypedDict, closed=True):
    connector_arn: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The ARN of the connector that establishes the integration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExternalIntegrationConfiguration) -> dict:
    out: dict = {}
    if "connector_arn" in value:
        out["ConnectorArn"] = value["connector_arn"]
    return out


def deserialize_json(data: dict) -> ExternalIntegrationConfiguration:
    out: ExternalIntegrationConfiguration = {}  # type: ignore[typeddict-item]
    if "ConnectorArn" in data:
        out["connector_arn"] = data["ConnectorArn"]
    return out
