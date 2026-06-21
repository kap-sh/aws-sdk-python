"""Generated from Smithy shape ``com.amazonaws.macie2#StorageClass``."""

from typing import Literal, TypeAlias, cast

"""<p>The storage class of the S3 object. Possible values are:</p>"""
StorageClass: TypeAlias = Literal[
    "STANDARD",
    "REDUCED_REDUNDANCY",
    "STANDARD_IA",
    "INTELLIGENT_TIERING",
    "DEEP_ARCHIVE",
    "ONEZONE_IA",
    "GLACIER",
    "GLACIER_IR",
    "OUTPOSTS",
]


# --- restJson1 ser/de ---
def serialize_json(value: StorageClass) -> str:
    return value


def deserialize_json(data: str) -> StorageClass:
    return cast(StorageClass, data)
