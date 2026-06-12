"""Generated from Smithy shape ``com.amazonaws.ssm#MaintenanceWindowLambdaPayload``."""

import base64
from typing import TypeAlias

MaintenanceWindowLambdaPayload: TypeAlias = bytes


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MaintenanceWindowLambdaPayload) -> str:
    return base64.b64encode(value).decode("ascii")


def deserialize_aws_json_1_1(data: str) -> MaintenanceWindowLambdaPayload:
    return base64.b64decode(data)
