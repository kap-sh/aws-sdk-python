"""Generated from Smithy shape ``com.amazonaws.connecthealth#S3Sources``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connecthealth.types.s3_source

S3Sources: TypeAlias = list["capo_connecthealth.types.s3_source.S3Source"]


# --- restJson1 ser/de ---
def serialize_json(value: S3Sources) -> list:
    import capo_connecthealth.types.s3_source

    out: list = []
    for item in value:
        out.append(capo_connecthealth.types.s3_source.serialize_json(item))
    return out


def deserialize_json(data: list) -> S3Sources:
    import capo_connecthealth.types.s3_source

    out: S3Sources = []
    for item in data:
        out.append(capo_connecthealth.types.s3_source.deserialize_json(item))
    return out
