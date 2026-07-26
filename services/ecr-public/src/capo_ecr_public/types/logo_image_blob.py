"""Generated from Smithy shape ``com.amazonaws.ecrpublic#LogoImageBlob``."""

import base64
from typing import TypeAlias

LogoImageBlob: TypeAlias = bytes


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LogoImageBlob) -> str:
    return base64.b64encode(value).decode("ascii")


def deserialize_aws_json_1_1(data: str) -> LogoImageBlob:
    return base64.b64decode(data)
