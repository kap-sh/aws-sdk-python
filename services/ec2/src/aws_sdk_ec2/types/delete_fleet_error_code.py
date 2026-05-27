"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteFleetErrorCode``."""

from typing import Literal, TypeAlias

DeleteFleetErrorCode: TypeAlias = Literal[
    "fleetIdDoesNotExist",
    "fleetIdMalformed",
    "fleetNotInDeletableState",
    "unexpectedError",
]
