"""Generated from Smithy shape ``com.amazonaws.ssmsap#ListConfigurationCheckDefinitionsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm_sap.types.configuration_check_definition_list
    import capo_ssm_sap.types.next_token


class ListConfigurationCheckDefinitionsOutput(TypedDict, closed=True):
    configuration_checks: NotRequired[
        "capo_ssm_sap.types.configuration_check_definition_list.ConfigurationCheckDefinitionList"
    ]
    """<p>The configuration check types supported by AWS Systems Manager for SAP.</p>"""
    next_token: NotRequired["capo_ssm_sap.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results. This value is null when there are no more results to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListConfigurationCheckDefinitionsOutput) -> dict:
    out: dict = {}
    if "configuration_checks" in value:
        import capo_ssm_sap.types.configuration_check_definition_list

        out["ConfigurationChecks"] = (
            capo_ssm_sap.types.configuration_check_definition_list.serialize_json(
                value["configuration_checks"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListConfigurationCheckDefinitionsOutput:
    out: ListConfigurationCheckDefinitionsOutput = {}  # type: ignore[typeddict-item]
    if "ConfigurationChecks" in data:
        import capo_ssm_sap.types.configuration_check_definition_list

        out["configuration_checks"] = (
            capo_ssm_sap.types.configuration_check_definition_list.deserialize_json(
                data["ConfigurationChecks"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
