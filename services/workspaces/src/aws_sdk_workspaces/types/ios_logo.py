"""Generated from Smithy shape ``com.amazonaws.workspaces#IosLogo``."""

import base64
from typing import TypeAlias

IosLogo: TypeAlias = bytes


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IosLogo) -> str:
    return base64.b64encode(value).decode("ascii")


def deserialize_aws_json_1_1(data: str) -> IosLogo:
    return base64.b64decode(data)
