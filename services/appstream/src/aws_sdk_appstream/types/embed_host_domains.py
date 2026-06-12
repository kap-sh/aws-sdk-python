"""Generated from Smithy shape ``com.amazonaws.appstream#EmbedHostDomains``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_appstream.types.embed_host_domain

EmbedHostDomains: TypeAlias = list[
    "aws_sdk_appstream.types.embed_host_domain.EmbedHostDomain"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EmbedHostDomains) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> EmbedHostDomains:
    return list(data)
