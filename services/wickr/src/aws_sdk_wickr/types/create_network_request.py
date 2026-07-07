"""Generated from Smithy shape ``com.amazonaws.wickr#CreateNetworkRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_wickr.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_wickr.types.access_level
    import aws_sdk_wickr.types.generic_string


class CreateNetworkRequest(TypedDict, closed=True):
    network_name: "aws_sdk_wickr.types.generic_string.GenericString"
    """<p>The name for the new network. Must be between 1 and 20 characters.</p>"""
    access_level: "aws_sdk_wickr.types.access_level.AccessLevel"
    """<p>The access level for the network. Valid values are STANDARD or PREMIUM, which determine the features and capabilities available to network members.</p>"""
    enable_premium_free_trial: NotRequired["bool"]
    """<p>Specifies whether to enable a premium free trial for the network. It is optional and has a default value as false. When set to true, the network starts with premium features for a limited trial period. </p>"""
    encryption_key_arn: NotRequired["aws_sdk_wickr.types.generic_string.GenericString"]
    """<p>The ARN of the Amazon Web Services KMS customer managed key to use for encrypting sensitive data in the network.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateNetworkRequest) -> dict:
    out: dict = {}
    out["networkName"] = value["network_name"]
    import aws_sdk_wickr.types.access_level

    out["accessLevel"] = aws_sdk_wickr.types.access_level.serialize_json(
        value["access_level"]
    )
    if "enable_premium_free_trial" in value:
        out["enablePremiumFreeTrial"] = value["enable_premium_free_trial"]
    if "encryption_key_arn" in value:
        out["encryptionKeyArn"] = value["encryption_key_arn"]
    return out


def deserialize_json(data: dict) -> CreateNetworkRequest:
    out: CreateNetworkRequest = {}  # type: ignore[typeddict-item]
    if "networkName" in data:
        out["network_name"] = data["networkName"]
    else:
        raise DeserializationError("CreateNetworkRequest.network_name required")
    if "accessLevel" in data:
        import aws_sdk_wickr.types.access_level

        out["access_level"] = aws_sdk_wickr.types.access_level.deserialize_json(
            data["accessLevel"]
        )
    else:
        raise DeserializationError("CreateNetworkRequest.access_level required")
    if "enablePremiumFreeTrial" in data:
        out["enable_premium_free_trial"] = data["enablePremiumFreeTrial"]
    if "encryptionKeyArn" in data:
        out["encryption_key_arn"] = data["encryptionKeyArn"]
    return out
