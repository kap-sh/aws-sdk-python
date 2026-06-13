"""Generated from Smithy shape ``com.amazonaws.backup#ListLegalHoldsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_backup.types.legal_holds_list
    import aws_sdk_backup.types.string


class ListLegalHoldsOutput(TypedDict):
    next_token: NotRequired["aws_sdk_backup.types.string.string"]
    """<p>The next item following a partial list of returned resources. For example, if a request is made to return <code>MaxResults</code> number of resources, <code>NextToken</code> allows you to return more items in your list starting at the location pointed to by the next token.</p>"""
    legal_holds: NotRequired["aws_sdk_backup.types.legal_holds_list.LegalHoldsList"]
    """<p>This is an array of returned legal holds, both active and previous.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListLegalHoldsOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "legal_holds" in value:
        import aws_sdk_backup.types.legal_holds_list

        out["LegalHolds"] = aws_sdk_backup.types.legal_holds_list.serialize_json(
            value["legal_holds"]
        )
    return out


def deserialize_json(data: dict) -> ListLegalHoldsOutput:
    out: ListLegalHoldsOutput = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "LegalHolds" in data:
        import aws_sdk_backup.types.legal_holds_list

        out["legal_holds"] = aws_sdk_backup.types.legal_holds_list.deserialize_json(
            data["LegalHolds"]
        )
    return out
