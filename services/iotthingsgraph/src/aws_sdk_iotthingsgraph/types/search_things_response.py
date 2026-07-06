"""Generated from Smithy shape ``com.amazonaws.iotthingsgraph#SearchThingsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iotthingsgraph.types.next_token
    import aws_sdk_iotthingsgraph.types.things


class SearchThingsResponse(TypedDict, closed=True):
    things: NotRequired["aws_sdk_iotthingsgraph.types.things.Things"]
    """<p>An array of things in the result set.</p>"""
    next_token: NotRequired["aws_sdk_iotthingsgraph.types.next_token.NextToken"]
    """<p>The string to specify as <code>nextToken</code> when you request the next page of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SearchThingsResponse) -> dict:
    out: dict = {}
    if "things" in value:
        import aws_sdk_iotthingsgraph.types.things

        out["things"] = aws_sdk_iotthingsgraph.types.things.serialize_aws_json_1_1(
            value["things"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SearchThingsResponse:
    out: SearchThingsResponse = {}  # type: ignore[typeddict-item]
    if "things" in data:
        import aws_sdk_iotthingsgraph.types.things

        out["things"] = aws_sdk_iotthingsgraph.types.things.deserialize_aws_json_1_1(
            data["things"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
