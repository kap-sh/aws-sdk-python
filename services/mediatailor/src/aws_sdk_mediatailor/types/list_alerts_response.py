"""Generated from Smithy shape ``com.amazonaws.mediatailor#ListAlertsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediatailor.types.__list_of_alert
    import aws_sdk_mediatailor.types.__string


class ListAlertsResponse(TypedDict, closed=True):
    items: NotRequired["aws_sdk_mediatailor.types.__list_of_alert.__listOfAlert"]
    """<p>A list of alerts that are associated with this resource.</p>"""
    next_token: NotRequired["aws_sdk_mediatailor.types.__string.__string"]
    """<p>Pagination token returned by the list request when results exceed the maximum allowed. Use the token to fetch the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAlertsResponse) -> dict:
    out: dict = {}
    if "items" in value:
        import aws_sdk_mediatailor.types.__list_of_alert

        out["Items"] = aws_sdk_mediatailor.types.__list_of_alert.serialize_json(
            value["items"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAlertsResponse:
    out: ListAlertsResponse = {}  # type: ignore[typeddict-item]
    if "Items" in data:
        import aws_sdk_mediatailor.types.__list_of_alert

        out["items"] = aws_sdk_mediatailor.types.__list_of_alert.deserialize_json(
            data["Items"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
