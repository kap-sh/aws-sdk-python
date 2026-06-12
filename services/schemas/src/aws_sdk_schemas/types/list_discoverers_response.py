"""Generated from Smithy shape ``com.amazonaws.schemas#ListDiscoverersResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_schemas.types.__list_of_discoverer_summary
    import aws_sdk_schemas.types.__string


class ListDiscoverersResponse(TypedDict):
    discoverers: NotRequired[
        "aws_sdk_schemas.types.__list_of_discoverer_summary.__listOfDiscovererSummary"
    ]
    """<p>An array of DiscovererSummary information.</p>"""
    next_token: NotRequired["aws_sdk_schemas.types.__string.__string"]
    """<p>The token that specifies the next page of results to return. To request the first page, leave NextToken empty. The token will expire in 24 hours, and cannot be shared with other accounts.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDiscoverersResponse) -> dict:
    out: dict = {}
    if "discoverers" in value:
        import aws_sdk_schemas.types.__list_of_discoverer_summary

        out["Discoverers"] = (
            aws_sdk_schemas.types.__list_of_discoverer_summary.serialize_json(
                value["discoverers"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDiscoverersResponse:
    out: ListDiscoverersResponse = {}  # type: ignore[typeddict-item]
    if "Discoverers" in data:
        import aws_sdk_schemas.types.__list_of_discoverer_summary

        out["discoverers"] = (
            aws_sdk_schemas.types.__list_of_discoverer_summary.deserialize_json(
                data["Discoverers"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
