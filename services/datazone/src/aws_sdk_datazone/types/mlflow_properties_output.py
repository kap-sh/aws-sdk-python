"""Generated from Smithy shape ``com.amazonaws.datazone#MlflowPropertiesOutput``."""

from typing import TypedDict

from typing_extensions import NotRequired


class MlflowPropertiesOutput(TypedDict):
    tracking_server_arn: NotRequired["str"]
    """<p>The tracking server ARN as part of the MLflow properties of a connection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MlflowPropertiesOutput) -> dict:
    out: dict = {}
    if "tracking_server_arn" in value:
        out["trackingServerArn"] = value["tracking_server_arn"]
    return out


def deserialize_json(data: dict) -> MlflowPropertiesOutput:
    out: MlflowPropertiesOutput = {}  # type: ignore[typeddict-item]
    if "trackingServerArn" in data:
        out["tracking_server_arn"] = data["trackingServerArn"]
    return out
