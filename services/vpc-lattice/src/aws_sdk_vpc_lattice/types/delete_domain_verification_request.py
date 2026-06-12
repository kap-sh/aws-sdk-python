"""Generated from Smithy shape ``com.amazonaws.vpclattice#DeleteDomainVerificationRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_vpc_lattice.types.domain_verification_identifier


class DeleteDomainVerificationRequest(TypedDict):
    domain_verification_identifier: "aws_sdk_vpc_lattice.types.domain_verification_identifier.DomainVerificationIdentifier"
    """<p> The ID of the domain verification to delete. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDomainVerificationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteDomainVerificationRequest:
    out: DeleteDomainVerificationRequest = {}  # type: ignore[typeddict-item]
    return out
