"""Generated from Smithy shape ``com.amazonaws.iot#ListThingPrincipalsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.next_token
    import aws_sdk_iot.types.principals


class ListThingPrincipalsResponse(TypedDict, closed=True):
    principals: NotRequired["aws_sdk_iot.types.principals.Principals"]
    """<p>The principals associated with the thing.</p>"""
    next_token: NotRequired["aws_sdk_iot.types.next_token.NextToken"]
    """<p>The token to use to get the next set of results, or <b>null</b> if there are no additional results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListThingPrincipalsResponse) -> dict:
    out: dict = {}
    if "principals" in value:
        import aws_sdk_iot.types.principals

        out["principals"] = aws_sdk_iot.types.principals.serialize_json(
            value["principals"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListThingPrincipalsResponse:
    out: ListThingPrincipalsResponse = {}  # type: ignore[typeddict-item]
    if "principals" in data:
        import aws_sdk_iot.types.principals

        out["principals"] = aws_sdk_iot.types.principals.deserialize_json(
            data["principals"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
