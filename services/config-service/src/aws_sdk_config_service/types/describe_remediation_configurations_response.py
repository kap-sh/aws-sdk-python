"""Generated from Smithy shape ``com.amazonaws.configservice#DescribeRemediationConfigurationsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_config_service.types.remediation_configurations


class DescribeRemediationConfigurationsResponse(TypedDict):
    remediation_configurations: NotRequired[
        "aws_sdk_config_service.types.remediation_configurations.RemediationConfigurations"
    ]
    """<p>Returns a remediation configuration object.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeRemediationConfigurationsResponse) -> dict:
    out: dict = {}
    if "remediation_configurations" in value:
        import aws_sdk_config_service.types.remediation_configurations

        out["RemediationConfigurations"] = (
            aws_sdk_config_service.types.remediation_configurations.serialize_aws_json_1_1(
                value["remediation_configurations"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeRemediationConfigurationsResponse:
    out: DescribeRemediationConfigurationsResponse = {}  # type: ignore[typeddict-item]
    if "RemediationConfigurations" in data:
        import aws_sdk_config_service.types.remediation_configurations

        out["remediation_configurations"] = (
            aws_sdk_config_service.types.remediation_configurations.deserialize_aws_json_1_1(
                data["RemediationConfigurations"]
            )
        )
    return out
