"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ListAssertionsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_resiliencehubv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_resiliencehubv2.types.assertion_list
    import aws_sdk_resiliencehubv2.types.next_token


class ListAssertionsResponse(TypedDict):
    assertions: "aws_sdk_resiliencehubv2.types.assertion_list.AssertionList"
    """<p>The list of assertions.</p>"""
    next_token: NotRequired["aws_sdk_resiliencehubv2.types.next_token.NextToken"]


# --- restJson1 ser/de ---
def serialize_json(value: ListAssertionsResponse) -> dict:
    out: dict = {}
    import aws_sdk_resiliencehubv2.types.assertion_list

    out["assertions"] = aws_sdk_resiliencehubv2.types.assertion_list.serialize_json(
        value["assertions"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAssertionsResponse:
    out: ListAssertionsResponse = {}  # type: ignore[typeddict-item]
    if "assertions" in data:
        import aws_sdk_resiliencehubv2.types.assertion_list

        out["assertions"] = (
            aws_sdk_resiliencehubv2.types.assertion_list.deserialize_json(
                data["assertions"]
            )
        )
    else:
        raise DeserializationError("ListAssertionsResponse.assertions required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
