"""Generated from Smithy shape ``com.amazonaws.resourceexplorer2#GetManagedViewInput``."""

from typing import TypedDict

from aws_sdk_resource_explorer_2.errors import DeserializationError


class GetManagedViewInput(TypedDict):
    managed_view_arn: "str"
    """<p>The Amazon resource name (ARN) of the managed view.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetManagedViewInput) -> dict:
    out: dict = {}
    out["ManagedViewArn"] = value["managed_view_arn"]
    return out


def deserialize_json(data: dict) -> GetManagedViewInput:
    out: GetManagedViewInput = {}  # type: ignore[typeddict-item]
    if "ManagedViewArn" in data:
        out["managed_view_arn"] = data["ManagedViewArn"]
    else:
        raise DeserializationError("GetManagedViewInput.managed_view_arn required")
    return out
