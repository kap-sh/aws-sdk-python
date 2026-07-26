"""Generated from Smithy shape ``com.amazonaws.ssmquicksetup#ListConfigurationsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm_quicksetup.types.filters_list


class ListConfigurationsInput(TypedDict, closed=True):
    starting_token: NotRequired["str"]
    """<p>The token to use when requesting a specific set of items from a list.</p>"""
    max_items: NotRequired["int"]
    """<p>Specifies the maximum number of configurations that are returned by the request.</p>"""
    filters: NotRequired["capo_ssm_quicksetup.types.filters_list.FiltersList"]
    """<p>Filters the results returned by the request.</p>"""
    manager_arn: NotRequired["str"]
    """<p>The ARN of the configuration manager.</p>"""
    configuration_definition_id: NotRequired["str"]
    """<p>The ID of the configuration definition.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListConfigurationsInput) -> dict:
    out: dict = {}
    if "starting_token" in value:
        out["StartingToken"] = value["starting_token"]
    if "max_items" in value:
        out["MaxItems"] = value["max_items"]
    if "filters" in value:
        import capo_ssm_quicksetup.types.filters_list

        out["Filters"] = capo_ssm_quicksetup.types.filters_list.serialize_json(
            value["filters"]
        )
    if "manager_arn" in value:
        out["ManagerArn"] = value["manager_arn"]
    if "configuration_definition_id" in value:
        out["ConfigurationDefinitionId"] = value["configuration_definition_id"]
    return out


def deserialize_json(data: dict) -> ListConfigurationsInput:
    out: ListConfigurationsInput = {}  # type: ignore[typeddict-item]
    if "StartingToken" in data:
        out["starting_token"] = data["StartingToken"]
    if "MaxItems" in data:
        out["max_items"] = data["MaxItems"]
    if "Filters" in data:
        import capo_ssm_quicksetup.types.filters_list

        out["filters"] = capo_ssm_quicksetup.types.filters_list.deserialize_json(
            data["Filters"]
        )
    if "ManagerArn" in data:
        out["manager_arn"] = data["ManagerArn"]
    if "ConfigurationDefinitionId" in data:
        out["configuration_definition_id"] = data["ConfigurationDefinitionId"]
    return out
