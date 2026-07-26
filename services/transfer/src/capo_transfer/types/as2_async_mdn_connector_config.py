"""Generated from Smithy shape ``com.amazonaws.transfer#As2AsyncMdnConnectorConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_transfer.types.as2_async_mdn_server_ids
    import capo_transfer.types.url


class As2AsyncMdnConnectorConfig(TypedDict, closed=True):
    url: NotRequired["capo_transfer.types.url.Url"]
    """<p>The URL endpoint where asynchronous MDN responses should be sent.</p>"""
    server_ids: NotRequired[
        "capo_transfer.types.as2_async_mdn_server_ids.As2AsyncMdnServerIds"
    ]
    """<p>A list of server identifiers that can handle asynchronous MDN responses. You can specify between 1 and 10 server IDs.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: As2AsyncMdnConnectorConfig) -> dict:
    out: dict = {}
    if "url" in value:
        out["Url"] = value["url"]
    if "server_ids" in value:
        import capo_transfer.types.as2_async_mdn_server_ids

        out["ServerIds"] = (
            capo_transfer.types.as2_async_mdn_server_ids.serialize_aws_json_1_1(
                value["server_ids"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> As2AsyncMdnConnectorConfig:
    out: As2AsyncMdnConnectorConfig = {}  # type: ignore[typeddict-item]
    if "Url" in data:
        out["url"] = data["Url"]
    if "ServerIds" in data:
        import capo_transfer.types.as2_async_mdn_server_ids

        out["server_ids"] = (
            capo_transfer.types.as2_async_mdn_server_ids.deserialize_aws_json_1_1(
                data["ServerIds"]
            )
        )
    return out
