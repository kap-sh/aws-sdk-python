"""Generated from Smithy shape ``com.amazonaws.greengrassv2#ListComponentsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_greengrassv2.types.component_list
    import aws_sdk_greengrassv2.types.next_token_string


class ListComponentsResponse(TypedDict):
    components: NotRequired["aws_sdk_greengrassv2.types.component_list.ComponentList"]
    """<p>A list that summarizes each component.</p>"""
    next_token: NotRequired[
        "aws_sdk_greengrassv2.types.next_token_string.NextTokenString"
    ]
    """<p>The token for the next set of results, or null if there are no additional results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListComponentsResponse) -> dict:
    out: dict = {}
    if "components" in value:
        import aws_sdk_greengrassv2.types.component_list

        out["components"] = aws_sdk_greengrassv2.types.component_list.serialize_json(
            value["components"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListComponentsResponse:
    out: ListComponentsResponse = {}  # type: ignore[typeddict-item]
    if "components" in data:
        import aws_sdk_greengrassv2.types.component_list

        out["components"] = aws_sdk_greengrassv2.types.component_list.deserialize_json(
            data["components"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
