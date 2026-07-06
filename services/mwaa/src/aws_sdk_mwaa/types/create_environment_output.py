"""Generated from Smithy shape ``com.amazonaws.mwaa#CreateEnvironmentOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mwaa.types.environment_arn


class CreateEnvironmentOutput(TypedDict, closed=True):
    arn: NotRequired["aws_sdk_mwaa.types.environment_arn.EnvironmentArn"]
    """<p>The Amazon Resource Name (ARN) returned in the response for the environment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateEnvironmentOutput) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> CreateEnvironmentOutput:
    out: CreateEnvironmentOutput = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    return out
