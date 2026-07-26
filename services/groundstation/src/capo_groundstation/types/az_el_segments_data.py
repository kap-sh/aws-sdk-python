"""Generated from Smithy shape ``com.amazonaws.groundstation#AzElSegmentsData``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_groundstation.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_groundstation.types.az_el_segments
    import capo_groundstation.types.s3_object


class _AzElSegmentsData_s3Object(TypedDict, closed=True):
    s3Object: "capo_groundstation.types.s3_object.S3Object"


class _AzElSegmentsData_azElData(TypedDict, closed=True):
    azElData: "capo_groundstation.types.az_el_segments.AzElSegments"


AzElSegmentsData: TypeAlias = _AzElSegmentsData_s3Object | _AzElSegmentsData_azElData


# --- restJson1 ser/de ---
def serialize_json(value: AzElSegmentsData) -> dict:
    if "s3Object" in value:
        import capo_groundstation.types.s3_object

        return {
            "s3Object": capo_groundstation.types.s3_object.serialize_json(
                value["s3Object"]
            )
        }
    elif "azElData" in value:
        import capo_groundstation.types.az_el_segments

        return {
            "azElData": capo_groundstation.types.az_el_segments.serialize_json(
                value["azElData"]
            )
        }
    else:
        raise SerializationError("AzElSegmentsData: no variant present")


def deserialize_json(data: dict) -> AzElSegmentsData:
    if "s3Object" in data:
        import capo_groundstation.types.s3_object

        return {
            "s3Object": capo_groundstation.types.s3_object.deserialize_json(
                data["s3Object"]
            )
        }
    elif "azElData" in data:
        import capo_groundstation.types.az_el_segments

        return {
            "azElData": capo_groundstation.types.az_el_segments.deserialize_json(
                data["azElData"]
            )
        }
    else:
        raise DeserializationError("AzElSegmentsData: no recognized variant key")
