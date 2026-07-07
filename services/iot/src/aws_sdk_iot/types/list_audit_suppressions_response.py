"""Generated from Smithy shape ``com.amazonaws.iot#ListAuditSuppressionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.audit_suppression_list
    import aws_sdk_iot.types.next_token


class ListAuditSuppressionsResponse(TypedDict, closed=True):
    suppressions: NotRequired[
        "aws_sdk_iot.types.audit_suppression_list.AuditSuppressionList"
    ]
    """<p> List of audit suppressions. </p>"""
    next_token: NotRequired["aws_sdk_iot.types.next_token.NextToken"]
    """<p> A token that can be used to retrieve the next set of results, or <code>null</code> if there are no additional results. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAuditSuppressionsResponse) -> dict:
    out: dict = {}
    if "suppressions" in value:
        import aws_sdk_iot.types.audit_suppression_list

        out["suppressions"] = aws_sdk_iot.types.audit_suppression_list.serialize_json(
            value["suppressions"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAuditSuppressionsResponse:
    out: ListAuditSuppressionsResponse = {}  # type: ignore[typeddict-item]
    if "suppressions" in data:
        import aws_sdk_iot.types.audit_suppression_list

        out["suppressions"] = aws_sdk_iot.types.audit_suppression_list.deserialize_json(
            data["suppressions"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
