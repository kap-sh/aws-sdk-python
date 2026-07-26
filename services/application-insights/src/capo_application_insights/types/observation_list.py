"""Generated from Smithy shape ``com.amazonaws.applicationinsights#ObservationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_application_insights.types.observation

ObservationList: TypeAlias = list[
    "capo_application_insights.types.observation.Observation"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ObservationList) -> list:
    import capo_application_insights.types.observation

    out: list = []
    for item in value:
        out.append(
            capo_application_insights.types.observation.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ObservationList:
    import capo_application_insights.types.observation

    out: ObservationList = []
    for item in data:
        out.append(
            capo_application_insights.types.observation.deserialize_aws_json_1_1(item)
        )
    return out
