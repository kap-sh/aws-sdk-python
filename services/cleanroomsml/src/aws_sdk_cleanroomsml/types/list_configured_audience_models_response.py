"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#ListConfiguredAudienceModelsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cleanroomsml.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanroomsml.types.configured_audience_model_list
    import aws_sdk_cleanroomsml.types.next_token


class ListConfiguredAudienceModelsResponse(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_cleanroomsml.types.next_token.NextToken"]
    """<p>The token value used to access the next page of results.</p>"""
    configured_audience_models: "aws_sdk_cleanroomsml.types.configured_audience_model_list.ConfiguredAudienceModelList"
    """<p>The configured audience models.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListConfiguredAudienceModelsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import aws_sdk_cleanroomsml.types.configured_audience_model_list

    out["configuredAudienceModels"] = (
        aws_sdk_cleanroomsml.types.configured_audience_model_list.serialize_json(
            value["configured_audience_models"]
        )
    )
    return out


def deserialize_json(data: dict) -> ListConfiguredAudienceModelsResponse:
    out: ListConfiguredAudienceModelsResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "configuredAudienceModels" in data:
        import aws_sdk_cleanroomsml.types.configured_audience_model_list

        out["configured_audience_models"] = (
            aws_sdk_cleanroomsml.types.configured_audience_model_list.deserialize_json(
                data["configuredAudienceModels"]
            )
        )
    else:
        raise DeserializationError(
            "ListConfiguredAudienceModelsResponse.configured_audience_models required"
        )
    return out
