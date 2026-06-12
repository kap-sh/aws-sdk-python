"""Generated from Smithy shape ``com.amazonaws.appmesh#EgressFilter``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_app_mesh.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_app_mesh.types.egress_filter_type

class EgressFilter(TypedDict):
    type: "aws_sdk_app_mesh.types.egress_filter_type.EgressFilterType"
    """<p>The egress filter type. By default, the type is <code>DROP_ALL</code>, which allows egress only from virtual nodes to other defined resources in the service mesh (and any traffic to <code>*.amazonaws.com</code> for Amazon Web Services API calls). You can set the egress filter type to <code>ALLOW_ALL</code> to allow egress to any endpoint inside or outside of the service mesh.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: EgressFilter) -> dict:
    out: dict = {}
    out["type"] = value["type"]
    return out


def deserialize_json(data: dict) -> EgressFilter:
    out: EgressFilter = {}  # type: ignore[typeddict-item]
    if "type" in data:
        out["type"] = data["type"]
    else:
        raise DeserializationError("EgressFilter.type required")
    return out