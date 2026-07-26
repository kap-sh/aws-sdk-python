"""Generated from Smithy shape ``com.amazonaws.inspector2#ListCisScanConfigurationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.cis_scan_configuration_list
    import capo_inspector2.types.next_token


class ListCisScanConfigurationsResponse(TypedDict, closed=True):
    scan_configurations: NotRequired[
        "capo_inspector2.types.cis_scan_configuration_list.CisScanConfigurationList"
    ]
    """<p>The CIS scan configuration scan configurations.</p>"""
    next_token: NotRequired["capo_inspector2.types.next_token.NextToken"]
    """<p>The pagination token from a previous request that's used to retrieve the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCisScanConfigurationsResponse) -> dict:
    out: dict = {}
    if "scan_configurations" in value:
        import capo_inspector2.types.cis_scan_configuration_list

        out["scanConfigurations"] = (
            capo_inspector2.types.cis_scan_configuration_list.serialize_json(
                value["scan_configurations"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListCisScanConfigurationsResponse:
    out: ListCisScanConfigurationsResponse = {}  # type: ignore[typeddict-item]
    if "scanConfigurations" in data:
        import capo_inspector2.types.cis_scan_configuration_list

        out["scan_configurations"] = (
            capo_inspector2.types.cis_scan_configuration_list.deserialize_json(
                data["scanConfigurations"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
