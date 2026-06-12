"""Generated from Smithy shape ``com.amazonaws.detective#CreateGraphResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_detective.types.graph_arn


class CreateGraphResponse(TypedDict):
    graph_arn: NotRequired["aws_sdk_detective.types.graph_arn.GraphArn"]
    """<p>The ARN of the new behavior graph.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateGraphResponse) -> dict:
    out: dict = {}
    if "graph_arn" in value:
        out["GraphArn"] = value["graph_arn"]
    return out


def deserialize_json(data: dict) -> CreateGraphResponse:
    out: CreateGraphResponse = {}  # type: ignore[typeddict-item]
    if "GraphArn" in data:
        out["graph_arn"] = data["GraphArn"]
    return out
