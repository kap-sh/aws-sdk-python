"""Generated from Smithy shape ``com.amazonaws.cloudwatch#AssociateDatasetKmsKeyOutput``."""

from typing import TypedDict

from aws_sdk_cloudwatch._protocol.xml import Element


class AssociateDatasetKmsKeyOutput(TypedDict):
    pass


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AssociateDatasetKmsKeyOutput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> AssociateDatasetKmsKeyOutput:
    out: AssociateDatasetKmsKeyOutput = {}  # type: ignore[typeddict-item]
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: AssociateDatasetKmsKeyOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pass


def deserialize_query(el: Element) -> AssociateDatasetKmsKeyOutput:
    out: AssociateDatasetKmsKeyOutput = {}  # type: ignore[typeddict-item]
    return out
