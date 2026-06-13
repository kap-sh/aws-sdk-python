"""Generated from Smithy shape ``com.amazonaws.drs#ConversionProperties``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_drs.types.large_bounded_string
    import aws_sdk_drs.types.volume_to_conversion_map
    import aws_sdk_drs.types.volume_to_product_codes
    import aws_sdk_drs.types.volume_to_size_map


class ConversionProperties(TypedDict):
    volume_to_conversion_map: NotRequired[
        "aws_sdk_drs.types.volume_to_conversion_map.VolumeToConversionMap"
    ]
    """<p>A mapping between the volumes being converted and the converted snapshot ids</p>"""
    root_volume_name: NotRequired[
        "aws_sdk_drs.types.large_bounded_string.LargeBoundedString"
    ]
    """<p>The root volume name of a conversion job</p>"""
    force_uefi: NotRequired["bool"]
    """<p>Whether the volume being converted uses UEFI or not</p>"""
    data_timestamp: NotRequired[
        "aws_sdk_drs.types.large_bounded_string.LargeBoundedString"
    ]
    """<p>The timestamp of when the snapshot being converted was taken</p>"""
    volume_to_volume_size: NotRequired[
        "aws_sdk_drs.types.volume_to_size_map.VolumeToSizeMap"
    ]
    """<p>A mapping between the volumes and their sizes</p>"""
    volume_to_product_codes: NotRequired[
        "aws_sdk_drs.types.volume_to_product_codes.VolumeToProductCodes"
    ]
    """<p>A mapping between the volumes being converted and the product codes associated with them</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConversionProperties) -> dict:
    out: dict = {}
    if "volume_to_conversion_map" in value:
        import aws_sdk_drs.types.volume_to_conversion_map

        out["volumeToConversionMap"] = (
            aws_sdk_drs.types.volume_to_conversion_map.serialize_json(
                value["volume_to_conversion_map"]
            )
        )
    if "root_volume_name" in value:
        out["rootVolumeName"] = value["root_volume_name"]
    if "force_uefi" in value:
        out["forceUefi"] = value["force_uefi"]
    if "data_timestamp" in value:
        out["dataTimestamp"] = value["data_timestamp"]
    if "volume_to_volume_size" in value:
        import aws_sdk_drs.types.volume_to_size_map

        out["volumeToVolumeSize"] = aws_sdk_drs.types.volume_to_size_map.serialize_json(
            value["volume_to_volume_size"]
        )
    if "volume_to_product_codes" in value:
        import aws_sdk_drs.types.volume_to_product_codes

        out["volumeToProductCodes"] = (
            aws_sdk_drs.types.volume_to_product_codes.serialize_json(
                value["volume_to_product_codes"]
            )
        )
    return out


def deserialize_json(data: dict) -> ConversionProperties:
    out: ConversionProperties = {}  # type: ignore[typeddict-item]
    if "volumeToConversionMap" in data:
        import aws_sdk_drs.types.volume_to_conversion_map

        out["volume_to_conversion_map"] = (
            aws_sdk_drs.types.volume_to_conversion_map.deserialize_json(
                data["volumeToConversionMap"]
            )
        )
    if "rootVolumeName" in data:
        out["root_volume_name"] = data["rootVolumeName"]
    if "forceUefi" in data:
        out["force_uefi"] = data["forceUefi"]
    if "dataTimestamp" in data:
        out["data_timestamp"] = data["dataTimestamp"]
    if "volumeToVolumeSize" in data:
        import aws_sdk_drs.types.volume_to_size_map

        out["volume_to_volume_size"] = (
            aws_sdk_drs.types.volume_to_size_map.deserialize_json(
                data["volumeToVolumeSize"]
            )
        )
    if "volumeToProductCodes" in data:
        import aws_sdk_drs.types.volume_to_product_codes

        out["volume_to_product_codes"] = (
            aws_sdk_drs.types.volume_to_product_codes.deserialize_json(
                data["volumeToProductCodes"]
            )
        )
    return out
