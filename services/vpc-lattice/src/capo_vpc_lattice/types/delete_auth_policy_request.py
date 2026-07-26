"""Generated from Smithy shape ``com.amazonaws.vpclattice#DeleteAuthPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_vpc_lattice.types.resource_identifier


class DeleteAuthPolicyRequest(TypedDict, closed=True):
    resource_identifier: "capo_vpc_lattice.types.resource_identifier.ResourceIdentifier"
    """<p>The ID or ARN of the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAuthPolicyRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteAuthPolicyRequest:
    out: DeleteAuthPolicyRequest = {}  # type: ignore[typeddict-item]
    return out
