"""Generated from Smithy shape ``com.amazonaws.artifact#ListReportVersionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_artifact.errors import DeserializationError

if TYPE_CHECKING:
    import capo_artifact.types.next_token_attribute
    import capo_artifact.types.reports_list


class ListReportVersionsResponse(TypedDict, closed=True):
    reports: "capo_artifact.types.reports_list.ReportsList"
    """<p>List of report resources.</p>"""
    next_token: NotRequired[
        "capo_artifact.types.next_token_attribute.NextTokenAttribute"
    ]
    """<p>Pagination token to request the next page of resources.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListReportVersionsResponse) -> dict:
    out: dict = {}
    import capo_artifact.types.reports_list

    out["reports"] = capo_artifact.types.reports_list.serialize_json(value["reports"])
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListReportVersionsResponse:
    out: ListReportVersionsResponse = {}  # type: ignore[typeddict-item]
    if "reports" in data:
        import capo_artifact.types.reports_list

        out["reports"] = capo_artifact.types.reports_list.deserialize_json(
            data["reports"]
        )
    else:
        raise DeserializationError("ListReportVersionsResponse.reports required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
