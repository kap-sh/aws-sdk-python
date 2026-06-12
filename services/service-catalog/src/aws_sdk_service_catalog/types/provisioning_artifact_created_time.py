"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ProvisioningArtifactCreatedTime``."""

import datetime
from typing import TypeAlias

ProvisioningArtifactCreatedTime: TypeAlias = datetime.datetime


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProvisioningArtifactCreatedTime) -> float:
    return value.timestamp()


def deserialize_aws_json_1_1(data: float) -> ProvisioningArtifactCreatedTime:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
