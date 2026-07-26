"""Generated from Smithy shape ``com.amazonaws.securityhub#GetFindingsV2Response``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.next_token
    import capo_securityhub.types.ocsf_findings_list


class GetFindingsV2Response(TypedDict, closed=True):
    findings: NotRequired["capo_securityhub.types.ocsf_findings_list.OcsfFindingsList"]
    """<p>An array of security findings returned by the operation.</p>"""
    next_token: NotRequired["capo_securityhub.types.next_token.NextToken"]
    """<p>The pagination token to use to request the next page of results. Otherwise, this parameter is null.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetFindingsV2Response) -> dict:
    out: dict = {}
    if "findings" in value:
        import capo_securityhub.types.ocsf_findings_list

        out["Findings"] = capo_securityhub.types.ocsf_findings_list.serialize_json(
            value["findings"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetFindingsV2Response:
    out: GetFindingsV2Response = {}  # type: ignore[typeddict-item]
    if "Findings" in data:
        import capo_securityhub.types.ocsf_findings_list

        out["findings"] = capo_securityhub.types.ocsf_findings_list.deserialize_json(
            data["Findings"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
