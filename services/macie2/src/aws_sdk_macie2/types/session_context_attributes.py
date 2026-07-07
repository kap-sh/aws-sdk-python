"""Generated from Smithy shape ``com.amazonaws.macie2#SessionContextAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__boolean
    import aws_sdk_macie2.types.__timestamp_iso8601


class SessionContextAttributes(TypedDict, closed=True):
    creation_date: NotRequired[
        "aws_sdk_macie2.types.__timestamp_iso8601.__timestampIso8601"
    ]
    """<p>The date and time, in UTC and ISO 8601 format, when the credentials were issued.</p>"""
    mfa_authenticated: NotRequired["aws_sdk_macie2.types.__boolean.__boolean"]
    """<p>Specifies whether the credentials were authenticated with a multi-factor authentication (MFA) device.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SessionContextAttributes) -> dict:
    out: dict = {}
    if "creation_date" in value:
        import aws_sdk_macie2.types.__timestamp_iso8601

        out["creationDate"] = aws_sdk_macie2.types.__timestamp_iso8601.serialize_json(
            value["creation_date"]
        )
    if "mfa_authenticated" in value:
        out["mfaAuthenticated"] = value["mfa_authenticated"]
    return out


def deserialize_json(data: dict) -> SessionContextAttributes:
    out: SessionContextAttributes = {}  # type: ignore[typeddict-item]
    if "creationDate" in data:
        import aws_sdk_macie2.types.__timestamp_iso8601

        out["creation_date"] = (
            aws_sdk_macie2.types.__timestamp_iso8601.deserialize_json(
                data["creationDate"]
            )
        )
    if "mfaAuthenticated" in data:
        out["mfa_authenticated"] = data["mfaAuthenticated"]
    return out
