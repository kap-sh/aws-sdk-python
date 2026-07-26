"""Generated from Smithy shape ``com.amazonaws.detective#DeleteGraphRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_detective.errors import DeserializationError

if TYPE_CHECKING:
    import capo_detective.types.graph_arn


class DeleteGraphRequest(TypedDict, closed=True):
    graph_arn: "capo_detective.types.graph_arn.GraphArn"
    """<p>The ARN of the behavior graph to disable.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteGraphRequest) -> dict:
    out: dict = {}
    out["GraphArn"] = value["graph_arn"]
    return out


def deserialize_json(data: dict) -> DeleteGraphRequest:
    out: DeleteGraphRequest = {}  # type: ignore[typeddict-item]
    if "GraphArn" in data:
        out["graph_arn"] = data["GraphArn"]
    else:
        raise DeserializationError("DeleteGraphRequest.graph_arn required")
    return out
