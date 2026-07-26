"""Generated from Smithy shape ``com.amazonaws.licensemanager#LicenseDeletionStatus``."""

from typing import Literal, TypeAlias, cast

LicenseDeletionStatus: TypeAlias = Literal[
    "PENDING_DELETE",
    "DELETED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LicenseDeletionStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LicenseDeletionStatus:
    return cast(LicenseDeletionStatus, data)
