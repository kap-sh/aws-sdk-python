"""Generated from Smithy shape ``com.amazonaws.appconfig#Extensions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appconfig.types.extension_summaries
    import aws_sdk_appconfig.types.next_token


class Extensions(TypedDict):
    items: NotRequired["aws_sdk_appconfig.types.extension_summaries.ExtensionSummaries"]
    """<p>The list of available extensions. The list includes Amazon Web Services authored and user-created extensions.</p>"""
    next_token: NotRequired["aws_sdk_appconfig.types.next_token.NextToken"]
    """<p>The token for the next set of items to return. Use this token to get the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Extensions) -> dict:
    out: dict = {}
    if "items" in value:
        import aws_sdk_appconfig.types.extension_summaries

        out["Items"] = aws_sdk_appconfig.types.extension_summaries.serialize_json(
            value["items"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> Extensions:
    out: Extensions = {}  # type: ignore[typeddict-item]
    if "Items" in data:
        import aws_sdk_appconfig.types.extension_summaries

        out["items"] = aws_sdk_appconfig.types.extension_summaries.deserialize_json(
            data["Items"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
