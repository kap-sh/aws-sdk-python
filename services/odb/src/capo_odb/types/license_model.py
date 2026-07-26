"""Generated from Smithy shape ``com.amazonaws.odb#LicenseModel``."""

from typing import Literal, TypeAlias, cast

LicenseModel: TypeAlias = Literal[
    "BRING_YOUR_OWN_LICENSE",
    "LICENSE_INCLUDED",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LicenseModel) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> LicenseModel:
    return cast(LicenseModel, data)
