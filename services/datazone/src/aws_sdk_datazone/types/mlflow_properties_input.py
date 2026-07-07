"""Generated from Smithy shape ``com.amazonaws.datazone#MlflowPropertiesInput``."""

from typing_extensions import NotRequired, TypedDict


class MlflowPropertiesInput(TypedDict, closed=True):
    tracking_server_arn: NotRequired["str"]
    """<p>The tracking server ARN as part of the MLflow properties of a connection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MlflowPropertiesInput) -> dict:
    out: dict = {}
    if "tracking_server_arn" in value:
        out["trackingServerArn"] = value["tracking_server_arn"]
    return out


def deserialize_json(data: dict) -> MlflowPropertiesInput:
    out: MlflowPropertiesInput = {}  # type: ignore[typeddict-item]
    if "trackingServerArn" in data:
        out["tracking_server_arn"] = data["trackingServerArn"]
    return out
