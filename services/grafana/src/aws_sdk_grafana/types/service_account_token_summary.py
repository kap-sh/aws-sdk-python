"""Generated from Smithy shape ``com.amazonaws.grafana#ServiceAccountTokenSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_grafana.errors import DeserializationError

if TYPE_CHECKING:
    import datetime


class ServiceAccountTokenSummary(TypedDict, closed=True):
    id: "str"
    """<p>The unique ID of the service account token.</p>"""
    name: "str"
    """<p>The name of the service account token.</p>"""
    created_at: "datetime.datetime"
    """<p>When the service account token was created.</p>"""
    expires_at: "datetime.datetime"
    """<p>When the service account token will expire.</p>"""
    last_used_at: NotRequired["datetime.datetime"]
    """<p>The last time the token was used to authorize a Grafana HTTP API.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceAccountTokenSummary) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["name"] = value["name"]
    import aws_sdk_grafana.types._prelude.timestamp

    out["createdAt"] = aws_sdk_grafana.types._prelude.timestamp.serialize_json(
        value["created_at"]
    )
    import aws_sdk_grafana.types._prelude.timestamp

    out["expiresAt"] = aws_sdk_grafana.types._prelude.timestamp.serialize_json(
        value["expires_at"]
    )
    if "last_used_at" in value:
        import aws_sdk_grafana.types._prelude.timestamp

        out["lastUsedAt"] = aws_sdk_grafana.types._prelude.timestamp.serialize_json(
            value["last_used_at"]
        )
    return out


def deserialize_json(data: dict) -> ServiceAccountTokenSummary:
    out: ServiceAccountTokenSummary = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("ServiceAccountTokenSummary.id required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("ServiceAccountTokenSummary.name required")
    if "createdAt" in data:
        import aws_sdk_grafana.types._prelude.timestamp

        out["created_at"] = aws_sdk_grafana.types._prelude.timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("ServiceAccountTokenSummary.created_at required")
    if "expiresAt" in data:
        import aws_sdk_grafana.types._prelude.timestamp

        out["expires_at"] = aws_sdk_grafana.types._prelude.timestamp.deserialize_json(
            data["expiresAt"]
        )
    else:
        raise DeserializationError("ServiceAccountTokenSummary.expires_at required")
    if "lastUsedAt" in data:
        import aws_sdk_grafana.types._prelude.timestamp

        out["last_used_at"] = aws_sdk_grafana.types._prelude.timestamp.deserialize_json(
            data["lastUsedAt"]
        )
    return out
