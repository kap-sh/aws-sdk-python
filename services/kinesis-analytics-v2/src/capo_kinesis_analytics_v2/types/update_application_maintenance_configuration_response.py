"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#UpdateApplicationMaintenanceConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.application_maintenance_configuration_description
    import capo_kinesis_analytics_v2.types.resource_arn


class UpdateApplicationMaintenanceConfigurationResponse(TypedDict, closed=True):
    application_arn: NotRequired[
        "capo_kinesis_analytics_v2.types.resource_arn.ResourceARN"
    ]
    """<p>The Amazon Resource Name (ARN) of the application.</p>"""
    application_maintenance_configuration_description: NotRequired[
        "capo_kinesis_analytics_v2.types.application_maintenance_configuration_description.ApplicationMaintenanceConfigurationDescription"
    ]
    """<p>The application maintenance configuration description after the update.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: UpdateApplicationMaintenanceConfigurationResponse,
) -> dict:
    out: dict = {}
    if "application_arn" in value:
        out["ApplicationARN"] = value["application_arn"]
    if "application_maintenance_configuration_description" in value:
        import capo_kinesis_analytics_v2.types.application_maintenance_configuration_description

        out["ApplicationMaintenanceConfigurationDescription"] = (
            capo_kinesis_analytics_v2.types.application_maintenance_configuration_description.serialize_aws_json_1_1(
                value["application_maintenance_configuration_description"]
            )
        )
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> UpdateApplicationMaintenanceConfigurationResponse:
    out: UpdateApplicationMaintenanceConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "ApplicationARN" in data:
        out["application_arn"] = data["ApplicationARN"]
    if "ApplicationMaintenanceConfigurationDescription" in data:
        import capo_kinesis_analytics_v2.types.application_maintenance_configuration_description

        out["application_maintenance_configuration_description"] = (
            capo_kinesis_analytics_v2.types.application_maintenance_configuration_description.deserialize_aws_json_1_1(
                data["ApplicationMaintenanceConfigurationDescription"]
            )
        )
    return out
