"""Generated from Smithy shape ``com.amazonaws.controlcatalog#ObjectiveResourceFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_controlcatalog.types.objective_arn


class ObjectiveResourceFilter(TypedDict, closed=True):
    arn: NotRequired["aws_sdk_controlcatalog.types.objective_arn.ObjectiveArn"]
    """<p>The Amazon Resource Name (ARN) of the objective.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ObjectiveResourceFilter) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> ObjectiveResourceFilter:
    out: ObjectiveResourceFilter = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    return out
