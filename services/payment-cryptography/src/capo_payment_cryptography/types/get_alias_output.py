"""Generated from Smithy shape ``com.amazonaws.paymentcryptography#GetAliasOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_payment_cryptography.errors import DeserializationError

if TYPE_CHECKING:
    import capo_payment_cryptography.types.alias


class GetAliasOutput(TypedDict, closed=True):
    alias: "capo_payment_cryptography.types.alias.Alias"
    """<p>The alias of the Amazon Web Services Payment Cryptography key.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetAliasOutput) -> dict:
    out: dict = {}
    import capo_payment_cryptography.types.alias

    out["Alias"] = capo_payment_cryptography.types.alias.serialize_aws_json_1_0(
        value["alias"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetAliasOutput:
    out: GetAliasOutput = {}  # type: ignore[typeddict-item]
    if "Alias" in data:
        import capo_payment_cryptography.types.alias

        out["alias"] = capo_payment_cryptography.types.alias.deserialize_aws_json_1_0(
            data["Alias"]
        )
    else:
        raise DeserializationError("GetAliasOutput.alias required")
    return out
