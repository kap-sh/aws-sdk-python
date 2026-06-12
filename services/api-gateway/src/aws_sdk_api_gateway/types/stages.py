"""Generated from Smithy shape ``com.amazonaws.apigateway#Stages``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_api_gateway.types.list_of_stage


class Stages(TypedDict):
    item: NotRequired["aws_sdk_api_gateway.types.list_of_stage.ListOfStage"]
    """<p>The current page of elements from this collection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Stages) -> dict:
    out: dict = {}
    if "item" in value:
        import aws_sdk_api_gateway.types.list_of_stage

        out["item"] = aws_sdk_api_gateway.types.list_of_stage.serialize_json(
            value["item"]
        )
    return out


def deserialize_json(data: dict) -> Stages:
    out: Stages = {}  # type: ignore[typeddict-item]
    if "item" in data:
        import aws_sdk_api_gateway.types.list_of_stage

        out["item"] = aws_sdk_api_gateway.types.list_of_stage.deserialize_json(
            data["item"]
        )
    return out
