"""Generated from Smithy shape ``com.amazonaws.wafv2#GetDecryptedAPIKeyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wafv2.types.timestamp
    import capo_wafv2.types.token_domains


class GetDecryptedAPIKeyResponse(TypedDict, closed=True):
    token_domains: NotRequired["capo_wafv2.types.token_domains.TokenDomains"]
    """<p>The token domains that are defined in this API key. </p>"""
    creation_timestamp: NotRequired["capo_wafv2.types.timestamp.Timestamp"]
    """<p>The date and time that the key was created. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDecryptedAPIKeyResponse) -> dict:
    out: dict = {}
    if "token_domains" in value:
        import capo_wafv2.types.token_domains

        out["TokenDomains"] = capo_wafv2.types.token_domains.serialize_aws_json_1_1(
            value["token_domains"]
        )
    if "creation_timestamp" in value:
        import capo_wafv2.types.timestamp

        out["CreationTimestamp"] = capo_wafv2.types.timestamp.serialize_aws_json_1_1(
            value["creation_timestamp"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDecryptedAPIKeyResponse:
    out: GetDecryptedAPIKeyResponse = {}  # type: ignore[typeddict-item]
    if "TokenDomains" in data:
        import capo_wafv2.types.token_domains

        out["token_domains"] = capo_wafv2.types.token_domains.deserialize_aws_json_1_1(
            data["TokenDomains"]
        )
    if "CreationTimestamp" in data:
        import capo_wafv2.types.timestamp

        out["creation_timestamp"] = capo_wafv2.types.timestamp.deserialize_aws_json_1_1(
            data["CreationTimestamp"]
        )
    return out
