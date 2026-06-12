"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTransponder``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.sensitive_string


class RouteTransponder(TypedDict):
    system_name: NotRequired[
        "aws_sdk_geo_routes.types.sensitive_string.SensitiveString"
    ]
    """<p>Names of the toll system collecting the toll.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteTransponder) -> dict:
    out: dict = {}
    if "system_name" in value:
        out["SystemName"] = value["system_name"]
    return out


def deserialize_json(data: dict) -> RouteTransponder:
    out: RouteTransponder = {}  # type: ignore[typeddict-item]
    if "SystemName" in data:
        out["system_name"] = data["SystemName"]
    return out
