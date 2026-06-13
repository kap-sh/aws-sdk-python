"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ProtectedJobResultConfigurationInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.protected_job_output_configuration_input


class ProtectedJobResultConfigurationInput(TypedDict):
    output_configuration: "aws_sdk_cleanrooms.types.protected_job_output_configuration_input.ProtectedJobOutputConfigurationInput"
    """<p> The output configuration for a protected job result.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProtectedJobResultConfigurationInput) -> dict:
    out: dict = {}
    import aws_sdk_cleanrooms.types.protected_job_output_configuration_input

    out["outputConfiguration"] = (
        aws_sdk_cleanrooms.types.protected_job_output_configuration_input.serialize_json(
            value["output_configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> ProtectedJobResultConfigurationInput:
    out: ProtectedJobResultConfigurationInput = {}  # type: ignore[typeddict-item]
    if "outputConfiguration" in data:
        import aws_sdk_cleanrooms.types.protected_job_output_configuration_input

        out["output_configuration"] = (
            aws_sdk_cleanrooms.types.protected_job_output_configuration_input.deserialize_json(
                data["outputConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "ProtectedJobResultConfigurationInput.output_configuration required"
        )
    return out
