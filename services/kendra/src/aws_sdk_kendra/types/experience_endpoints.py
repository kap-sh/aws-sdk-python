"""Generated from Smithy shape ``com.amazonaws.kendra#ExperienceEndpoints``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kendra.types.experience_endpoint

ExperienceEndpoints: TypeAlias = list[
    "aws_sdk_kendra.types.experience_endpoint.ExperienceEndpoint"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExperienceEndpoints) -> list:
    import aws_sdk_kendra.types.experience_endpoint

    out: list = []
    for item in value:
        out.append(
            aws_sdk_kendra.types.experience_endpoint.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ExperienceEndpoints:
    import aws_sdk_kendra.types.experience_endpoint

    out: ExperienceEndpoints = []
    for item in data:
        out.append(
            aws_sdk_kendra.types.experience_endpoint.deserialize_aws_json_1_1(item)
        )
    return out
