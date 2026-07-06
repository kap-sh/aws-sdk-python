"""Generated from Smithy shape ``com.amazonaws.inspector2#ListCisScansResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.cis_scan_list
    import aws_sdk_inspector2.types.next_token


class ListCisScansResponse(TypedDict, closed=True):
    scans: NotRequired["aws_sdk_inspector2.types.cis_scan_list.CisScanList"]
    """<p>The CIS scans.</p>"""
    next_token: NotRequired["aws_sdk_inspector2.types.next_token.NextToken"]
    """<p>The pagination token from a previous request that's used to retrieve the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCisScansResponse) -> dict:
    out: dict = {}
    if "scans" in value:
        import aws_sdk_inspector2.types.cis_scan_list

        out["scans"] = aws_sdk_inspector2.types.cis_scan_list.serialize_json(
            value["scans"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListCisScansResponse:
    out: ListCisScansResponse = {}  # type: ignore[typeddict-item]
    if "scans" in data:
        import aws_sdk_inspector2.types.cis_scan_list

        out["scans"] = aws_sdk_inspector2.types.cis_scan_list.deserialize_json(
            data["scans"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
