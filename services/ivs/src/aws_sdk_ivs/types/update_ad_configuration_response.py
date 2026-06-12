"""Generated from Smithy shape ``com.amazonaws.ivs#UpdateAdConfigurationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_ivs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ivs.types.ad_configuration


class UpdateAdConfigurationResponse(TypedDict):
    ad_configuration: "aws_sdk_ivs.types.ad_configuration.AdConfiguration"
    """<p>Object specifying the updated ad configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAdConfigurationResponse) -> dict:
    out: dict = {}
    import aws_sdk_ivs.types.ad_configuration

    out["adConfiguration"] = aws_sdk_ivs.types.ad_configuration.serialize_json(
        value["ad_configuration"]
    )
    return out


def deserialize_json(data: dict) -> UpdateAdConfigurationResponse:
    out: UpdateAdConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "adConfiguration" in data:
        import aws_sdk_ivs.types.ad_configuration

        out["ad_configuration"] = aws_sdk_ivs.types.ad_configuration.deserialize_json(
            data["adConfiguration"]
        )
    else:
        raise DeserializationError(
            "UpdateAdConfigurationResponse.ad_configuration required"
        )
    return out
