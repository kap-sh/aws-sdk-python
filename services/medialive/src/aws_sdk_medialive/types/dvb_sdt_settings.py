"""Generated from Smithy shape ``com.amazonaws.medialive#DvbSdtSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__integer_min25_max2000
    import aws_sdk_medialive.types.__string_min1_max256
    import aws_sdk_medialive.types.dvb_sdt_output_sdt


class DvbSdtSettings(TypedDict, closed=True):
    output_sdt: NotRequired[
        "aws_sdk_medialive.types.dvb_sdt_output_sdt.DvbSdtOutputSdt"
    ]
    """Selects method of inserting SDT information into output stream. The sdtFollow setting copies SDT information from input stream to output stream. The sdtFollowIfPresent setting copies SDT information from input stream to output stream if SDT information is present in the input, otherwise it will fall back on the user-defined values. The sdtManual setting means user will enter the SDT information. The sdtNone setting means output stream will not contain SDT information."""
    rep_interval: NotRequired[
        "aws_sdk_medialive.types.__integer_min25_max2000.__integerMin25Max2000"
    ]
    """The number of milliseconds between instances of this table in the output transport stream."""
    service_name: NotRequired[
        "aws_sdk_medialive.types.__string_min1_max256.__stringMin1Max256"
    ]
    """The service name placed in the serviceDescriptor in the Service Description Table. Maximum length is 256 characters."""
    service_provider_name: NotRequired[
        "aws_sdk_medialive.types.__string_min1_max256.__stringMin1Max256"
    ]
    """The service provider name placed in the serviceDescriptor in the Service Description Table. Maximum length is 256 characters."""


# --- restJson1 ser/de ---
def serialize_json(value: DvbSdtSettings) -> dict:
    out: dict = {}
    if "output_sdt" in value:
        import aws_sdk_medialive.types.dvb_sdt_output_sdt

        out["outputSdt"] = aws_sdk_medialive.types.dvb_sdt_output_sdt.serialize_json(
            value["output_sdt"]
        )
    if "rep_interval" in value:
        out["repInterval"] = value["rep_interval"]
    if "service_name" in value:
        out["serviceName"] = value["service_name"]
    if "service_provider_name" in value:
        out["serviceProviderName"] = value["service_provider_name"]
    return out


def deserialize_json(data: dict) -> DvbSdtSettings:
    out: DvbSdtSettings = {}  # type: ignore[typeddict-item]
    if "outputSdt" in data:
        import aws_sdk_medialive.types.dvb_sdt_output_sdt

        out["output_sdt"] = aws_sdk_medialive.types.dvb_sdt_output_sdt.deserialize_json(
            data["outputSdt"]
        )
    if "repInterval" in data:
        out["rep_interval"] = data["repInterval"]
    if "serviceName" in data:
        out["service_name"] = data["serviceName"]
    if "serviceProviderName" in data:
        out["service_provider_name"] = data["serviceProviderName"]
    return out
