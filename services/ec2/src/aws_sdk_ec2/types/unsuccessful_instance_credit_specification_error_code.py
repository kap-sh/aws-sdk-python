"""Generated from Smithy shape ``com.amazonaws.ec2#UnsuccessfulInstanceCreditSpecificationErrorCode``."""

from typing import Literal, TypeAlias

UnsuccessfulInstanceCreditSpecificationErrorCode: TypeAlias = Literal[
    "InvalidInstanceID.Malformed",
    "InvalidInstanceID.NotFound",
    "IncorrectInstanceState",
    "InstanceCreditSpecification.NotSupported",
]
