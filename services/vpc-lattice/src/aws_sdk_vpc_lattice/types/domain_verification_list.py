"""Generated from Smithy shape ``com.amazonaws.vpclattice#DomainVerificationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_vpc_lattice.types.domain_verification_summary

DomainVerificationList: TypeAlias = list[
    "aws_sdk_vpc_lattice.types.domain_verification_summary.DomainVerificationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: DomainVerificationList) -> list:
    import aws_sdk_vpc_lattice.types.domain_verification_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_vpc_lattice.types.domain_verification_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> DomainVerificationList:
    import aws_sdk_vpc_lattice.types.domain_verification_summary

    out: DomainVerificationList = []
    for item in data:
        out.append(
            aws_sdk_vpc_lattice.types.domain_verification_summary.deserialize_json(item)
        )
    return out
