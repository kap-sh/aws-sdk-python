"""Generated from Smithy shape ``com.amazonaws.licensemanager#CheckInLicenseResponse``."""

from typing_extensions import TypedDict


class CheckInLicenseResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CheckInLicenseResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> CheckInLicenseResponse:
    out: CheckInLicenseResponse = {}  # type: ignore[typeddict-item]
    return out
