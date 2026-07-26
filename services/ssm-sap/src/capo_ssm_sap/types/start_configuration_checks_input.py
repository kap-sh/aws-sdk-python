"""Generated from Smithy shape ``com.amazonaws.ssmsap#StartConfigurationChecksInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ssm_sap.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ssm_sap.types.application_id
    import capo_ssm_sap.types.configuration_check_type_list


class StartConfigurationChecksInput(TypedDict, closed=True):
    application_id: "capo_ssm_sap.types.application_id.ApplicationId"
    """<p>The ID of the application.</p>"""
    configuration_check_ids: NotRequired[
        "capo_ssm_sap.types.configuration_check_type_list.ConfigurationCheckTypeList"
    ]
    """<p>The list of configuration checks to perform.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartConfigurationChecksInput) -> dict:
    out: dict = {}
    out["ApplicationId"] = value["application_id"]
    if "configuration_check_ids" in value:
        import capo_ssm_sap.types.configuration_check_type_list

        out["ConfigurationCheckIds"] = (
            capo_ssm_sap.types.configuration_check_type_list.serialize_json(
                value["configuration_check_ids"]
            )
        )
    return out


def deserialize_json(data: dict) -> StartConfigurationChecksInput:
    out: StartConfigurationChecksInput = {}  # type: ignore[typeddict-item]
    if "ApplicationId" in data:
        out["application_id"] = data["ApplicationId"]
    else:
        raise DeserializationError(
            "StartConfigurationChecksInput.application_id required"
        )
    if "ConfigurationCheckIds" in data:
        import capo_ssm_sap.types.configuration_check_type_list

        out["configuration_check_ids"] = (
            capo_ssm_sap.types.configuration_check_type_list.deserialize_json(
                data["ConfigurationCheckIds"]
            )
        )
    return out
