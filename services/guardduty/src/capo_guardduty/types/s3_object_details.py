"""Generated from Smithy shape ``com.amazonaws.guardduty#S3ObjectDetails``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.s3_object_detail

S3ObjectDetails: TypeAlias = list[
    "capo_guardduty.types.s3_object_detail.S3ObjectDetail"
]


# --- restJson1 ser/de ---
def serialize_json(value: S3ObjectDetails) -> list:
    import capo_guardduty.types.s3_object_detail

    out: list = []
    for item in value:
        out.append(capo_guardduty.types.s3_object_detail.serialize_json(item))
    return out


def deserialize_json(data: list) -> S3ObjectDetails:
    import capo_guardduty.types.s3_object_detail

    out: S3ObjectDetails = []
    for item in data:
        out.append(capo_guardduty.types.s3_object_detail.deserialize_json(item))
    return out
