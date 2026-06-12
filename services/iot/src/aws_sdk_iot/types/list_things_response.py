"""Generated from Smithy shape ``com.amazonaws.iot#ListThingsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.next_token
    import aws_sdk_iot.types.thing_attribute_list


class ListThingsResponse(TypedDict):
    things: NotRequired["aws_sdk_iot.types.thing_attribute_list.ThingAttributeList"]
    """<p>The things.</p>"""
    next_token: NotRequired["aws_sdk_iot.types.next_token.NextToken"]
    """<p>The token to use to get the next set of results. Will not be returned if operation has returned all results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListThingsResponse) -> dict:
    out: dict = {}
    if "things" in value:
        import aws_sdk_iot.types.thing_attribute_list

        out["things"] = aws_sdk_iot.types.thing_attribute_list.serialize_json(
            value["things"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListThingsResponse:
    out: ListThingsResponse = {}  # type: ignore[typeddict-item]
    if "things" in data:
        import aws_sdk_iot.types.thing_attribute_list

        out["things"] = aws_sdk_iot.types.thing_attribute_list.deserialize_json(
            data["things"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
