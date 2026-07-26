"""Generated from Smithy shape ``com.amazonaws.ecr#RelatedVulnerabilitiesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecr.types.related_vulnerability

RelatedVulnerabilitiesList: TypeAlias = list[
    "capo_ecr.types.related_vulnerability.RelatedVulnerability"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RelatedVulnerabilitiesList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> RelatedVulnerabilitiesList:
    return list(data)
