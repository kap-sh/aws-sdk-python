"""Generated from Smithy shape ``com.amazonaws.vpclattice#ArnResource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_vpc_lattice.types.wildcard_arn


class ArnResource(TypedDict, closed=True):
    arn: NotRequired["capo_vpc_lattice.types.wildcard_arn.WildcardArn"]
    """<p>The Amazon Resource Name (ARN) of the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ArnResource) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> ArnResource:
    out: ArnResource = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    return out
