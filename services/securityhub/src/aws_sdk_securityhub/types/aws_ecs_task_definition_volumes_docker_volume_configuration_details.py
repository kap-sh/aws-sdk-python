"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEcsTaskDefinitionVolumesDockerVolumeConfigurationDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.boolean
    import aws_sdk_securityhub.types.field_map
    import aws_sdk_securityhub.types.non_empty_string


class AwsEcsTaskDefinitionVolumesDockerVolumeConfigurationDetails(
    TypedDict, closed=True
):
    autoprovision: NotRequired["aws_sdk_securityhub.types.boolean.Boolean"]
    """<p>Whether to create the Docker volume automatically if it does not already exist.</p>"""
    driver: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The Docker volume driver to use.</p>"""
    driver_opts: NotRequired["aws_sdk_securityhub.types.field_map.FieldMap"]
    """<p>A map of Docker driver-specific options that are passed through.</p>"""
    labels: NotRequired["aws_sdk_securityhub.types.field_map.FieldMap"]
    """<p>Custom metadata to add to the Docker volume.</p>"""
    scope: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The scope for the Docker volume that determines its lifecycle. Docker volumes that are scoped to a task are provisioned automatically when the task starts and destroyed when the task stops. Docker volumes that are shared persist after the task stops. Valid values are <code>shared</code> or <code>task</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsEcsTaskDefinitionVolumesDockerVolumeConfigurationDetails,
) -> dict:
    out: dict = {}
    if "autoprovision" in value:
        out["Autoprovision"] = value["autoprovision"]
    if "driver" in value:
        out["Driver"] = value["driver"]
    if "driver_opts" in value:
        import aws_sdk_securityhub.types.field_map

        out["DriverOpts"] = aws_sdk_securityhub.types.field_map.serialize_json(
            value["driver_opts"]
        )
    if "labels" in value:
        import aws_sdk_securityhub.types.field_map

        out["Labels"] = aws_sdk_securityhub.types.field_map.serialize_json(
            value["labels"]
        )
    if "scope" in value:
        out["Scope"] = value["scope"]
    return out


def deserialize_json(
    data: dict,
) -> AwsEcsTaskDefinitionVolumesDockerVolumeConfigurationDetails:
    out: AwsEcsTaskDefinitionVolumesDockerVolumeConfigurationDetails = {}  # type: ignore[typeddict-item]
    if "Autoprovision" in data:
        out["autoprovision"] = data["Autoprovision"]
    if "Driver" in data:
        out["driver"] = data["Driver"]
    if "DriverOpts" in data:
        import aws_sdk_securityhub.types.field_map

        out["driver_opts"] = aws_sdk_securityhub.types.field_map.deserialize_json(
            data["DriverOpts"]
        )
    if "Labels" in data:
        import aws_sdk_securityhub.types.field_map

        out["labels"] = aws_sdk_securityhub.types.field_map.deserialize_json(
            data["Labels"]
        )
    if "Scope" in data:
        out["scope"] = data["Scope"]
    return out
