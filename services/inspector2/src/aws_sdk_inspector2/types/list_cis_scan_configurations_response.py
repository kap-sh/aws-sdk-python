"""Generated from Smithy shape ``com.amazonaws.inspector2#ListCisScanConfigurationsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.cis_scan_configuration_list
    import aws_sdk_inspector2.types.next_token


class ListCisScanConfigurationsResponse(TypedDict):
    scan_configurations: NotRequired[
        "aws_sdk_inspector2.types.cis_scan_configuration_list.CisScanConfigurationList"
    ]
    """<p>The CIS scan configuration scan configurations.</p>"""
    next_token: NotRequired["aws_sdk_inspector2.types.next_token.NextToken"]
    """<p>The pagination token from a previous request that's used to retrieve the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCisScanConfigurationsResponse) -> dict:
    out: dict = {}
    if "scan_configurations" in value:
        import aws_sdk_inspector2.types.cis_scan_configuration_list

        out["scanConfigurations"] = (
            aws_sdk_inspector2.types.cis_scan_configuration_list.serialize_json(
                value["scan_configurations"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListCisScanConfigurationsResponse:
    out: ListCisScanConfigurationsResponse = {}  # type: ignore[typeddict-item]
    if "scanConfigurations" in data:
        import aws_sdk_inspector2.types.cis_scan_configuration_list

        out["scan_configurations"] = (
            aws_sdk_inspector2.types.cis_scan_configuration_list.deserialize_json(
                data["scanConfigurations"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
