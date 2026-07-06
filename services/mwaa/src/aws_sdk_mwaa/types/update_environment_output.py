"""Generated from Smithy shape ``com.amazonaws.mwaa#UpdateEnvironmentOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mwaa.types.environment_arn


class UpdateEnvironmentOutput(TypedDict, closed=True):
    arn: NotRequired["aws_sdk_mwaa.types.environment_arn.EnvironmentArn"]
    """<p>The Amazon Resource Name (ARN) of the Amazon MWAA environment. For example, <code>arn:aws:airflow:us-east-1:123456789012:environment/MyMWAAEnvironment</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateEnvironmentOutput) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> UpdateEnvironmentOutput:
    out: UpdateEnvironmentOutput = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    return out
