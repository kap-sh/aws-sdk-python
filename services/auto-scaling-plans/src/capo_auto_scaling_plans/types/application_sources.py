"""Generated from Smithy shape ``com.amazonaws.autoscalingplans#ApplicationSources``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_auto_scaling_plans.types.application_source

ApplicationSources: TypeAlias = list[
    "capo_auto_scaling_plans.types.application_source.ApplicationSource"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApplicationSources) -> list:
    import capo_auto_scaling_plans.types.application_source

    out: list = []
    for item in value:
        out.append(
            capo_auto_scaling_plans.types.application_source.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ApplicationSources:
    import capo_auto_scaling_plans.types.application_source

    out: ApplicationSources = []
    for item in data:
        out.append(
            capo_auto_scaling_plans.types.application_source.deserialize_aws_json_1_1(
                item
            )
        )
    return out
