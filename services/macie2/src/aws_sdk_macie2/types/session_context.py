"""Generated from Smithy shape ``com.amazonaws.macie2#SessionContext``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_macie2.types.session_context_attributes
    import aws_sdk_macie2.types.session_issuer


class SessionContext(TypedDict, closed=True):
    attributes: NotRequired[
        "aws_sdk_macie2.types.session_context_attributes.SessionContextAttributes"
    ]
    """<p>The date and time when the credentials were issued, and whether the credentials were authenticated with a multi-factor authentication (MFA) device.</p>"""
    session_issuer: NotRequired["aws_sdk_macie2.types.session_issuer.SessionIssuer"]
    """<p>The source and type of credentials that were issued to the entity.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SessionContext) -> dict:
    out: dict = {}
    if "attributes" in value:
        import aws_sdk_macie2.types.session_context_attributes

        out["attributes"] = (
            aws_sdk_macie2.types.session_context_attributes.serialize_json(
                value["attributes"]
            )
        )
    if "session_issuer" in value:
        import aws_sdk_macie2.types.session_issuer

        out["sessionIssuer"] = aws_sdk_macie2.types.session_issuer.serialize_json(
            value["session_issuer"]
        )
    return out


def deserialize_json(data: dict) -> SessionContext:
    out: SessionContext = {}  # type: ignore[typeddict-item]
    if "attributes" in data:
        import aws_sdk_macie2.types.session_context_attributes

        out["attributes"] = (
            aws_sdk_macie2.types.session_context_attributes.deserialize_json(
                data["attributes"]
            )
        )
    if "sessionIssuer" in data:
        import aws_sdk_macie2.types.session_issuer

        out["session_issuer"] = aws_sdk_macie2.types.session_issuer.deserialize_json(
            data["sessionIssuer"]
        )
    return out
