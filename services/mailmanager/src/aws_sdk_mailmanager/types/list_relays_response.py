"""Generated from Smithy shape ``com.amazonaws.mailmanager#ListRelaysResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_mailmanager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mailmanager.types.pagination_token
    import aws_sdk_mailmanager.types.relays


class ListRelaysResponse(TypedDict, closed=True):
    relays: "aws_sdk_mailmanager.types.relays.Relays"
    """<p>The list of returned relays.</p>"""
    next_token: NotRequired[
        "aws_sdk_mailmanager.types.pagination_token.PaginationToken"
    ]
    """<p>If NextToken is returned, there are more results available. The value of NextToken is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListRelaysResponse) -> dict:
    out: dict = {}
    import aws_sdk_mailmanager.types.relays

    out["Relays"] = aws_sdk_mailmanager.types.relays.serialize_aws_json_1_0(
        value["relays"]
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListRelaysResponse:
    out: ListRelaysResponse = {}  # type: ignore[typeddict-item]
    if "Relays" in data:
        import aws_sdk_mailmanager.types.relays

        out["relays"] = aws_sdk_mailmanager.types.relays.deserialize_aws_json_1_0(
            data["Relays"]
        )
    else:
        raise DeserializationError("ListRelaysResponse.relays required")
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
