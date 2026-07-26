"""Generated from Smithy shape ``com.amazonaws.fsx#FilterName``."""

from typing import Literal, TypeAlias, cast

"""<p>The name for a filter.</p>"""
FilterName: TypeAlias = Literal[
    "file-system-id",
    "backup-type",
    "file-system-type",
    "volume-id",
    "data-repository-type",
    "file-cache-id",
    "file-cache-type",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FilterName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FilterName:
    return cast(FilterName, data)
