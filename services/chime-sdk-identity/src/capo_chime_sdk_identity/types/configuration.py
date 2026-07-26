"""Generated from Smithy shape ``com.amazonaws.chimesdkidentity#Configuration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_chime_sdk_identity.errors import DeserializationError

if TYPE_CHECKING:
    import capo_chime_sdk_identity.types.lex_configuration


class Configuration(TypedDict, closed=True):
    lex: "capo_chime_sdk_identity.types.lex_configuration.LexConfiguration"
    """<p>The configuration for an Amazon Lex V2 bot.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Configuration) -> dict:
    out: dict = {}
    import capo_chime_sdk_identity.types.lex_configuration

    out["Lex"] = capo_chime_sdk_identity.types.lex_configuration.serialize_json(
        value["lex"]
    )
    return out


def deserialize_json(data: dict) -> Configuration:
    out: Configuration = {}  # type: ignore[typeddict-item]
    if "Lex" in data:
        import capo_chime_sdk_identity.types.lex_configuration

        out["lex"] = capo_chime_sdk_identity.types.lex_configuration.deserialize_json(
            data["Lex"]
        )
    else:
        raise DeserializationError("Configuration.lex required")
    return out
