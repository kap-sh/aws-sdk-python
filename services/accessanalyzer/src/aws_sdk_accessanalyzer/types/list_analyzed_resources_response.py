"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#ListAnalyzedResourcesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_accessanalyzer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_accessanalyzer.types.analyzed_resources_list
    import aws_sdk_accessanalyzer.types.token


class ListAnalyzedResourcesResponse(TypedDict, closed=True):
    analyzed_resources: (
        "aws_sdk_accessanalyzer.types.analyzed_resources_list.AnalyzedResourcesList"
    )
    """<p>A list of resources that were analyzed.</p>"""
    next_token: NotRequired["aws_sdk_accessanalyzer.types.token.Token"]
    """<p>A token used for pagination of results returned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAnalyzedResourcesResponse) -> dict:
    out: dict = {}
    import aws_sdk_accessanalyzer.types.analyzed_resources_list

    out["analyzedResources"] = (
        aws_sdk_accessanalyzer.types.analyzed_resources_list.serialize_json(
            value["analyzed_resources"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAnalyzedResourcesResponse:
    out: ListAnalyzedResourcesResponse = {}  # type: ignore[typeddict-item]
    if "analyzedResources" in data:
        import aws_sdk_accessanalyzer.types.analyzed_resources_list

        out["analyzed_resources"] = (
            aws_sdk_accessanalyzer.types.analyzed_resources_list.deserialize_json(
                data["analyzedResources"]
            )
        )
    else:
        raise DeserializationError(
            "ListAnalyzedResourcesResponse.analyzed_resources required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
