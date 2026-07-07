"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ListFailureModeFindingsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_resiliencehubv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_resiliencehubv2.types.findings_list
    import aws_sdk_resiliencehubv2.types.next_token


class ListFailureModeFindingsResponse(TypedDict, closed=True):
    findings_summary: "aws_sdk_resiliencehubv2.types.findings_list.FindingsList"
    """<p>The list of finding summaries.</p>"""
    next_token: NotRequired["aws_sdk_resiliencehubv2.types.next_token.NextToken"]


# --- restJson1 ser/de ---
def serialize_json(value: ListFailureModeFindingsResponse) -> dict:
    out: dict = {}
    import aws_sdk_resiliencehubv2.types.findings_list

    out["findingsSummary"] = aws_sdk_resiliencehubv2.types.findings_list.serialize_json(
        value["findings_summary"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListFailureModeFindingsResponse:
    out: ListFailureModeFindingsResponse = {}  # type: ignore[typeddict-item]
    if "findingsSummary" in data:
        import aws_sdk_resiliencehubv2.types.findings_list

        out["findings_summary"] = (
            aws_sdk_resiliencehubv2.types.findings_list.deserialize_json(
                data["findingsSummary"]
            )
        )
    else:
        raise DeserializationError(
            "ListFailureModeFindingsResponse.findings_summary required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
