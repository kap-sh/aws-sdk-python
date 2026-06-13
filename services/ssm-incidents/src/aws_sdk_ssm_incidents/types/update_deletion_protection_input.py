"""Generated from Smithy shape ``com.amazonaws.ssmincidents#UpdateDeletionProtectionInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ssm_incidents.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm_incidents.types.arn
    import aws_sdk_ssm_incidents.types.client_token


class UpdateDeletionProtectionInput(TypedDict):
    arn: "aws_sdk_ssm_incidents.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the replication set to update.</p>"""
    deletion_protected: "bool"
    """<p>Specifies if deletion protection is turned on or off in your account. </p>"""
    client_token: NotRequired["aws_sdk_ssm_incidents.types.client_token.ClientToken"]
    """<p>A token that ensures that the operation is called only once with the specified details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDeletionProtectionInput) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["deletionProtected"] = value["deletion_protected"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> UpdateDeletionProtectionInput:
    out: UpdateDeletionProtectionInput = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("UpdateDeletionProtectionInput.arn required")
    if "deletionProtected" in data:
        out["deletion_protected"] = data["deletionProtected"]
    else:
        raise DeserializationError(
            "UpdateDeletionProtectionInput.deletion_protected required"
        )
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
