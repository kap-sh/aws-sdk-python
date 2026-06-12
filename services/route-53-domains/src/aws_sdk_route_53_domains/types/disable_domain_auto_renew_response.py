"""Generated from Smithy shape ``com.amazonaws.route53domains#DisableDomainAutoRenewResponse``."""

from typing import TypedDict


class DisableDomainAutoRenewResponse(TypedDict):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DisableDomainAutoRenewResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DisableDomainAutoRenewResponse:
    out: DisableDomainAutoRenewResponse = {}  # type: ignore[typeddict-item]
    return out
