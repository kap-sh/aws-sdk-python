"""Generated from Smithy shape ``com.amazonaws.configservice#DisassociateResourceTypesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_config_service.errors import DeserializationError

if TYPE_CHECKING:
    import capo_config_service.types.configuration_recorder


class DisassociateResourceTypesResponse(TypedDict, closed=True):
    configuration_recorder: (
        "capo_config_service.types.configuration_recorder.ConfigurationRecorder"
    )


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DisassociateResourceTypesResponse) -> dict:
    out: dict = {}
    import capo_config_service.types.configuration_recorder

    out["ConfigurationRecorder"] = (
        capo_config_service.types.configuration_recorder.serialize_aws_json_1_1(
            value["configuration_recorder"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DisassociateResourceTypesResponse:
    out: DisassociateResourceTypesResponse = {}  # type: ignore[typeddict-item]
    if "ConfigurationRecorder" in data:
        import capo_config_service.types.configuration_recorder

        out["configuration_recorder"] = (
            capo_config_service.types.configuration_recorder.deserialize_aws_json_1_1(
                data["ConfigurationRecorder"]
            )
        )
    else:
        raise DeserializationError(
            "DisassociateResourceTypesResponse.configuration_recorder required"
        )
    return out
