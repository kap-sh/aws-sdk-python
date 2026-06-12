"""Generated from Smithy shape ``com.amazonaws.configservice#PutRemediationConfigurationsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_config_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_config_service.types.remediation_configurations


class PutRemediationConfigurationsRequest(TypedDict):
    remediation_configurations: "aws_sdk_config_service.types.remediation_configurations.RemediationConfigurations"
    """<p>A list of remediation configuration objects.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutRemediationConfigurationsRequest) -> dict:
    out: dict = {}
    import aws_sdk_config_service.types.remediation_configurations

    out["RemediationConfigurations"] = (
        aws_sdk_config_service.types.remediation_configurations.serialize_aws_json_1_1(
            value["remediation_configurations"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutRemediationConfigurationsRequest:
    out: PutRemediationConfigurationsRequest = {}  # type: ignore[typeddict-item]
    if "RemediationConfigurations" in data:
        import aws_sdk_config_service.types.remediation_configurations

        out["remediation_configurations"] = (
            aws_sdk_config_service.types.remediation_configurations.deserialize_aws_json_1_1(
                data["RemediationConfigurations"]
            )
        )
    else:
        raise DeserializationError(
            "PutRemediationConfigurationsRequest.remediation_configurations required"
        )
    return out
