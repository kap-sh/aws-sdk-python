"""Generated from Smithy shape ``com.amazonaws.iot#ListActiveViolationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.active_violations
    import aws_sdk_iot.types.next_token


class ListActiveViolationsResponse(TypedDict, closed=True):
    active_violations: NotRequired[
        "aws_sdk_iot.types.active_violations.ActiveViolations"
    ]
    """<p>The list of active violations.</p>"""
    next_token: NotRequired["aws_sdk_iot.types.next_token.NextToken"]
    """<p>A token that can be used to retrieve the next set of results, or <code>null</code> if there are no additional results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListActiveViolationsResponse) -> dict:
    out: dict = {}
    if "active_violations" in value:
        import aws_sdk_iot.types.active_violations

        out["activeViolations"] = aws_sdk_iot.types.active_violations.serialize_json(
            value["active_violations"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListActiveViolationsResponse:
    out: ListActiveViolationsResponse = {}  # type: ignore[typeddict-item]
    if "activeViolations" in data:
        import aws_sdk_iot.types.active_violations

        out["active_violations"] = aws_sdk_iot.types.active_violations.deserialize_json(
            data["activeViolations"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
