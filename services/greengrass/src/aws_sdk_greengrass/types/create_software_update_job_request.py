"""Generated from Smithy shape ``com.amazonaws.greengrass#CreateSoftwareUpdateJobRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_greengrass.types.__string
    import aws_sdk_greengrass.types.s3_url_signer_role
    import aws_sdk_greengrass.types.software_to_update
    import aws_sdk_greengrass.types.update_agent_log_level
    import aws_sdk_greengrass.types.update_targets
    import aws_sdk_greengrass.types.update_targets_architecture
    import aws_sdk_greengrass.types.update_targets_operating_system


class CreateSoftwareUpdateJobRequest(TypedDict):
    amzn_client_token: NotRequired["aws_sdk_greengrass.types.__string.__string"]
    """A client token used to correlate requests and responses."""
    s3_url_signer_role: NotRequired[
        "aws_sdk_greengrass.types.s3_url_signer_role.S3UrlSignerRole"
    ]
    software_to_update: NotRequired[
        "aws_sdk_greengrass.types.software_to_update.SoftwareToUpdate"
    ]
    update_agent_log_level: NotRequired[
        "aws_sdk_greengrass.types.update_agent_log_level.UpdateAgentLogLevel"
    ]
    update_targets: NotRequired["aws_sdk_greengrass.types.update_targets.UpdateTargets"]
    update_targets_architecture: NotRequired[
        "aws_sdk_greengrass.types.update_targets_architecture.UpdateTargetsArchitecture"
    ]
    update_targets_operating_system: NotRequired[
        "aws_sdk_greengrass.types.update_targets_operating_system.UpdateTargetsOperatingSystem"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: CreateSoftwareUpdateJobRequest) -> dict:
    out: dict = {}
    if "s3_url_signer_role" in value:
        out["S3UrlSignerRole"] = value["s3_url_signer_role"]
    if "software_to_update" in value:
        import aws_sdk_greengrass.types.software_to_update

        out["SoftwareToUpdate"] = (
            aws_sdk_greengrass.types.software_to_update.serialize_json(
                value["software_to_update"]
            )
        )
    if "update_agent_log_level" in value:
        import aws_sdk_greengrass.types.update_agent_log_level

        out["UpdateAgentLogLevel"] = (
            aws_sdk_greengrass.types.update_agent_log_level.serialize_json(
                value["update_agent_log_level"]
            )
        )
    if "update_targets" in value:
        import aws_sdk_greengrass.types.update_targets

        out["UpdateTargets"] = aws_sdk_greengrass.types.update_targets.serialize_json(
            value["update_targets"]
        )
    if "update_targets_architecture" in value:
        import aws_sdk_greengrass.types.update_targets_architecture

        out["UpdateTargetsArchitecture"] = (
            aws_sdk_greengrass.types.update_targets_architecture.serialize_json(
                value["update_targets_architecture"]
            )
        )
    if "update_targets_operating_system" in value:
        import aws_sdk_greengrass.types.update_targets_operating_system

        out["UpdateTargetsOperatingSystem"] = (
            aws_sdk_greengrass.types.update_targets_operating_system.serialize_json(
                value["update_targets_operating_system"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateSoftwareUpdateJobRequest:
    out: CreateSoftwareUpdateJobRequest = {}  # type: ignore[typeddict-item]
    if "S3UrlSignerRole" in data:
        out["s3_url_signer_role"] = data["S3UrlSignerRole"]
    if "SoftwareToUpdate" in data:
        import aws_sdk_greengrass.types.software_to_update

        out["software_to_update"] = (
            aws_sdk_greengrass.types.software_to_update.deserialize_json(
                data["SoftwareToUpdate"]
            )
        )
    if "UpdateAgentLogLevel" in data:
        import aws_sdk_greengrass.types.update_agent_log_level

        out["update_agent_log_level"] = (
            aws_sdk_greengrass.types.update_agent_log_level.deserialize_json(
                data["UpdateAgentLogLevel"]
            )
        )
    if "UpdateTargets" in data:
        import aws_sdk_greengrass.types.update_targets

        out["update_targets"] = (
            aws_sdk_greengrass.types.update_targets.deserialize_json(
                data["UpdateTargets"]
            )
        )
    if "UpdateTargetsArchitecture" in data:
        import aws_sdk_greengrass.types.update_targets_architecture

        out["update_targets_architecture"] = (
            aws_sdk_greengrass.types.update_targets_architecture.deserialize_json(
                data["UpdateTargetsArchitecture"]
            )
        )
    if "UpdateTargetsOperatingSystem" in data:
        import aws_sdk_greengrass.types.update_targets_operating_system

        out["update_targets_operating_system"] = (
            aws_sdk_greengrass.types.update_targets_operating_system.deserialize_json(
                data["UpdateTargetsOperatingSystem"]
            )
        )
    return out
