"""Generated from Smithy shape ``com.amazonaws.ssmsap#StartConfigurationChecksOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm_sap.types.configuration_check_operation_list


class StartConfigurationChecksOutput(TypedDict, closed=True):
    configuration_check_operations: NotRequired[
        "capo_ssm_sap.types.configuration_check_operation_list.ConfigurationCheckOperationList"
    ]
    """<p>The configuration check operations that were started.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartConfigurationChecksOutput) -> dict:
    out: dict = {}
    if "configuration_check_operations" in value:
        import capo_ssm_sap.types.configuration_check_operation_list

        out["ConfigurationCheckOperations"] = (
            capo_ssm_sap.types.configuration_check_operation_list.serialize_json(
                value["configuration_check_operations"]
            )
        )
    return out


def deserialize_json(data: dict) -> StartConfigurationChecksOutput:
    out: StartConfigurationChecksOutput = {}  # type: ignore[typeddict-item]
    if "ConfigurationCheckOperations" in data:
        import capo_ssm_sap.types.configuration_check_operation_list

        out["configuration_check_operations"] = (
            capo_ssm_sap.types.configuration_check_operation_list.deserialize_json(
                data["ConfigurationCheckOperations"]
            )
        )
    return out
