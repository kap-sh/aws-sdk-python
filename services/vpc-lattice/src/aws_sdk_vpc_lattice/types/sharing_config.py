"""Generated from Smithy shape ``com.amazonaws.vpclattice#SharingConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_vpc_lattice.types.boolean


class SharingConfig(TypedDict, closed=True):
    enabled: NotRequired["aws_sdk_vpc_lattice.types.boolean.Boolean"]
    """<p>Specifies if the service network is enabled for sharing.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SharingConfig) -> dict:
    out: dict = {}
    if "enabled" in value:
        out["enabled"] = value["enabled"]
    return out


def deserialize_json(data: dict) -> SharingConfig:
    out: SharingConfig = {}  # type: ignore[typeddict-item]
    if "enabled" in data:
        out["enabled"] = data["enabled"]
    return out
