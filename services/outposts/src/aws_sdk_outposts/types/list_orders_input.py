"""Generated from Smithy shape ``com.amazonaws.outposts#ListOrdersInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_outposts.types.max_results1000
    import aws_sdk_outposts.types.outpost_identifier
    import aws_sdk_outposts.types.token


class ListOrdersInput(TypedDict):
    outpost_identifier_filter: NotRequired[
        "aws_sdk_outposts.types.outpost_identifier.OutpostIdentifier"
    ]
    """<p> The ID or the Amazon Resource Name (ARN) of the Outpost. </p>"""
    next_token: NotRequired["aws_sdk_outposts.types.token.Token"]
    max_results: NotRequired["aws_sdk_outposts.types.max_results1000.MaxResults1000"]


# --- restJson1 ser/de ---
def serialize_json(value: ListOrdersInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListOrdersInput:
    out: ListOrdersInput = {}  # type: ignore[typeddict-item]
    return out
