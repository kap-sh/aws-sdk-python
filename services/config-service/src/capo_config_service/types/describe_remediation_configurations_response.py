"""Generated from Smithy shape ``com.amazonaws.configservice#DescribeRemediationConfigurationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.remediation_configurations


class DescribeRemediationConfigurationsResponse(TypedDict, closed=True):
    remediation_configurations: NotRequired[
        "capo_config_service.types.remediation_configurations.RemediationConfigurations"
    ]
    """<p>Returns a remediation configuration object.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeRemediationConfigurationsResponse) -> dict:
    out: dict = {}
    if "remediation_configurations" in value:
        import capo_config_service.types.remediation_configurations

        out["RemediationConfigurations"] = (
            capo_config_service.types.remediation_configurations.serialize_aws_json_1_1(
                value["remediation_configurations"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeRemediationConfigurationsResponse:
    out: DescribeRemediationConfigurationsResponse = {}  # type: ignore[typeddict-item]
    if "RemediationConfigurations" in data:
        import capo_config_service.types.remediation_configurations

        out["remediation_configurations"] = (
            capo_config_service.types.remediation_configurations.deserialize_aws_json_1_1(
                data["RemediationConfigurations"]
            )
        )
    return out
