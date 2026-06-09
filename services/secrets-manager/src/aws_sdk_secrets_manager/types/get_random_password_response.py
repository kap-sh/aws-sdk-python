"""Generated from Smithy shape ``com.amazonaws.secretsmanager#GetRandomPasswordResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_secrets_manager.types.random_password_type


class GetRandomPasswordResponse(TypedDict):
    random_password: NotRequired[
        "aws_sdk_secrets_manager.types.random_password_type.RandomPasswordType"
    ]
    """<p>A string with the password.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetRandomPasswordResponse) -> dict:
    out: dict = {}
    if "random_password" in value:
        out["RandomPassword"] = value["random_password"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetRandomPasswordResponse:
    out: GetRandomPasswordResponse = {}  # type: ignore[typeddict-item]
    if "RandomPassword" in data:
        out["random_password"] = data["RandomPassword"]
    return out
