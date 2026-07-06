"""Generated from Smithy shape ``com.amazonaws.groundstation#CreateEphemerisRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_groundstation.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_groundstation.types.customer_ephemeris_priority
    import aws_sdk_groundstation.types.ephemeris_data
    import aws_sdk_groundstation.types.key_arn
    import aws_sdk_groundstation.types.safe_name
    import aws_sdk_groundstation.types.tags_map
    import aws_sdk_groundstation.types.uuid


class CreateEphemerisRequest(TypedDict, closed=True):
    satellite_id: NotRequired["aws_sdk_groundstation.types.uuid.Uuid"]
    """<p>The satellite ID that associates this ephemeris with a satellite in AWS Ground Station.</p>"""
    enabled: NotRequired["bool"]
    """<p>Set to <code>true</code> to enable the ephemeris after validation. Set to <code>false</code> to keep it disabled.</p>"""
    priority: NotRequired[
        "aws_sdk_groundstation.types.customer_ephemeris_priority.CustomerEphemerisPriority"
    ]
    """<p>A priority score that determines which ephemeris to use when multiple ephemerides overlap.</p> <p>Higher numbers take precedence. The default is 1. Must be 1 or greater.</p>"""
    expiration_time: NotRequired["datetime.datetime"]
    """<p>An overall expiration time for the ephemeris in UTC, after which it will become <code>EXPIRED</code>.</p>"""
    name: "aws_sdk_groundstation.types.safe_name.SafeName"
    """<p>A name that you can use to identify the ephemeris.</p>"""
    kms_key_arn: NotRequired["aws_sdk_groundstation.types.key_arn.KeyArn"]
    """<p>The ARN of the KMS key to use for encrypting the ephemeris.</p>"""
    ephemeris: NotRequired["aws_sdk_groundstation.types.ephemeris_data.EphemerisData"]
    """<p>Ephemeris data.</p>"""
    tags: NotRequired["aws_sdk_groundstation.types.tags_map.TagsMap"]
    """<p>Tags assigned to an ephemeris.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateEphemerisRequest) -> dict:
    out: dict = {}
    if "satellite_id" in value:
        out["satelliteId"] = value["satellite_id"]
    if "enabled" in value:
        out["enabled"] = value["enabled"]
    if "priority" in value:
        out["priority"] = value["priority"]
    if "expiration_time" in value:
        import aws_sdk_groundstation.types._prelude.timestamp

        out["expirationTime"] = (
            aws_sdk_groundstation.types._prelude.timestamp.serialize_json(
                value["expiration_time"]
            )
        )
    out["name"] = value["name"]
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    if "ephemeris" in value:
        import aws_sdk_groundstation.types.ephemeris_data

        out["ephemeris"] = aws_sdk_groundstation.types.ephemeris_data.serialize_json(
            value["ephemeris"]
        )
    if "tags" in value:
        import aws_sdk_groundstation.types.tags_map

        out["tags"] = aws_sdk_groundstation.types.tags_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateEphemerisRequest:
    out: CreateEphemerisRequest = {}  # type: ignore[typeddict-item]
    if "satelliteId" in data:
        out["satellite_id"] = data["satelliteId"]
    if "enabled" in data:
        out["enabled"] = data["enabled"]
    if "priority" in data:
        out["priority"] = data["priority"]
    if "expirationTime" in data:
        import aws_sdk_groundstation.types._prelude.timestamp

        out["expiration_time"] = (
            aws_sdk_groundstation.types._prelude.timestamp.deserialize_json(
                data["expirationTime"]
            )
        )
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateEphemerisRequest.name required")
    if "kmsKeyArn" in data:
        out["kms_key_arn"] = data["kmsKeyArn"]
    if "ephemeris" in data:
        import aws_sdk_groundstation.types.ephemeris_data

        out["ephemeris"] = aws_sdk_groundstation.types.ephemeris_data.deserialize_json(
            data["ephemeris"]
        )
    if "tags" in data:
        import aws_sdk_groundstation.types.tags_map

        out["tags"] = aws_sdk_groundstation.types.tags_map.deserialize_json(
            data["tags"]
        )
    return out
