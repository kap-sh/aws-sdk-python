"""Generated from Smithy shape ``com.amazonaws.taxsettings#SpainAdditionalInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_taxsettings.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_taxsettings.types.registration_type


class SpainAdditionalInfo(TypedDict, closed=True):
    registration_type: "aws_sdk_taxsettings.types.registration_type.RegistrationType"
    """<p>The registration type in Spain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SpainAdditionalInfo) -> dict:
    out: dict = {}
    import aws_sdk_taxsettings.types.registration_type

    out["registrationType"] = (
        aws_sdk_taxsettings.types.registration_type.serialize_json(
            value["registration_type"]
        )
    )
    return out


def deserialize_json(data: dict) -> SpainAdditionalInfo:
    out: SpainAdditionalInfo = {}  # type: ignore[typeddict-item]
    if "registrationType" in data:
        import aws_sdk_taxsettings.types.registration_type

        out["registration_type"] = (
            aws_sdk_taxsettings.types.registration_type.deserialize_json(
                data["registrationType"]
            )
        )
    else:
        raise DeserializationError("SpainAdditionalInfo.registration_type required")
    return out
