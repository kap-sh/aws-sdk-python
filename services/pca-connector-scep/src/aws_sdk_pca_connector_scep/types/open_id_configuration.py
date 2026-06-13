"""Generated from Smithy shape ``com.amazonaws.pcaconnectorscep#OpenIdConfiguration``."""

from typing import TypedDict

from typing_extensions import NotRequired


class OpenIdConfiguration(TypedDict):
    issuer: NotRequired["str"]
    """<p>The issuer value to copy into your Microsoft Entra app registration's OIDC.</p>"""
    subject: NotRequired["str"]
    """<p>The subject value to copy into your Microsoft Entra app registration's OIDC.</p>"""
    audience: NotRequired["str"]
    """<p>The audience value to copy into your Microsoft Entra app registration's OIDC.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OpenIdConfiguration) -> dict:
    out: dict = {}
    if "issuer" in value:
        out["Issuer"] = value["issuer"]
    if "subject" in value:
        out["Subject"] = value["subject"]
    if "audience" in value:
        out["Audience"] = value["audience"]
    return out


def deserialize_json(data: dict) -> OpenIdConfiguration:
    out: OpenIdConfiguration = {}  # type: ignore[typeddict-item]
    if "Issuer" in data:
        out["issuer"] = data["Issuer"]
    if "Subject" in data:
        out["subject"] = data["Subject"]
    if "Audience" in data:
        out["audience"] = data["Audience"]
    return out
