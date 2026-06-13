"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#CdnIdentifierSecretArns``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediapackagev2.types.cdn_identifier_secret_arn

CdnIdentifierSecretArns: TypeAlias = list[
    "aws_sdk_mediapackagev2.types.cdn_identifier_secret_arn.CdnIdentifierSecretArn"
]


# --- restJson1 ser/de ---
def serialize_json(value: CdnIdentifierSecretArns) -> list:
    return list(value)


def deserialize_json(data: list) -> CdnIdentifierSecretArns:
    return list(data)
