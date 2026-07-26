"""Generated from Smithy shape ``com.amazonaws.shield#TopContributors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_shield.types.contributor

TopContributors: TypeAlias = list["capo_shield.types.contributor.Contributor"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TopContributors) -> list:
    import capo_shield.types.contributor

    out: list = []
    for item in value:
        out.append(capo_shield.types.contributor.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> TopContributors:
    import capo_shield.types.contributor

    out: TopContributors = []
    for item in data:
        out.append(capo_shield.types.contributor.deserialize_aws_json_1_1(item))
    return out
