"""Generated from Smithy shape ``com.amazonaws.inspector2#GetCisScanResultDetailsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.cis_scan_result_details_list
    import capo_inspector2.types.next_token


class GetCisScanResultDetailsResponse(TypedDict, closed=True):
    scan_result_details: NotRequired[
        "capo_inspector2.types.cis_scan_result_details_list.CisScanResultDetailsList"
    ]
    """<p>The scan result details.</p>"""
    next_token: NotRequired["capo_inspector2.types.next_token.NextToken"]
    """<p>The pagination token from a previous request that's used to retrieve the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCisScanResultDetailsResponse) -> dict:
    out: dict = {}
    if "scan_result_details" in value:
        import capo_inspector2.types.cis_scan_result_details_list

        out["scanResultDetails"] = (
            capo_inspector2.types.cis_scan_result_details_list.serialize_json(
                value["scan_result_details"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetCisScanResultDetailsResponse:
    out: GetCisScanResultDetailsResponse = {}  # type: ignore[typeddict-item]
    if "scanResultDetails" in data:
        import capo_inspector2.types.cis_scan_result_details_list

        out["scan_result_details"] = (
            capo_inspector2.types.cis_scan_result_details_list.deserialize_json(
                data["scanResultDetails"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
