"""Generated from Smithy shape ``com.amazonaws.ivs#CreateAdConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_ivs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ivs.types.ad_configuration


class CreateAdConfigurationResponse(TypedDict, closed=True):
    ad_configuration: "aws_sdk_ivs.types.ad_configuration.AdConfiguration"
    """<p/>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAdConfigurationResponse) -> dict:
    out: dict = {}
    import aws_sdk_ivs.types.ad_configuration

    out["adConfiguration"] = aws_sdk_ivs.types.ad_configuration.serialize_json(
        value["ad_configuration"]
    )
    return out


def deserialize_json(data: dict) -> CreateAdConfigurationResponse:
    out: CreateAdConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "adConfiguration" in data:
        import aws_sdk_ivs.types.ad_configuration

        out["ad_configuration"] = aws_sdk_ivs.types.ad_configuration.deserialize_json(
            data["adConfiguration"]
        )
    else:
        raise DeserializationError(
            "CreateAdConfigurationResponse.ad_configuration required"
        )
    return out
