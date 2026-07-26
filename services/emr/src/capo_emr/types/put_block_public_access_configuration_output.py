"""Generated from Smithy shape ``com.amazonaws.emr#PutBlockPublicAccessConfigurationOutput``."""

from typing_extensions import TypedDict


class PutBlockPublicAccessConfigurationOutput(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutBlockPublicAccessConfigurationOutput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> PutBlockPublicAccessConfigurationOutput:
    out: PutBlockPublicAccessConfigurationOutput = {}  # type: ignore[typeddict-item]
    return out
