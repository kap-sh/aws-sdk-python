"""Generated from Smithy shape ``com.amazonaws.macie2#ClassificationScopeUpdateOperation``."""

from typing import Literal, TypeAlias, cast

"""<p>Specifies how to apply changes to the S3 bucket exclusion list defined by the classification scope for an Amazon Macie account. Valid values are:</p>"""
ClassificationScopeUpdateOperation: TypeAlias = Literal[
    "ADD",
    "REPLACE",
    "REMOVE",
]


# --- restJson1 ser/de ---
def serialize_json(value: ClassificationScopeUpdateOperation) -> str:
    return value


def deserialize_json(data: str) -> ClassificationScopeUpdateOperation:
    return cast(ClassificationScopeUpdateOperation, data)
