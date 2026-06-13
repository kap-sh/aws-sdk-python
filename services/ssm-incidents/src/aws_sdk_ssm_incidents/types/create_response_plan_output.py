"""Generated from Smithy shape ``com.amazonaws.ssmincidents#CreateResponsePlanOutput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_ssm_incidents.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm_incidents.types.arn


class CreateResponsePlanOutput(TypedDict):
    arn: "aws_sdk_ssm_incidents.types.arn.Arn"
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
