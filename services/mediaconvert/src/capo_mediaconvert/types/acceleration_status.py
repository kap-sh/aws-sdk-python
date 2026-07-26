"""Generated from Smithy shape ``com.amazonaws.mediaconvert#AccelerationStatus``."""

from typing import Literal, TypeAlias, cast

"""Describes whether the current job is running with accelerated transcoding. For jobs that have Acceleration (AccelerationMode) set to DISABLED, AccelerationStatus is always NOT_APPLICABLE. For jobs that have Acceleration (AccelerationMode) set to ENABLED or PREFERRED, AccelerationStatus is one of the other states. AccelerationStatus is IN_PROGRESS initially, while the service determines whether the input files and job settings are compatible with accelerated transcoding. If they are, AcclerationStatus is ACCELERATED. If your input files and job settings aren't compatible with accelerated transcoding, the service either fails your job or runs it without accelerated transcoding, depending on how you set Acceleration (AccelerationMode). When the service runs your job without accelerated transcoding, AccelerationStatus is NOT_ACCELERATED."""
AccelerationStatus: TypeAlias = Literal[
    "NOT_APPLICABLE",
    "IN_PROGRESS",
    "ACCELERATED",
    "NOT_ACCELERATED",
]


# --- restJson1 ser/de ---
def serialize_json(value: AccelerationStatus) -> str:
    return value


def deserialize_json(data: str) -> AccelerationStatus:
    return cast(AccelerationStatus, data)
