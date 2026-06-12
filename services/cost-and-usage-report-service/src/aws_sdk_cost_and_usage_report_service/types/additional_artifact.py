"""Generated from Smithy shape ``com.amazonaws.costandusagereportservice#AdditionalArtifact``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cost_and_usage_report_service.errors import DeserializationError

"""<p>The types of manifest that you want Amazon Web Services to create for this report.</p>"""
AdditionalArtifact: TypeAlias = Literal[
    "REDSHIFT",
    "QUICKSIGHT",
    "ATHENA",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "REDSHIFT",
        "QUICKSIGHT",
        "ATHENA",
    )
)


def serialize_aws_json_1_1(value: AdditionalArtifact) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AdditionalArtifact:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AdditionalArtifact value: {data!r}")
    return cast(AdditionalArtifact, data)
