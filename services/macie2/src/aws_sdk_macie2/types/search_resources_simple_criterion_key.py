"""Generated from Smithy shape ``com.amazonaws.macie2#SearchResourcesSimpleCriterionKey``."""

from typing import Literal, TypeAlias, cast

"""<p>The property to use in a condition that filters the query results. Valid values are:</p>"""
SearchResourcesSimpleCriterionKey: TypeAlias = Literal[
    "ACCOUNT_ID",
    "S3_BUCKET_NAME",
    "S3_BUCKET_EFFECTIVE_PERMISSION",
    "S3_BUCKET_SHARED_ACCESS",
    "AUTOMATED_DISCOVERY_MONITORING_STATUS",
]


# --- restJson1 ser/de ---
def serialize_json(value: SearchResourcesSimpleCriterionKey) -> str:
    return value


def deserialize_json(data: str) -> SearchResourcesSimpleCriterionKey:
    return cast(SearchResourcesSimpleCriterionKey, data)
