"""Generated from Smithy shape ``com.amazonaws.frauddetector#ListOfModelVersions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_frauddetector.types.model_version

ListOfModelVersions: TypeAlias = list[
    "capo_frauddetector.types.model_version.ModelVersion"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListOfModelVersions) -> list:
    import capo_frauddetector.types.model_version

    out: list = []
    for item in value:
        out.append(capo_frauddetector.types.model_version.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ListOfModelVersions:
    import capo_frauddetector.types.model_version

    out: ListOfModelVersions = []
    for item in data:
        out.append(
            capo_frauddetector.types.model_version.deserialize_aws_json_1_1(item)
        )
    return out
