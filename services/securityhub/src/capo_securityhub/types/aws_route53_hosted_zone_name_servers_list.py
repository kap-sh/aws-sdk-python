"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsRoute53HostedZoneNameServersList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string

AwsRoute53HostedZoneNameServersList: TypeAlias = list[
    "capo_securityhub.types.non_empty_string.NonEmptyString"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsRoute53HostedZoneNameServersList) -> list:
    return list(value)


def deserialize_json(data: list) -> AwsRoute53HostedZoneNameServersList:
    return list(data)
