"""Generated from Smithy shape ``com.amazonaws.resourceexplorer2#GetServiceViewInput``."""

from typing import TypedDict

from aws_sdk_resource_explorer_2.errors import DeserializationError


class GetServiceViewInput(TypedDict):
    service_view_arn: "str"
    """<p>The Amazon Resource Name (ARN) of the service view to retrieve details for.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetServiceViewInput) -> dict:
    out: dict = {}
    out["ServiceViewArn"] = value["service_view_arn"]
    return out


def deserialize_json(data: dict) -> GetServiceViewInput:
    out: GetServiceViewInput = {}  # type: ignore[typeddict-item]
    if "ServiceViewArn" in data:
        out["service_view_arn"] = data["ServiceViewArn"]
    else:
        raise DeserializationError("GetServiceViewInput.service_view_arn required")
    return out
