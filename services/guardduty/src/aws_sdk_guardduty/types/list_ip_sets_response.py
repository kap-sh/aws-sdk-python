"""Generated from Smithy shape ``com.amazonaws.guardduty#ListIPSetsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.ip_set_ids
    import aws_sdk_guardduty.types.string


class ListIPSetsResponse(TypedDict):
    ip_set_ids: NotRequired["aws_sdk_guardduty.types.ip_set_ids.IpSetIds"]
    """<p>The IDs of the IPSet resources.</p>"""
    next_token: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The pagination parameter to be used on the next list operation to retrieve more items.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListIPSetsResponse) -> dict:
    out: dict = {}
    if "ip_set_ids" in value:
        import aws_sdk_guardduty.types.ip_set_ids

        out["ipSetIds"] = aws_sdk_guardduty.types.ip_set_ids.serialize_json(
            value["ip_set_ids"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListIPSetsResponse:
    out: ListIPSetsResponse = {}  # type: ignore[typeddict-item]
    if "ipSetIds" in data:
        import aws_sdk_guardduty.types.ip_set_ids

        out["ip_set_ids"] = aws_sdk_guardduty.types.ip_set_ids.deserialize_json(
            data["ipSetIds"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
