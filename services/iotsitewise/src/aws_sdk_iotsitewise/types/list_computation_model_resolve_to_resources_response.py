"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ListComputationModelResolveToResourcesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.computation_model_resolve_to_resource_summaries
    import aws_sdk_iotsitewise.types.next_token


class ListComputationModelResolveToResourcesResponse(TypedDict):
    computation_model_resolve_to_resource_summaries: "aws_sdk_iotsitewise.types.computation_model_resolve_to_resource_summaries.ComputationModelResolveToResourceSummaries"
    """<p>A list of summaries describing the distinct resources that this computation model resolves to when actions were executed.</p>"""
    next_token: NotRequired["aws_sdk_iotsitewise.types.next_token.NextToken"]
    """<p>The token for the next set of paginated results, or null if there are no additional results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListComputationModelResolveToResourcesResponse) -> dict:
    out: dict = {}
    import aws_sdk_iotsitewise.types.computation_model_resolve_to_resource_summaries

    out["computationModelResolveToResourceSummaries"] = (
        aws_sdk_iotsitewise.types.computation_model_resolve_to_resource_summaries.serialize_json(
            value["computation_model_resolve_to_resource_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListComputationModelResolveToResourcesResponse:
    out: ListComputationModelResolveToResourcesResponse = {}  # type: ignore[typeddict-item]
    if "computationModelResolveToResourceSummaries" in data:
        import aws_sdk_iotsitewise.types.computation_model_resolve_to_resource_summaries

        out["computation_model_resolve_to_resource_summaries"] = (
            aws_sdk_iotsitewise.types.computation_model_resolve_to_resource_summaries.deserialize_json(
                data["computationModelResolveToResourceSummaries"]
            )
        )
    else:
        raise DeserializationError(
            "ListComputationModelResolveToResourcesResponse.computation_model_resolve_to_resource_summaries required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
