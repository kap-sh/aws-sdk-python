"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#EmbeddedCryptoWallet``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.crypto_wallet_network
    import aws_sdk_bedrock_agentcore.types.linked_account_list


class EmbeddedCryptoWallet(TypedDict):
    network: "aws_sdk_bedrock_agentcore.types.crypto_wallet_network.CryptoWalletNetwork"
    """<p>The blockchain network for this embedded crypto wallet. Supported networks: ETHEREUM, SOLANA.</p>"""
    linked_accounts: (
        "aws_sdk_bedrock_agentcore.types.linked_account_list.LinkedAccountList"
    )
    """<p>List of linked accounts linked to this wallet. Each represents a way the end user can authenticate to this wallet.</p>"""
    wallet_address: NotRequired["str"]
    """<p>The wallet address on the specified blockchain network.</p>"""
    redirect_url: NotRequired["str"]
    """<p>URL for the end user to complete a provider-specific action such as wallet linking or onboarding.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EmbeddedCryptoWallet) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agentcore.types.crypto_wallet_network

    out["network"] = (
        aws_sdk_bedrock_agentcore.types.crypto_wallet_network.serialize_json(
            value["network"]
        )
    )
    import aws_sdk_bedrock_agentcore.types.linked_account_list

    out["linkedAccounts"] = (
        aws_sdk_bedrock_agentcore.types.linked_account_list.serialize_json(
            value["linked_accounts"]
        )
    )
    if "wallet_address" in value:
        out["walletAddress"] = value["wallet_address"]
    if "redirect_url" in value:
        out["redirectUrl"] = value["redirect_url"]
    return out


def deserialize_json(data: dict) -> EmbeddedCryptoWallet:
    out: EmbeddedCryptoWallet = {}  # type: ignore[typeddict-item]
    if "network" in data:
        import aws_sdk_bedrock_agentcore.types.crypto_wallet_network

        out["network"] = (
            aws_sdk_bedrock_agentcore.types.crypto_wallet_network.deserialize_json(
                data["network"]
            )
        )
    else:
        raise DeserializationError("EmbeddedCryptoWallet.network required")
    if "linkedAccounts" in data:
        import aws_sdk_bedrock_agentcore.types.linked_account_list

        out["linked_accounts"] = (
            aws_sdk_bedrock_agentcore.types.linked_account_list.deserialize_json(
                data["linkedAccounts"]
            )
        )
    else:
        raise DeserializationError("EmbeddedCryptoWallet.linked_accounts required")
    if "walletAddress" in data:
        out["wallet_address"] = data["walletAddress"]
    if "redirectUrl" in data:
        out["redirect_url"] = data["redirectUrl"]
    return out
