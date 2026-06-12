"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancing#CreateLBCookieStickinessPolicyOutput``."""

from typing import TypedDict

from aws_sdk_elastic_load_balancing._protocol.xml import Element


class CreateLBCookieStickinessPolicyOutput(TypedDict):
    pass


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateLBCookieStickinessPolicyOutput,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    pass


def deserialize_query(el: Element) -> CreateLBCookieStickinessPolicyOutput:
    out: CreateLBCookieStickinessPolicyOutput = {}  # type: ignore[typeddict-item]
    return out
