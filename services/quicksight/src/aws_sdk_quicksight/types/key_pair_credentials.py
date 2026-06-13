"""Generated from Smithy shape ``com.amazonaws.quicksight#KeyPairCredentials``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.db_username
    import aws_sdk_quicksight.types.private_key
    import aws_sdk_quicksight.types.private_key_passphrase


class KeyPairCredentials(TypedDict):
    key_pair_username: "aws_sdk_quicksight.types.db_username.DbUsername"
    """<p>Username</p>"""
    private_key: "aws_sdk_quicksight.types.private_key.PrivateKey"
    """<p>PrivateKey</p>"""
    private_key_passphrase: NotRequired[
        "aws_sdk_quicksight.types.private_key_passphrase.PrivateKeyPassphrase"
    ]
    """<p>PrivateKeyPassphrase</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KeyPairCredentials) -> dict:
    out: dict = {}
    out["KeyPairUsername"] = value["key_pair_username"]
    out["PrivateKey"] = value["private_key"]
    if "private_key_passphrase" in value:
        out["PrivateKeyPassphrase"] = value["private_key_passphrase"]
    return out


def deserialize_json(data: dict) -> KeyPairCredentials:
    out: KeyPairCredentials = {}  # type: ignore[typeddict-item]
    if "KeyPairUsername" in data:
        out["key_pair_username"] = data["KeyPairUsername"]
    else:
        raise DeserializationError("KeyPairCredentials.key_pair_username required")
    if "PrivateKey" in data:
        out["private_key"] = data["PrivateKey"]
    else:
        raise DeserializationError("KeyPairCredentials.private_key required")
    if "PrivateKeyPassphrase" in data:
        out["private_key_passphrase"] = data["PrivateKeyPassphrase"]
    return out
