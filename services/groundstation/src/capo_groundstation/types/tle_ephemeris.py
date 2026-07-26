"""Generated from Smithy shape ``com.amazonaws.groundstation#TLEEphemeris``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_groundstation.types.s3_object
    import capo_groundstation.types.tle_data_list


class TLEEphemeris(TypedDict, closed=True):
    s3_object: NotRequired["capo_groundstation.types.s3_object.S3Object"]
    """<p>The Amazon S3 object that contains the ephemeris data.</p>"""
    tle_data: NotRequired["capo_groundstation.types.tle_data_list.TLEDataList"]
    """<p>TLE data that you provide directly instead of using an Amazon S3 object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TLEEphemeris) -> dict:
    out: dict = {}
    if "s3_object" in value:
        import capo_groundstation.types.s3_object

        out["s3Object"] = capo_groundstation.types.s3_object.serialize_json(
            value["s3_object"]
        )
    if "tle_data" in value:
        import capo_groundstation.types.tle_data_list

        out["tleData"] = capo_groundstation.types.tle_data_list.serialize_json(
            value["tle_data"]
        )
    return out


def deserialize_json(data: dict) -> TLEEphemeris:
    out: TLEEphemeris = {}  # type: ignore[typeddict-item]
    if "s3Object" in data:
        import capo_groundstation.types.s3_object

        out["s3_object"] = capo_groundstation.types.s3_object.deserialize_json(
            data["s3Object"]
        )
    if "tleData" in data:
        import capo_groundstation.types.tle_data_list

        out["tle_data"] = capo_groundstation.types.tle_data_list.deserialize_json(
            data["tleData"]
        )
    return out
