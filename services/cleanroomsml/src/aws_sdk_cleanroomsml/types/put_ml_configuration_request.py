"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#PutMLConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cleanroomsml.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanroomsml.types.ml_output_configuration
    import aws_sdk_cleanroomsml.types.uuid


class PutMLConfigurationRequest(TypedDict, closed=True):
    membership_identifier: "aws_sdk_cleanroomsml.types.uuid.UUID"
    """<p>The membership ID of the member that is being configured.</p>"""
    default_output_location: (
        "aws_sdk_cleanroomsml.types.ml_output_configuration.MLOutputConfiguration"
    )
    """<p>The default Amazon S3 location where ML output is stored for the specified member.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutMLConfigurationRequest) -> dict:
    out: dict = {}
    import aws_sdk_cleanroomsml.types.ml_output_configuration

    out["defaultOutputLocation"] = (
        aws_sdk_cleanroomsml.types.ml_output_configuration.serialize_json(
            value["default_output_location"]
        )
    )
    return out


def deserialize_json(data: dict) -> PutMLConfigurationRequest:
    out: PutMLConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "defaultOutputLocation" in data:
        import aws_sdk_cleanroomsml.types.ml_output_configuration

        out["default_output_location"] = (
            aws_sdk_cleanroomsml.types.ml_output_configuration.deserialize_json(
                data["defaultOutputLocation"]
            )
        )
    else:
        raise DeserializationError(
            "PutMLConfigurationRequest.default_output_location required"
        )
    return out
