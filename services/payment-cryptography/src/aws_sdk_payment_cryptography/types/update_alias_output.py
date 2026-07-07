"""Generated from Smithy shape ``com.amazonaws.paymentcryptography#UpdateAliasOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_payment_cryptography.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_payment_cryptography.types.alias


class UpdateAliasOutput(TypedDict, closed=True):
    alias: "aws_sdk_payment_cryptography.types.alias.Alias"
    """<p>The alias name.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateAliasOutput) -> dict:
    out: dict = {}
    import aws_sdk_payment_cryptography.types.alias

    out["Alias"] = aws_sdk_payment_cryptography.types.alias.serialize_aws_json_1_0(
        value["alias"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateAliasOutput:
    out: UpdateAliasOutput = {}  # type: ignore[typeddict-item]
    if "Alias" in data:
        import aws_sdk_payment_cryptography.types.alias

        out["alias"] = (
            aws_sdk_payment_cryptography.types.alias.deserialize_aws_json_1_0(
                data["Alias"]
            )
        )
    else:
        raise DeserializationError("UpdateAliasOutput.alias required")
    return out
