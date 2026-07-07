"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#ListAudienceModelsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cleanroomsml.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanroomsml.types.audience_model_list
    import aws_sdk_cleanroomsml.types.next_token


class ListAudienceModelsResponse(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_cleanroomsml.types.next_token.NextToken"]
    """<p>The token value used to access the next page of results.</p>"""
    audience_models: "aws_sdk_cleanroomsml.types.audience_model_list.AudienceModelList"
    """<p>The audience models that match the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAudienceModelsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import aws_sdk_cleanroomsml.types.audience_model_list

    out["audienceModels"] = (
        aws_sdk_cleanroomsml.types.audience_model_list.serialize_json(
            value["audience_models"]
        )
    )
    return out


def deserialize_json(data: dict) -> ListAudienceModelsResponse:
    out: ListAudienceModelsResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "audienceModels" in data:
        import aws_sdk_cleanroomsml.types.audience_model_list

        out["audience_models"] = (
            aws_sdk_cleanroomsml.types.audience_model_list.deserialize_json(
                data["audienceModels"]
            )
        )
    else:
        raise DeserializationError(
            "ListAudienceModelsResponse.audience_models required"
        )
    return out
