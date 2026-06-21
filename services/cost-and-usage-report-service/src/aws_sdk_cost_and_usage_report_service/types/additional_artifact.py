"""Generated from Smithy shape ``com.amazonaws.costandusagereportservice#AdditionalArtifact``."""

from typing import Literal, TypeAlias, cast

"""<p>The types of manifest that you want Amazon Web Services to create for this report.</p>"""
AdditionalArtifact: TypeAlias = Literal[
    "REDSHIFT",
    "QUICKSIGHT",
    "ATHENA",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AdditionalArtifact) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AdditionalArtifact:
    return cast(AdditionalArtifact, data)
