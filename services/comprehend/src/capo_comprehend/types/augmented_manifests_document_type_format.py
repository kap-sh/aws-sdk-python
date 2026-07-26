"""Generated from Smithy shape ``com.amazonaws.comprehend#AugmentedManifestsDocumentTypeFormat``."""

from typing import Literal, TypeAlias, cast

AugmentedManifestsDocumentTypeFormat: TypeAlias = Literal[
    "PLAIN_TEXT_DOCUMENT",
    "SEMI_STRUCTURED_DOCUMENT",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AugmentedManifestsDocumentTypeFormat) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AugmentedManifestsDocumentTypeFormat:
    return cast(AugmentedManifestsDocumentTypeFormat, data)
