"""Generated from Smithy shape ``com.amazonaws.appconfig#ExtensionAssociations``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_appconfig.types.extension_association_summaries
    import aws_sdk_appconfig.types.next_token


class ExtensionAssociations(TypedDict, closed=True):
    items: NotRequired[
        "aws_sdk_appconfig.types.extension_association_summaries.ExtensionAssociationSummaries"
    ]
    """<p>The list of extension associations. Each item represents an extension association to an application, environment, or configuration profile. </p>"""
    next_token: NotRequired["aws_sdk_appconfig.types.next_token.NextToken"]
    """<p>The token for the next set of items to return. Use this token to get the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExtensionAssociations) -> dict:
    out: dict = {}
    if "items" in value:
        import aws_sdk_appconfig.types.extension_association_summaries

        out["Items"] = (
            aws_sdk_appconfig.types.extension_association_summaries.serialize_json(
                value["items"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ExtensionAssociations:
    out: ExtensionAssociations = {}  # type: ignore[typeddict-item]
    if "Items" in data:
        import aws_sdk_appconfig.types.extension_association_summaries

        out["items"] = (
            aws_sdk_appconfig.types.extension_association_summaries.deserialize_json(
                data["Items"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
