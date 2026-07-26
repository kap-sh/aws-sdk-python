"""Generated from Smithy shape ``com.amazonaws.ssmsap#ListConfigurationCheckOperationsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm_sap.types.configuration_check_operation_list
    import capo_ssm_sap.types.next_token


class ListConfigurationCheckOperationsOutput(TypedDict, closed=True):
    configuration_check_operations: NotRequired[
        "capo_ssm_sap.types.configuration_check_operation_list.ConfigurationCheckOperationList"
    ]
    """<p>The configuration check operations performed by AWS Systems Manager for SAP.</p>"""
    next_token: NotRequired["capo_ssm_sap.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results. This value is null when there are no more results to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListConfigurationCheckOperationsOutput) -> dict:
    out: dict = {}
    if "configuration_check_operations" in value:
        import capo_ssm_sap.types.configuration_check_operation_list

        out["ConfigurationCheckOperations"] = (
            capo_ssm_sap.types.configuration_check_operation_list.serialize_json(
                value["configuration_check_operations"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListConfigurationCheckOperationsOutput:
    out: ListConfigurationCheckOperationsOutput = {}  # type: ignore[typeddict-item]
    if "ConfigurationCheckOperations" in data:
        import capo_ssm_sap.types.configuration_check_operation_list

        out["configuration_check_operations"] = (
            capo_ssm_sap.types.configuration_check_operation_list.deserialize_json(
                data["ConfigurationCheckOperations"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
