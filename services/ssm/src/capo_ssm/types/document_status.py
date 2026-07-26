"""Generated from Smithy shape ``com.amazonaws.ssm#DocumentStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>The status of a document.</p>"""
DocumentStatus: TypeAlias = Literal[
    "Creating",
    "Active",
    "Updating",
    "Deleting",
    "Failed",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DocumentStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DocumentStatus:
    return cast(DocumentStatus, data)
