"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ProtectedJobResultConfigurationOutput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.protected_job_output_configuration_output


class ProtectedJobResultConfigurationOutput(TypedDict):
    output_configuration: "aws_sdk_cleanrooms.types.protected_job_output_configuration_output.ProtectedJobOutputConfigurationOutput"
    """<p>The output configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProtectedJobResultConfigurationOutput) -> dict:
    out: dict = {}
    import aws_sdk_cleanrooms.types.protected_job_output_configuration_output

    out["outputConfiguration"] = (
        aws_sdk_cleanrooms.types.protected_job_output_configuration_output.serialize_json(
            value["output_configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> ProtectedJobResultConfigurationOutput:
    out: ProtectedJobResultConfigurationOutput = {}  # type: ignore[typeddict-item]
    if "outputConfiguration" in data:
        import aws_sdk_cleanrooms.types.protected_job_output_configuration_output

        out["output_configuration"] = (
            aws_sdk_cleanrooms.types.protected_job_output_configuration_output.deserialize_json(
                data["outputConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "ProtectedJobResultConfigurationOutput.output_configuration required"
        )
    return out
