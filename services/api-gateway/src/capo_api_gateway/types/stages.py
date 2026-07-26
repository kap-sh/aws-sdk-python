"""Generated from Smithy shape ``com.amazonaws.apigateway#Stages``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_api_gateway.types.list_of_stage


class Stages(TypedDict, closed=True):
    item: NotRequired["capo_api_gateway.types.list_of_stage.ListOfStage"]
    """<p>The current page of elements from this collection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Stages) -> dict:
    out: dict = {}
    if "item" in value:
        import capo_api_gateway.types.list_of_stage

        out["item"] = capo_api_gateway.types.list_of_stage.serialize_json(value["item"])
    return out


def deserialize_json(data: dict) -> Stages:
    out: Stages = {}  # type: ignore[typeddict-item]
    if "item" in data:
        import capo_api_gateway.types.list_of_stage

        out["item"] = capo_api_gateway.types.list_of_stage.deserialize_json(
            data["item"]
        )
    return out
