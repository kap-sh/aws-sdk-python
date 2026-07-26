"""Generated from Smithy shape ``com.amazonaws.iot#Authorizers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot.types.authorizer_summary

Authorizers: TypeAlias = list["capo_iot.types.authorizer_summary.AuthorizerSummary"]


# --- restJson1 ser/de ---
def serialize_json(value: Authorizers) -> list:
    import capo_iot.types.authorizer_summary

    out: list = []
    for item in value:
        out.append(capo_iot.types.authorizer_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> Authorizers:
    import capo_iot.types.authorizer_summary

    out: Authorizers = []
    for item in data:
        out.append(capo_iot.types.authorizer_summary.deserialize_json(item))
    return out
