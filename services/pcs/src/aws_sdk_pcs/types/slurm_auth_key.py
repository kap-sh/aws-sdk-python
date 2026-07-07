"""Generated from Smithy shape ``com.amazonaws.pcs#SlurmAuthKey``."""

from typing_extensions import TypedDict

from aws_sdk_pcs.errors import DeserializationError


class SlurmAuthKey(TypedDict, closed=True):
    secret_arn: "str"
    """<p>The Amazon Resource Name (ARN) of the shared Slurm key.</p>"""
    secret_version: "str"
    """<p>The version of the shared Slurm key.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SlurmAuthKey) -> dict:
    out: dict = {}
    out["secretArn"] = value["secret_arn"]
    out["secretVersion"] = value["secret_version"]
    return out


def deserialize_aws_json_1_0(data: dict) -> SlurmAuthKey:
    out: SlurmAuthKey = {}  # type: ignore[typeddict-item]
    if "secretArn" in data:
        out["secret_arn"] = data["secretArn"]
    else:
        raise DeserializationError("SlurmAuthKey.secret_arn required")
    if "secretVersion" in data:
        out["secret_version"] = data["secretVersion"]
    else:
        raise DeserializationError("SlurmAuthKey.secret_version required")
    return out
