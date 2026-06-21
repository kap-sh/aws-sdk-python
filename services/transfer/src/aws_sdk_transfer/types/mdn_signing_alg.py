"""Generated from Smithy shape ``com.amazonaws.transfer#MdnSigningAlg``."""

from typing import Literal, TypeAlias, cast

MdnSigningAlg: TypeAlias = Literal[
    "SHA256",
    "SHA384",
    "SHA512",
    "SHA1",
    "NONE",
    "DEFAULT",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MdnSigningAlg) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MdnSigningAlg:
    return cast(MdnSigningAlg, data)
