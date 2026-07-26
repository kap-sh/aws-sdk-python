"""Generated from Smithy shape ``com.amazonaws.groundstation#EphemerisItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_groundstation.types.ephemeris_priority
    import capo_groundstation.types.ephemeris_status
    import capo_groundstation.types.ephemeris_type
    import capo_groundstation.types.s3_object
    import capo_groundstation.types.safe_name
    import capo_groundstation.types.uuid


class EphemerisItem(TypedDict, closed=True):
    ephemeris_id: NotRequired["capo_groundstation.types.uuid.Uuid"]
    """<p>The AWS Ground Station ephemeris ID.</p>"""
    ephemeris_type: NotRequired["capo_groundstation.types.ephemeris_type.EphemerisType"]
    """<p>The type of ephemeris.</p>"""
    status: NotRequired["capo_groundstation.types.ephemeris_status.EphemerisStatus"]
    """<p>The status of the ephemeris.</p>"""
    priority: NotRequired[
        "capo_groundstation.types.ephemeris_priority.EphemerisPriority"
    ]
    """<p>A priority score that determines which ephemeris to use when multiple ephemerides overlap.</p> <p>Higher numbers take precedence. The default is 1. Must be 1 or greater.</p>"""
    enabled: NotRequired["bool"]
    """<p>Whether or not the ephemeris is enabled.</p>"""
    creation_time: NotRequired["datetime.datetime"]
    """<p>The time the ephemeris was uploaded in UTC.</p>"""
    name: NotRequired["capo_groundstation.types.safe_name.SafeName"]
    """<p>A name that you can use to identify the ephemeris.</p>"""
    source_s3_object: NotRequired["capo_groundstation.types.s3_object.S3Object"]
    """<p>Source Amazon S3 object used for the ephemeris.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EphemerisItem) -> dict:
    out: dict = {}
    if "ephemeris_id" in value:
        out["ephemerisId"] = value["ephemeris_id"]
    if "ephemeris_type" in value:
        import capo_groundstation.types.ephemeris_type

        out["ephemerisType"] = capo_groundstation.types.ephemeris_type.serialize_json(
            value["ephemeris_type"]
        )
    if "status" in value:
        import capo_groundstation.types.ephemeris_status

        out["status"] = capo_groundstation.types.ephemeris_status.serialize_json(
            value["status"]
        )
    if "priority" in value:
        out["priority"] = value["priority"]
    if "enabled" in value:
        out["enabled"] = value["enabled"]
    if "creation_time" in value:
        import capo_groundstation.types._prelude.timestamp

        out["creationTime"] = (
            capo_groundstation.types._prelude.timestamp.serialize_json(
                value["creation_time"]
            )
        )
    if "name" in value:
        out["name"] = value["name"]
    if "source_s3_object" in value:
        import capo_groundstation.types.s3_object

        out["sourceS3Object"] = capo_groundstation.types.s3_object.serialize_json(
            value["source_s3_object"]
        )
    return out


def deserialize_json(data: dict) -> EphemerisItem:
    out: EphemerisItem = {}  # type: ignore[typeddict-item]
    if "ephemerisId" in data:
        out["ephemeris_id"] = data["ephemerisId"]
    if "ephemerisType" in data:
        import capo_groundstation.types.ephemeris_type

        out["ephemeris_type"] = (
            capo_groundstation.types.ephemeris_type.deserialize_json(
                data["ephemerisType"]
            )
        )
    if "status" in data:
        import capo_groundstation.types.ephemeris_status

        out["status"] = capo_groundstation.types.ephemeris_status.deserialize_json(
            data["status"]
        )
    if "priority" in data:
        out["priority"] = data["priority"]
    if "enabled" in data:
        out["enabled"] = data["enabled"]
    if "creationTime" in data:
        import capo_groundstation.types._prelude.timestamp

        out["creation_time"] = (
            capo_groundstation.types._prelude.timestamp.deserialize_json(
                data["creationTime"]
            )
        )
    if "name" in data:
        out["name"] = data["name"]
    if "sourceS3Object" in data:
        import capo_groundstation.types.s3_object

        out["source_s3_object"] = capo_groundstation.types.s3_object.deserialize_json(
            data["sourceS3Object"]
        )
    return out
