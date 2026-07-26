"""Generated from Smithy shape ``com.amazonaws.appmesh#HttpRetryPolicyEvents``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_app_mesh.types.http_retry_policy_event

HttpRetryPolicyEvents: TypeAlias = list[
    "capo_app_mesh.types.http_retry_policy_event.HttpRetryPolicyEvent"
]


# --- restJson1 ser/de ---
def serialize_json(value: HttpRetryPolicyEvents) -> list:
    return list(value)


def deserialize_json(data: list) -> HttpRetryPolicyEvents:
    return list(data)
