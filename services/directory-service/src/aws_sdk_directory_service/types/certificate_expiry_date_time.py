"""Generated from Smithy shape ``com.amazonaws.directoryservice#CertificateExpiryDateTime``."""

import datetime
from typing import TypeAlias

CertificateExpiryDateTime: TypeAlias = datetime.datetime


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CertificateExpiryDateTime) -> float:
    return value.timestamp()


def deserialize_aws_json_1_1(data: float) -> CertificateExpiryDateTime:
    return datetime.datetime.fromtimestamp(float(data), tz=datetime.timezone.utc)
