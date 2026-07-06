"""Generated from Smithy shape ``com.amazonaws.chimesdkidentity#AppInstanceAdminSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_identity.types.identity


class AppInstanceAdminSummary(TypedDict, closed=True):
    admin: NotRequired["aws_sdk_chime_sdk_identity.types.identity.Identity"]
    """<p>The details of the <code>AppInstanceAdmin</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AppInstanceAdminSummary) -> dict:
    out: dict = {}
    if "admin" in value:
        import aws_sdk_chime_sdk_identity.types.identity

        out["Admin"] = aws_sdk_chime_sdk_identity.types.identity.serialize_json(
            value["admin"]
        )
    return out


def deserialize_json(data: dict) -> AppInstanceAdminSummary:
    out: AppInstanceAdminSummary = {}  # type: ignore[typeddict-item]
    if "Admin" in data:
        import aws_sdk_chime_sdk_identity.types.identity

        out["admin"] = aws_sdk_chime_sdk_identity.types.identity.deserialize_json(
            data["Admin"]
        )
    return out
