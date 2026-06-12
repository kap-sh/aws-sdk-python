"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ListDomainLayoutsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.layout_list
    import aws_sdk_customer_profiles.types.token


class ListDomainLayoutsResponse(TypedDict):
    items: NotRequired["aws_sdk_customer_profiles.types.layout_list.LayoutList"]
    """<p>Contains summary information about an EventStream.</p>"""
    next_token: NotRequired["aws_sdk_customer_profiles.types.token.token"]
    """<p>Identifies the next page of results to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDomainLayoutsResponse) -> dict:
    out: dict = {}
    if "items" in value:
        import aws_sdk_customer_profiles.types.layout_list

        out["Items"] = aws_sdk_customer_profiles.types.layout_list.serialize_json(
            value["items"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDomainLayoutsResponse:
    out: ListDomainLayoutsResponse = {}  # type: ignore[typeddict-item]
    if "Items" in data:
        import aws_sdk_customer_profiles.types.layout_list

        out["items"] = aws_sdk_customer_profiles.types.layout_list.deserialize_json(
            data["Items"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
