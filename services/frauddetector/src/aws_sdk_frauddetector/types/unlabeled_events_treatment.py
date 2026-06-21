"""Generated from Smithy shape ``com.amazonaws.frauddetector#UnlabeledEventsTreatment``."""

from typing import Literal, TypeAlias, cast

UnlabeledEventsTreatment: TypeAlias = Literal[
    "IGNORE",
    "FRAUD",
    "LEGIT",
    "AUTO",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UnlabeledEventsTreatment) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> UnlabeledEventsTreatment:
    return cast(UnlabeledEventsTreatment, data)
