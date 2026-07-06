"""Generated from Smithy shape ``com.amazonaws.ivs#GetAdConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ivs.types.ad_configuration


class GetAdConfigurationResponse(TypedDict, closed=True):
    ad_configuration: NotRequired["aws_sdk_ivs.types.ad_configuration.AdConfiguration"]
    """<p/>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAdConfigurationResponse) -> dict:
    out: dict = {}
    if "ad_configuration" in value:
        import aws_sdk_ivs.types.ad_configuration

        out["adConfiguration"] = aws_sdk_ivs.types.ad_configuration.serialize_json(
            value["ad_configuration"]
        )
    return out


def deserialize_json(data: dict) -> GetAdConfigurationResponse:
    out: GetAdConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "adConfiguration" in data:
        import aws_sdk_ivs.types.ad_configuration

        out["ad_configuration"] = aws_sdk_ivs.types.ad_configuration.deserialize_json(
            data["adConfiguration"]
        )
    return out
