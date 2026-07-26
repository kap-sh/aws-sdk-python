"""Generated from Smithy shape ``com.amazonaws.ssmsap#GetConfigurationCheckOperationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm_sap.types.configuration_check_operation


class GetConfigurationCheckOperationOutput(TypedDict, closed=True):
    configuration_check_operation: NotRequired[
        "capo_ssm_sap.types.configuration_check_operation.ConfigurationCheckOperation"
    ]
    """<p>Returns the details of a configuration check operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetConfigurationCheckOperationOutput) -> dict:
    out: dict = {}
    if "configuration_check_operation" in value:
        import capo_ssm_sap.types.configuration_check_operation

        out["ConfigurationCheckOperation"] = (
            capo_ssm_sap.types.configuration_check_operation.serialize_json(
                value["configuration_check_operation"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetConfigurationCheckOperationOutput:
    out: GetConfigurationCheckOperationOutput = {}  # type: ignore[typeddict-item]
    if "ConfigurationCheckOperation" in data:
        import capo_ssm_sap.types.configuration_check_operation

        out["configuration_check_operation"] = (
            capo_ssm_sap.types.configuration_check_operation.deserialize_json(
                data["ConfigurationCheckOperation"]
            )
        )
    return out
