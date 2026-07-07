"""Generated from Smithy shape ``com.amazonaws.artifact#ListReportsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_artifact.types.next_token_attribute
    import aws_sdk_artifact.types.reports_list


class ListReportsResponse(TypedDict, closed=True):
    reports: NotRequired["aws_sdk_artifact.types.reports_list.ReportsList"]
    """<p>List of report resources.</p>"""
    next_token: NotRequired[
        "aws_sdk_artifact.types.next_token_attribute.NextTokenAttribute"
    ]
    """<p>Pagination token to request the next page of resources.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListReportsResponse) -> dict:
    out: dict = {}
    if "reports" in value:
        import aws_sdk_artifact.types.reports_list

        out["reports"] = aws_sdk_artifact.types.reports_list.serialize_json(
            value["reports"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListReportsResponse:
    out: ListReportsResponse = {}  # type: ignore[typeddict-item]
    if "reports" in data:
        import aws_sdk_artifact.types.reports_list

        out["reports"] = aws_sdk_artifact.types.reports_list.deserialize_json(
            data["reports"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
