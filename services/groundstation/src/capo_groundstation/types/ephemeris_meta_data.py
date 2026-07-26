"""Generated from Smithy shape ``com.amazonaws.groundstation#EphemerisMetaData``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_groundstation.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_groundstation.types.ephemeris_source
    import capo_groundstation.types.safe_name
    import capo_groundstation.types.uuid


class EphemerisMetaData(TypedDict, closed=True):
    source: "capo_groundstation.types.ephemeris_source.EphemerisSource"
    """<p>The <code>EphemerisSource</code> that generated a given ephemeris.</p>"""
    ephemeris_id: NotRequired["capo_groundstation.types.uuid.Uuid"]
    """<p>UUID of a customer-provided ephemeris.</p> <p>This field is not populated for default ephemerides from Space Track.</p>"""
    epoch: NotRequired["datetime.datetime"]
    """<p>The epoch of a default, ephemeris from Space Track in UTC.</p> <p>This field is not populated for customer-provided ephemerides.</p>"""
    name: NotRequired["capo_groundstation.types.safe_name.SafeName"]
    """<p>A name string associated with the ephemeris. Used as a human-readable identifier for the ephemeris.</p> <p>A name is only returned for customer-provider ephemerides that have a name associated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EphemerisMetaData) -> dict:
    out: dict = {}
    import capo_groundstation.types.ephemeris_source

    out["source"] = capo_groundstation.types.ephemeris_source.serialize_json(
        value["source"]
    )
    if "ephemeris_id" in value:
        out["ephemerisId"] = value["ephemeris_id"]
    if "epoch" in value:
        import capo_groundstation.types._prelude.timestamp

        out["epoch"] = capo_groundstation.types._prelude.timestamp.serialize_json(
            value["epoch"]
        )
    if "name" in value:
        out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> EphemerisMetaData:
    out: EphemerisMetaData = {}  # type: ignore[typeddict-item]
    if "source" in data:
        import capo_groundstation.types.ephemeris_source

        out["source"] = capo_groundstation.types.ephemeris_source.deserialize_json(
            data["source"]
        )
    else:
        raise DeserializationError("EphemerisMetaData.source required")
    if "ephemerisId" in data:
        out["ephemeris_id"] = data["ephemerisId"]
    if "epoch" in data:
        import capo_groundstation.types._prelude.timestamp

        out["epoch"] = capo_groundstation.types._prelude.timestamp.deserialize_json(
            data["epoch"]
        )
    if "name" in data:
        out["name"] = data["name"]
    return out
