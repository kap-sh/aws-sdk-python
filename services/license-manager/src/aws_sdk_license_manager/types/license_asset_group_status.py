"""Generated from Smithy shape ``com.amazonaws.licensemanager#LicenseAssetGroupStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>License asset group status. Allowed values are</p> <ul> <li> <p> <code>ACTIVE</code> </p> </li> <li> <p> <code>DISABLED</code> </p> </li> <li> <p> <code>DELETED</code> </p> </li> </ul>"""
LicenseAssetGroupStatus: TypeAlias = Literal[
    "ACTIVE",
    "DISABLED",
    "DELETED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LicenseAssetGroupStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LicenseAssetGroupStatus:
    return cast(LicenseAssetGroupStatus, data)
