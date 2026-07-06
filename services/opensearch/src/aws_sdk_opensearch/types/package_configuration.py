"""Generated from Smithy shape ``com.amazonaws.opensearch#PackageConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_opensearch.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.boolean
    import aws_sdk_opensearch.types.license_filepath
    import aws_sdk_opensearch.types.requirement_level


class PackageConfiguration(TypedDict, closed=True):
    license_requirement: "aws_sdk_opensearch.types.requirement_level.RequirementLevel"
    """<p>The license requirements for the package.</p>"""
    license_filepath: NotRequired[
        "aws_sdk_opensearch.types.license_filepath.LicenseFilepath"
    ]
    """<p>The relative file path for the license associated with the package.</p>"""
    configuration_requirement: (
        "aws_sdk_opensearch.types.requirement_level.RequirementLevel"
    )
    """<p>The configuration requirements for the package.</p>"""
    requires_restart_for_configuration_update: NotRequired[
        "aws_sdk_opensearch.types.boolean.Boolean"
    ]
    """<p>This indicates whether a B/G deployment is required for updating the configuration that the plugin is prerequisite for.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PackageConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_opensearch.types.requirement_level

    out["LicenseRequirement"] = (
        aws_sdk_opensearch.types.requirement_level.serialize_json(
            value["license_requirement"]
        )
    )
    if "license_filepath" in value:
        out["LicenseFilepath"] = value["license_filepath"]
    import aws_sdk_opensearch.types.requirement_level

    out["ConfigurationRequirement"] = (
        aws_sdk_opensearch.types.requirement_level.serialize_json(
            value["configuration_requirement"]
        )
    )
    if "requires_restart_for_configuration_update" in value:
        out["RequiresRestartForConfigurationUpdate"] = value[
            "requires_restart_for_configuration_update"
        ]
    return out


def deserialize_json(data: dict) -> PackageConfiguration:
    out: PackageConfiguration = {}  # type: ignore[typeddict-item]
    if "LicenseRequirement" in data:
        import aws_sdk_opensearch.types.requirement_level

        out["license_requirement"] = (
            aws_sdk_opensearch.types.requirement_level.deserialize_json(
                data["LicenseRequirement"]
            )
        )
    else:
        raise DeserializationError("PackageConfiguration.license_requirement required")
    if "LicenseFilepath" in data:
        out["license_filepath"] = data["LicenseFilepath"]
    if "ConfigurationRequirement" in data:
        import aws_sdk_opensearch.types.requirement_level

        out["configuration_requirement"] = (
            aws_sdk_opensearch.types.requirement_level.deserialize_json(
                data["ConfigurationRequirement"]
            )
        )
    else:
        raise DeserializationError(
            "PackageConfiguration.configuration_requirement required"
        )
    if "RequiresRestartForConfigurationUpdate" in data:
        out["requires_restart_for_configuration_update"] = data[
            "RequiresRestartForConfigurationUpdate"
        ]
    return out
