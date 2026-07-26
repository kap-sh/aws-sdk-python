"""Generated from Smithy shape ``com.amazonaws.ssmsap#ListConfigurationCheckOperationsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ssm_sap.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ssm_sap.types.application_id
    import capo_ssm_sap.types.configuration_check_operation_listing_mode
    import capo_ssm_sap.types.filter_list
    import capo_ssm_sap.types.max_results
    import capo_ssm_sap.types.next_token


class ListConfigurationCheckOperationsInput(TypedDict, closed=True):
    application_id: "capo_ssm_sap.types.application_id.ApplicationId"
    """<p>The ID of the application.</p>"""
    list_mode: "capo_ssm_sap.types.configuration_check_operation_listing_mode.ConfigurationCheckOperationListingMode"
    r"""<p>The mode for listing configuration check operations. Defaults to \"LATEST_PER_CHECK\".</p> <ul> <li> <p>LATEST_PER_CHECK - Will list the latest configuration check operation per check type.</p> </li> <li> <p>ALL_OPERATIONS - Will list all configuration check operations performed on the application.</p> </li> </ul>"""
    max_results: NotRequired["capo_ssm_sap.types.max_results.MaxResults"]
    """<p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned nextToken value.</p>"""
    next_token: NotRequired["capo_ssm_sap.types.next_token.NextToken"]
    """<p>The token for the next page of results.</p>"""
    filters: NotRequired["capo_ssm_sap.types.filter_list.FilterList"]
    """<p>The filters of an operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListConfigurationCheckOperationsInput) -> dict:
    out: dict = {}
    out["ApplicationId"] = value["application_id"]
    import capo_ssm_sap.types.configuration_check_operation_listing_mode

    out["ListMode"] = (
        capo_ssm_sap.types.configuration_check_operation_listing_mode.serialize_json(
            value.get("list_mode", "LATEST_PER_CHECK")
        )
    )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "filters" in value:
        import capo_ssm_sap.types.filter_list

        out["Filters"] = capo_ssm_sap.types.filter_list.serialize_json(value["filters"])
    return out


def deserialize_json(data: dict) -> ListConfigurationCheckOperationsInput:
    out: ListConfigurationCheckOperationsInput = {}  # type: ignore[typeddict-item]
    if "ApplicationId" in data:
        out["application_id"] = data["ApplicationId"]
    else:
        raise DeserializationError(
            "ListConfigurationCheckOperationsInput.application_id required"
        )
    if "ListMode" in data:
        import capo_ssm_sap.types.configuration_check_operation_listing_mode

        out["list_mode"] = (
            capo_ssm_sap.types.configuration_check_operation_listing_mode.deserialize_json(
                data["ListMode"]
            )
        )
    else:
        out["list_mode"] = "LATEST_PER_CHECK"
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "Filters" in data:
        import capo_ssm_sap.types.filter_list

        out["filters"] = capo_ssm_sap.types.filter_list.deserialize_json(
            data["Filters"]
        )
    return out
