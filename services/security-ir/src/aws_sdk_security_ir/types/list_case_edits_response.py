"""Generated from Smithy shape ``com.amazonaws.securityir#ListCaseEditsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_security_ir.types.case_edit_items


class ListCaseEditsResponse(TypedDict, closed=True):
    next_token: NotRequired["str"]
    """<p>An optional string that, if supplied on subsequent calls to ListCaseEdits, allows the API to fetch the next page of results. </p>"""
    items: NotRequired["aws_sdk_security_ir.types.case_edit_items.CaseEditItems"]
    """<p>Response element for ListCaseEdits that includes the action, event timestamp, message, and principal for the response. </p>"""
    total: NotRequired["int"]
    """<p>Response element for ListCaseEdits that identifies the total number of edits.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCaseEditsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "items" in value:
        import aws_sdk_security_ir.types.case_edit_items

        out["items"] = aws_sdk_security_ir.types.case_edit_items.serialize_json(
            value["items"]
        )
    if "total" in value:
        out["total"] = value["total"]
    return out


def deserialize_json(data: dict) -> ListCaseEditsResponse:
    out: ListCaseEditsResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "items" in data:
        import aws_sdk_security_ir.types.case_edit_items

        out["items"] = aws_sdk_security_ir.types.case_edit_items.deserialize_json(
            data["items"]
        )
    if "total" in data:
        out["total"] = data["total"]
    return out
