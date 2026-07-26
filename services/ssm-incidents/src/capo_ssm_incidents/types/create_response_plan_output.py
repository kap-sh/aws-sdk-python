"""Generated from Smithy shape ``com.amazonaws.ssmincidents#CreateResponsePlanOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_ssm_incidents.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ssm_incidents.types.arn


class CreateResponsePlanOutput(TypedDict, closed=True):
    arn: "capo_ssm_incidents.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the response plan.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateResponsePlanOutput) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> CreateResponsePlanOutput:
    out: CreateResponsePlanOutput = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("CreateResponsePlanOutput.arn required")
    return out
