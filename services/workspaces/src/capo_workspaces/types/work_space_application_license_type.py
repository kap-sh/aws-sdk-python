"""Generated from Smithy shape ``com.amazonaws.workspaces#WorkSpaceApplicationLicenseType``."""

from typing import Literal, TypeAlias, cast

WorkSpaceApplicationLicenseType: TypeAlias = Literal[
    "LICENSED",
    "UNLICENSED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WorkSpaceApplicationLicenseType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> WorkSpaceApplicationLicenseType:
    return cast(WorkSpaceApplicationLicenseType, data)
