"""Generated from Smithy shape ``com.amazonaws.paymentcryptography#ListAliasesOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_payment_cryptography.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_payment_cryptography.types.aliases
    import aws_sdk_payment_cryptography.types.next_token


class ListAliasesOutput(TypedDict):
    aliases: "aws_sdk_payment_cryptography.types.aliases.Aliases"
    """<p>The list of aliases. Each alias describes the <code>KeyArn</code> contained within.</p>"""
    next_token: NotRequired["aws_sdk_payment_cryptography.types.next_token.NextToken"]
    """<p>The token for the next set of results, or an empty or null value if there are no more results.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListAliasesOutput) -> dict:
    out: dict = {}
    import aws_sdk_payment_cryptography.types.aliases

    out["Aliases"] = aws_sdk_payment_cryptography.types.aliases.serialize_aws_json_1_0(
        value["aliases"]
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListAliasesOutput:
    out: ListAliasesOutput = {}  # type: ignore[typeddict-item]
    if "Aliases" in data:
        import aws_sdk_payment_cryptography.types.aliases

        out["aliases"] = (
            aws_sdk_payment_cryptography.types.aliases.deserialize_aws_json_1_0(
                data["Aliases"]
            )
        )
    else:
        raise DeserializationError("ListAliasesOutput.aliases required")
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
