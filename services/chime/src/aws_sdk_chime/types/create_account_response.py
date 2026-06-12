"""Generated from Smithy shape ``com.amazonaws.chime#CreateAccountResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_chime.types.account


class CreateAccountResponse(TypedDict):
    account: NotRequired["aws_sdk_chime.types.account.Account"]
    """<p>The Amazon Chime account details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAccountResponse) -> dict:
    out: dict = {}
    if "account" in value:
        import aws_sdk_chime.types.account

        out["Account"] = aws_sdk_chime.types.account.serialize_json(value["account"])
    return out


def deserialize_json(data: dict) -> CreateAccountResponse:
    out: CreateAccountResponse = {}  # type: ignore[typeddict-item]
    if "Account" in data:
        import aws_sdk_chime.types.account

        out["account"] = aws_sdk_chime.types.account.deserialize_json(data["Account"])
    return out
