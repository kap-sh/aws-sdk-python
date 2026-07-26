"""Generated from Smithy shape ``com.amazonaws.datazone#RedshiftCredentialConfiguration``."""

from typing_extensions import TypedDict

from capo_datazone.errors import DeserializationError


class RedshiftCredentialConfiguration(TypedDict, closed=True):
    secret_manager_arn: "str"
    """<p>The ARN of a secret manager for an Amazon Redshift cluster.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RedshiftCredentialConfiguration) -> dict:
    out: dict = {}
    out["secretManagerArn"] = value["secret_manager_arn"]
    return out


def deserialize_json(data: dict) -> RedshiftCredentialConfiguration:
    out: RedshiftCredentialConfiguration = {}  # type: ignore[typeddict-item]
    if "secretManagerArn" in data:
        out["secret_manager_arn"] = data["secretManagerArn"]
    else:
        raise DeserializationError(
            "RedshiftCredentialConfiguration.secret_manager_arn required"
        )
    return out
