"""Generated from Smithy shape ``com.amazonaws.iot#ListAuditSuppressionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.audit_suppression_list
    import capo_iot.types.next_token


class ListAuditSuppressionsResponse(TypedDict, closed=True):
    suppressions: NotRequired[
        "capo_iot.types.audit_suppression_list.AuditSuppressionList"
    ]
    """<p> List of audit suppressions. </p>"""
    next_token: NotRequired["capo_iot.types.next_token.NextToken"]
    """<p> A token that can be used to retrieve the next set of results, or <code>null</code> if there are no additional results. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAuditSuppressionsResponse) -> dict:
    out: dict = {}
    if "suppressions" in value:
        import capo_iot.types.audit_suppression_list

        out["suppressions"] = capo_iot.types.audit_suppression_list.serialize_json(
            value["suppressions"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAuditSuppressionsResponse:
    out: ListAuditSuppressionsResponse = {}  # type: ignore[typeddict-item]
    if "suppressions" in data:
        import capo_iot.types.audit_suppression_list

        out["suppressions"] = capo_iot.types.audit_suppression_list.deserialize_json(
            data["suppressions"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
