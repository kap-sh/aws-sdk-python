"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#SearchChannelsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_chime_sdk_messaging.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_messaging.types.chime_arn
    import aws_sdk_chime_sdk_messaging.types.max_results
    import aws_sdk_chime_sdk_messaging.types.next_token
    import aws_sdk_chime_sdk_messaging.types.search_fields


class SearchChannelsRequest(TypedDict, closed=True):
    chime_bearer: NotRequired["aws_sdk_chime_sdk_messaging.types.chime_arn.ChimeArn"]
    """<p>The <code>AppInstanceUserArn</code> of the user making the API call.</p>"""
    fields: "aws_sdk_chime_sdk_messaging.types.search_fields.SearchFields"
    """<p>A list of the <code>Field</code> objects in the channel being searched.</p>"""
    max_results: NotRequired["aws_sdk_chime_sdk_messaging.types.max_results.MaxResults"]
    """<p>The maximum number of channels that you want returned.</p>"""
    next_token: NotRequired["aws_sdk_chime_sdk_messaging.types.next_token.NextToken"]
    """<p>The token returned from previous API requests until the number of channels is reached.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchChannelsRequest) -> dict:
    out: dict = {}
    import aws_sdk_chime_sdk_messaging.types.search_fields

    out["Fields"] = aws_sdk_chime_sdk_messaging.types.search_fields.serialize_json(
        value["fields"]
    )
    return out


def deserialize_json(data: dict) -> SearchChannelsRequest:
    out: SearchChannelsRequest = {}  # type: ignore[typeddict-item]
    if "Fields" in data:
        import aws_sdk_chime_sdk_messaging.types.search_fields

        out["fields"] = (
            aws_sdk_chime_sdk_messaging.types.search_fields.deserialize_json(
                data["Fields"]
            )
        )
    else:
        raise DeserializationError("SearchChannelsRequest.fields required")
    return out
