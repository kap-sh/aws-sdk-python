"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#ListAudienceModelsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cleanroomsml.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cleanroomsml.types.audience_model_list
    import capo_cleanroomsml.types.next_token


class ListAudienceModelsResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_cleanroomsml.types.next_token.NextToken"]
    """<p>The token value used to access the next page of results.</p>"""
    audience_models: "capo_cleanroomsml.types.audience_model_list.AudienceModelList"
    """<p>The audience models that match the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAudienceModelsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_cleanroomsml.types.audience_model_list

    out["audienceModels"] = capo_cleanroomsml.types.audience_model_list.serialize_json(
        value["audience_models"]
    )
    return out


def deserialize_json(data: dict) -> ListAudienceModelsResponse:
    out: ListAudienceModelsResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "audienceModels" in data:
        import capo_cleanroomsml.types.audience_model_list

        out["audience_models"] = (
            capo_cleanroomsml.types.audience_model_list.deserialize_json(
                data["audienceModels"]
            )
        )
    else:
        raise DeserializationError(
            "ListAudienceModelsResponse.audience_models required"
        )
    return out
