"""Generated from Smithy shape ``com.amazonaws.inspector2#ListCodeSecurityScanConfigurationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.code_security_scan_configuration_summaries
    import capo_inspector2.types.next_token


class ListCodeSecurityScanConfigurationsResponse(TypedDict, closed=True):
    configurations: NotRequired[
        "capo_inspector2.types.code_security_scan_configuration_summaries.CodeSecurityScanConfigurationSummaries"
    ]
    """<p>A list of code security scan configuration summaries.</p>"""
    next_token: NotRequired["capo_inspector2.types.next_token.NextToken"]
    """<p>A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request. For subsequent calls, use the NextToken value returned from the previous request to continue listing results after the first page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCodeSecurityScanConfigurationsResponse) -> dict:
    out: dict = {}
    if "configurations" in value:
        import capo_inspector2.types.code_security_scan_configuration_summaries

        out["configurations"] = (
            capo_inspector2.types.code_security_scan_configuration_summaries.serialize_json(
                value["configurations"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListCodeSecurityScanConfigurationsResponse:
    out: ListCodeSecurityScanConfigurationsResponse = {}  # type: ignore[typeddict-item]
    if "configurations" in data:
        import capo_inspector2.types.code_security_scan_configuration_summaries

        out["configurations"] = (
            capo_inspector2.types.code_security_scan_configuration_summaries.deserialize_json(
                data["configurations"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
