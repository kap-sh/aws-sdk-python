"""Generated from Smithy shape ``com.amazonaws.chimesdkidentity#Configuration``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_chime_sdk_identity.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_identity.types.lex_configuration


class Configuration(TypedDict):
    lex: "aws_sdk_chime_sdk_identity.types.lex_configuration.LexConfiguration"
    """<p>The configuration for an Amazon Lex V2 bot.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Configuration) -> dict:
    out: dict = {}
    import aws_sdk_chime_sdk_identity.types.lex_configuration

    out["Lex"] = aws_sdk_chime_sdk_identity.types.lex_configuration.serialize_json(
        value["lex"]
    )
    return out


def deserialize_json(data: dict) -> Configuration:
    out: Configuration = {}  # type: ignore[typeddict-item]
    if "Lex" in data:
        import aws_sdk_chime_sdk_identity.types.lex_configuration

        out["lex"] = (
            aws_sdk_chime_sdk_identity.types.lex_configuration.deserialize_json(
                data["Lex"]
            )
        )
    else:
        raise DeserializationError("Configuration.lex required")
    return out
