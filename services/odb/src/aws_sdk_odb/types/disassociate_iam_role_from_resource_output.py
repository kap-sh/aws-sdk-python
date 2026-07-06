"""Generated from Smithy shape ``com.amazonaws.odb#DisassociateIamRoleFromResourceOutput``."""

from typing_extensions import TypedDict


class DisassociateIamRoleFromResourceOutput(TypedDict, closed=True):
    pass


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DisassociateIamRoleFromResourceOutput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> DisassociateIamRoleFromResourceOutput:
    out: DisassociateIamRoleFromResourceOutput = {}  # type: ignore[typeddict-item]
    return out
