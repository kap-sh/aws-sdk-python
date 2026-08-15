"""Generated from Smithy shape ``com.amazonaws.lambda#S3ObjectStorageMode``."""

from typing import Literal, TypeAlias, cast

"""<p>The method Lambda uses to store a function's deployment package — either by copying the package into Lambda-managed storage (<code>COPY</code>) or by referencing it directly from the source Amazon S3 bucket (<code>REFERENCE</code>).</p>"""
S3ObjectStorageMode: TypeAlias = Literal[
    "COPY",
    "REFERENCE",
]


# --- restJson1 ser/de ---
def serialize_json(value: S3ObjectStorageMode) -> str:
    return value


def deserialize_json(data: str) -> S3ObjectStorageMode:
    return cast(S3ObjectStorageMode, data)
