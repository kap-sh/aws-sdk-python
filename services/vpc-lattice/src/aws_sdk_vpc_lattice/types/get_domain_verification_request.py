"""Generated from Smithy shape ``com.amazonaws.vpclattice#GetDomainVerificationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_vpc_lattice.types.domain_verification_identifier


class GetDomainVerificationRequest(TypedDict, closed=True):
    domain_verification_identifier: "aws_sdk_vpc_lattice.types.domain_verification_identifier.DomainVerificationIdentifier"
    """<p> The ID or ARN of the domain verification to retrieve. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDomainVerificationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetDomainVerificationRequest:
    out: GetDomainVerificationRequest = {}  # type: ignore[typeddict-item]
    return out
