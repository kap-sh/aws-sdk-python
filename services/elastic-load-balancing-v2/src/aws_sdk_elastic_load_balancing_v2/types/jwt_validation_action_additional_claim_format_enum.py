"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#JwtValidationActionAdditionalClaimFormatEnum``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_elastic_load_balancing_v2._protocol.xml import Element

JwtValidationActionAdditionalClaimFormatEnum: TypeAlias = Literal[
    "single-string",
    "string-array",
    "space-separated-values",
]


# --- awsQuery ser/de ---
def to_query_text(value: JwtValidationActionAdditionalClaimFormatEnum) -> str:
    return value


def from_query_text(text: str) -> JwtValidationActionAdditionalClaimFormatEnum:
    return cast(JwtValidationActionAdditionalClaimFormatEnum, text)


def serialize_query(
    value: JwtValidationActionAdditionalClaimFormatEnum,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> JwtValidationActionAdditionalClaimFormatEnum:
    return from_query_text(el.text or "")
