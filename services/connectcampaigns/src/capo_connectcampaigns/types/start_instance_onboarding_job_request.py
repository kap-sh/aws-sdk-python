"""Generated from Smithy shape ``com.amazonaws.connectcampaigns#StartInstanceOnboardingJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_connectcampaigns.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connectcampaigns.types.encryption_config
    import capo_connectcampaigns.types.instance_id


class StartInstanceOnboardingJobRequest(TypedDict, closed=True):
    connect_instance_id: "capo_connectcampaigns.types.instance_id.InstanceId"
    encryption_config: "capo_connectcampaigns.types.encryption_config.EncryptionConfig"


# --- restJson1 ser/de ---
def serialize_json(value: StartInstanceOnboardingJobRequest) -> dict:
    out: dict = {}
    import capo_connectcampaigns.types.encryption_config

    out["encryptionConfig"] = (
        capo_connectcampaigns.types.encryption_config.serialize_json(
            value["encryption_config"]
        )
    )
    return out


def deserialize_json(data: dict) -> StartInstanceOnboardingJobRequest:
    out: StartInstanceOnboardingJobRequest = {}  # type: ignore[typeddict-item]
    if "encryptionConfig" in data:
        import capo_connectcampaigns.types.encryption_config

        out["encryption_config"] = (
            capo_connectcampaigns.types.encryption_config.deserialize_json(
                data["encryptionConfig"]
            )
        )
    else:
        raise DeserializationError(
            "StartInstanceOnboardingJobRequest.encryption_config required"
        )
    return out
