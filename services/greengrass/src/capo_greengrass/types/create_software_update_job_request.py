"""Generated from Smithy shape ``com.amazonaws.greengrass#CreateSoftwareUpdateJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_greengrass.types.__string
    import capo_greengrass.types.s3_url_signer_role
    import capo_greengrass.types.software_to_update
    import capo_greengrass.types.update_agent_log_level
    import capo_greengrass.types.update_targets
    import capo_greengrass.types.update_targets_architecture
    import capo_greengrass.types.update_targets_operating_system


class CreateSoftwareUpdateJobRequest(TypedDict, closed=True):
    amzn_client_token: NotRequired["capo_greengrass.types.__string.__string"]
    """A client token used to correlate requests and responses."""
    s3_url_signer_role: NotRequired[
        "capo_greengrass.types.s3_url_signer_role.S3UrlSignerRole"
    ]
    software_to_update: NotRequired[
        "capo_greengrass.types.software_to_update.SoftwareToUpdate"
    ]
    update_agent_log_level: NotRequired[
        "capo_greengrass.types.update_agent_log_level.UpdateAgentLogLevel"
    ]
    update_targets: NotRequired["capo_greengrass.types.update_targets.UpdateTargets"]
    update_targets_architecture: NotRequired[
        "capo_greengrass.types.update_targets_architecture.UpdateTargetsArchitecture"
    ]
    update_targets_operating_system: NotRequired[
        "capo_greengrass.types.update_targets_operating_system.UpdateTargetsOperatingSystem"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: CreateSoftwareUpdateJobRequest) -> dict:
    out: dict = {}
    if "s3_url_signer_role" in value:
        out["S3UrlSignerRole"] = value["s3_url_signer_role"]
    if "software_to_update" in value:
        import capo_greengrass.types.software_to_update

        out["SoftwareToUpdate"] = (
            capo_greengrass.types.software_to_update.serialize_json(
                value["software_to_update"]
            )
        )
    if "update_agent_log_level" in value:
        import capo_greengrass.types.update_agent_log_level

        out["UpdateAgentLogLevel"] = (
            capo_greengrass.types.update_agent_log_level.serialize_json(
                value["update_agent_log_level"]
            )
        )
    if "update_targets" in value:
        import capo_greengrass.types.update_targets

        out["UpdateTargets"] = capo_greengrass.types.update_targets.serialize_json(
            value["update_targets"]
        )
    if "update_targets_architecture" in value:
        import capo_greengrass.types.update_targets_architecture

        out["UpdateTargetsArchitecture"] = (
            capo_greengrass.types.update_targets_architecture.serialize_json(
                value["update_targets_architecture"]
            )
        )
    if "update_targets_operating_system" in value:
        import capo_greengrass.types.update_targets_operating_system

        out["UpdateTargetsOperatingSystem"] = (
            capo_greengrass.types.update_targets_operating_system.serialize_json(
                value["update_targets_operating_system"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateSoftwareUpdateJobRequest:
    out: CreateSoftwareUpdateJobRequest = {}  # type: ignore[typeddict-item]
    if "S3UrlSignerRole" in data:
        out["s3_url_signer_role"] = data["S3UrlSignerRole"]
    if "SoftwareToUpdate" in data:
        import capo_greengrass.types.software_to_update

        out["software_to_update"] = (
            capo_greengrass.types.software_to_update.deserialize_json(
                data["SoftwareToUpdate"]
            )
        )
    if "UpdateAgentLogLevel" in data:
        import capo_greengrass.types.update_agent_log_level

        out["update_agent_log_level"] = (
            capo_greengrass.types.update_agent_log_level.deserialize_json(
                data["UpdateAgentLogLevel"]
            )
        )
    if "UpdateTargets" in data:
        import capo_greengrass.types.update_targets

        out["update_targets"] = capo_greengrass.types.update_targets.deserialize_json(
            data["UpdateTargets"]
        )
    if "UpdateTargetsArchitecture" in data:
        import capo_greengrass.types.update_targets_architecture

        out["update_targets_architecture"] = (
            capo_greengrass.types.update_targets_architecture.deserialize_json(
                data["UpdateTargetsArchitecture"]
            )
        )
    if "UpdateTargetsOperatingSystem" in data:
        import capo_greengrass.types.update_targets_operating_system

        out["update_targets_operating_system"] = (
            capo_greengrass.types.update_targets_operating_system.deserialize_json(
                data["UpdateTargetsOperatingSystem"]
            )
        )
    return out
