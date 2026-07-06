"""Generated from Smithy shape ``com.amazonaws.m2#StopApplicationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_m2.types.boolean
    import aws_sdk_m2.types.identifier


class StopApplicationRequest(TypedDict, closed=True):
    application_id: "aws_sdk_m2.types.identifier.Identifier"
    """<p>The unique identifier of the application you want to stop.</p>"""
    force_stop: "aws_sdk_m2.types.boolean.Boolean"
    """<p>Stopping an application process can take a long time. Setting this parameter to true lets you force stop the application so you don't need to wait until the process finishes to apply another action on the application. The default value is false.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StopApplicationRequest) -> dict:
    out: dict = {}
    out["forceStop"] = value.get("force_stop", False)
    return out


def deserialize_json(data: dict) -> StopApplicationRequest:
    out: StopApplicationRequest = {}  # type: ignore[typeddict-item]
    if "forceStop" in data:
        out["force_stop"] = data["forceStop"]
    else:
        out["force_stop"] = False
    return out
