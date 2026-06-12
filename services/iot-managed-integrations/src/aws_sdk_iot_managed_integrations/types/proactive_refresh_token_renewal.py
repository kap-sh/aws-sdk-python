"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#ProactiveRefreshTokenRenewal``."""

from typing import TypedDict

from typing_extensions import NotRequired


class ProactiveRefreshTokenRenewal(TypedDict):
    enabled: NotRequired["bool"]
    """<p>Indicates whether proactive refresh token renewal is enabled.</p>"""
    days_before_renewal: NotRequired["int"]
    """<p>The days before token expiration when the system should attempt to renew the token, specified in days.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProactiveRefreshTokenRenewal) -> dict:
    out: dict = {}
    if "enabled" in value:
        out["enabled"] = value["enabled"]
    if "days_before_renewal" in value:
        out["DaysBeforeRenewal"] = value["days_before_renewal"]
    return out


def deserialize_json(data: dict) -> ProactiveRefreshTokenRenewal:
    out: ProactiveRefreshTokenRenewal = {}  # type: ignore[typeddict-item]
    if "enabled" in data:
        out["enabled"] = data["enabled"]
    if "DaysBeforeRenewal" in data:
        out["days_before_renewal"] = data["DaysBeforeRenewal"]
    return out
