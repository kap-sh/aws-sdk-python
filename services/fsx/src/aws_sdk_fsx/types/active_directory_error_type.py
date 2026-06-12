"""Generated from Smithy shape ``com.amazonaws.fsx#ActiveDirectoryErrorType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_fsx.errors import DeserializationError

"""<p>The type of error relating to Microsoft Active Directory. NOT_FOUND means that no directory was found by specifying the given directory. INCOMPATIBLE_MODE means that the directory specified is not a Microsoft AD directory. WRONG_VPC means that the specified directory isn't accessible from the specified VPC. WRONG_STAGE means that the specified directory isn't currently in the ACTIVE state.</p>"""
ActiveDirectoryErrorType: TypeAlias = Literal[
    "DOMAIN_NOT_FOUND",
    "INCOMPATIBLE_DOMAIN_MODE",
    "WRONG_VPC",
    "INVALID_NETWORK_TYPE",
    "INVALID_DOMAIN_STAGE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DOMAIN_NOT_FOUND",
        "INCOMPATIBLE_DOMAIN_MODE",
        "WRONG_VPC",
        "INVALID_NETWORK_TYPE",
        "INVALID_DOMAIN_STAGE",
    )
)


def serialize_aws_json_1_1(value: ActiveDirectoryErrorType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ActiveDirectoryErrorType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ActiveDirectoryErrorType value: {data!r}")
    return cast(ActiveDirectoryErrorType, data)
