"""Generated from Smithy shape ``com.amazonaws.vpclattice#GetAuthPolicyRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_vpc_lattice.types.resource_identifier


class GetAuthPolicyRequest(TypedDict):
    resource_identifier: (
        "aws_sdk_vpc_lattice.types.resource_identifier.ResourceIdentifier"
    )
    """<p>The ID or ARN of the service network or service.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAuthPolicyRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetAuthPolicyRequest:
    out: GetAuthPolicyRequest = {}  # type: ignore[typeddict-item]
    return out
