"""Generated from Smithy shape ``com.amazonaws.grafana#ServiceAccountTokenSummaryWithKey``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_grafana.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_grafana.types.service_account_token_key


class ServiceAccountTokenSummaryWithKey(TypedDict):
    id: "str"
    """<p>The unique ID of the service account token.</p>"""
    name: "str"
    """<p>The name of the service account token.</p>"""
    key: "aws_sdk_grafana.types.service_account_token_key.ServiceAccountTokenKey"
    """<p>The key for the service account token. Used when making calls to the Grafana HTTP APIs to authenticate and authorize the requests.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceAccountTokenSummaryWithKey) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["name"] = value["name"]
    out["key"] = value["key"]
    return out


def deserialize_json(data: dict) -> ServiceAccountTokenSummaryWithKey:
    out: ServiceAccountTokenSummaryWithKey = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("ServiceAccountTokenSummaryWithKey.id required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("ServiceAccountTokenSummaryWithKey.name required")
    if "key" in data:
        out["key"] = data["key"]
    else:
        raise DeserializationError("ServiceAccountTokenSummaryWithKey.key required")
    return out
