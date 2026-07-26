"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#ListTagsForResourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_observabilityadmin.errors import DeserializationError

if TYPE_CHECKING:
    import capo_observabilityadmin.types.resource_arn


class ListTagsForResourceInput(TypedDict, closed=True):
    resource_arn: "capo_observabilityadmin.types.resource_arn.ResourceArn"
    """<p> The Amazon Resource Name (ARN) of the telemetry rule resource whose tags you want to list. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceInput) -> dict:
    out: dict = {}
    out["ResourceARN"] = value["resource_arn"]
    return out


def deserialize_json(data: dict) -> ListTagsForResourceInput:
    out: ListTagsForResourceInput = {}  # type: ignore[typeddict-item]
    if "ResourceARN" in data:
        out["resource_arn"] = data["ResourceARN"]
    else:
        raise DeserializationError("ListTagsForResourceInput.resource_arn required")
    return out
