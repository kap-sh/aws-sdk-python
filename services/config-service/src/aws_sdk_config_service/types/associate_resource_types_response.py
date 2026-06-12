"""Generated from Smithy shape ``com.amazonaws.configservice#AssociateResourceTypesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_config_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_config_service.types.configuration_recorder


class AssociateResourceTypesResponse(TypedDict):
    configuration_recorder: (
        "aws_sdk_config_service.types.configuration_recorder.ConfigurationRecorder"
    )


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociateResourceTypesResponse) -> dict:
    out: dict = {}
    import aws_sdk_config_service.types.configuration_recorder

    out["ConfigurationRecorder"] = (
        aws_sdk_config_service.types.configuration_recorder.serialize_aws_json_1_1(
            value["configuration_recorder"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> AssociateResourceTypesResponse:
    out: AssociateResourceTypesResponse = {}  # type: ignore[typeddict-item]
    if "ConfigurationRecorder" in data:
        import aws_sdk_config_service.types.configuration_recorder

        out["configuration_recorder"] = (
            aws_sdk_config_service.types.configuration_recorder.deserialize_aws_json_1_1(
                data["ConfigurationRecorder"]
            )
        )
    else:
        raise DeserializationError(
            "AssociateResourceTypesResponse.configuration_recorder required"
        )
    return out
