"""Generated from Smithy shape ``com.amazonaws.route53resolver#DnsThreatProtection``."""

from typing import Literal, TypeAlias, cast

DnsThreatProtection: TypeAlias = Literal[
    "DGA",
    "DNS_TUNNELING",
    "DICTIONARY_DGA",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DnsThreatProtection) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DnsThreatProtection:
    return cast(DnsThreatProtection, data)
