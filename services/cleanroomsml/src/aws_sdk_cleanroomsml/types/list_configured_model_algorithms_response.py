"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#ListConfiguredModelAlgorithmsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cleanroomsml.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanroomsml.types.configured_model_algorithm_list
    import aws_sdk_cleanroomsml.types.next_token


class ListConfiguredModelAlgorithmsResponse(TypedDict):
    next_token: NotRequired["aws_sdk_cleanroomsml.types.next_token.NextToken"]
    """<p>The token value used to access the next page of results.</p>"""
    configured_model_algorithms: "aws_sdk_cleanroomsml.types.configured_model_algorithm_list.ConfiguredModelAlgorithmList"
    """<p>The list of configured model algorithms.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListConfiguredModelAlgorithmsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import aws_sdk_cleanroomsml.types.configured_model_algorithm_list

    out["configuredModelAlgorithms"] = (
        aws_sdk_cleanroomsml.types.configured_model_algorithm_list.serialize_json(
            value["configured_model_algorithms"]
        )
    )
    return out


def deserialize_json(data: dict) -> ListConfiguredModelAlgorithmsResponse:
    out: ListConfiguredModelAlgorithmsResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "configuredModelAlgorithms" in data:
        import aws_sdk_cleanroomsml.types.configured_model_algorithm_list

        out["configured_model_algorithms"] = (
            aws_sdk_cleanroomsml.types.configured_model_algorithm_list.deserialize_json(
                data["configuredModelAlgorithms"]
            )
        )
    else:
        raise DeserializationError(
            "ListConfiguredModelAlgorithmsResponse.configured_model_algorithms required"
        )
    return out
