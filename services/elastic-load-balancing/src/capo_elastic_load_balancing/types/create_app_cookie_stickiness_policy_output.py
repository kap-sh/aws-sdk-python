"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancing#CreateAppCookieStickinessPolicyOutput``."""

from typing_extensions import TypedDict

from capo_elastic_load_balancing._protocol.xml import Element


class CreateAppCookieStickinessPolicyOutput(TypedDict, closed=True):
    pass


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateAppCookieStickinessPolicyOutput,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    pass


def deserialize_query(el: Element) -> CreateAppCookieStickinessPolicyOutput:
    out: CreateAppCookieStickinessPolicyOutput = {}  # type: ignore[typeddict-item]
    return out
