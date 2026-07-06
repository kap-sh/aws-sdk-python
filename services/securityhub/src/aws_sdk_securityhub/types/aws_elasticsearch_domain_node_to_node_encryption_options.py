"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsElasticsearchDomainNodeToNodeEncryptionOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.boolean


class AwsElasticsearchDomainNodeToNodeEncryptionOptions(TypedDict, closed=True):
    enabled: NotRequired["aws_sdk_securityhub.types.boolean.Boolean"]
    """<p>Whether node-to-node encryption is enabled.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsElasticsearchDomainNodeToNodeEncryptionOptions) -> dict:
    out: dict = {}
    if "enabled" in value:
        out["Enabled"] = value["enabled"]
    return out


def deserialize_json(data: dict) -> AwsElasticsearchDomainNodeToNodeEncryptionOptions:
    out: AwsElasticsearchDomainNodeToNodeEncryptionOptions = {}  # type: ignore[typeddict-item]
    if "Enabled" in data:
        out["enabled"] = data["Enabled"]
    return out
