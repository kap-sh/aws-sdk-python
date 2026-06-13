"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#AudienceDestination``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cleanroomsml.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanroomsml.types.s3_config_map


class AudienceDestination(TypedDict):
    s3_destination: "aws_sdk_cleanroomsml.types.s3_config_map.S3ConfigMap"
    """<p>The Amazon S3 bucket and path for the configured audience.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AudienceDestination) -> dict:
    out: dict = {}
    import aws_sdk_cleanroomsml.types.s3_config_map

    out["s3Destination"] = aws_sdk_cleanroomsml.types.s3_config_map.serialize_json(
        value["s3_destination"]
    )
    return out


def deserialize_json(data: dict) -> AudienceDestination:
    out: AudienceDestination = {}  # type: ignore[typeddict-item]
    if "s3Destination" in data:
        import aws_sdk_cleanroomsml.types.s3_config_map

        out["s3_destination"] = (
            aws_sdk_cleanroomsml.types.s3_config_map.deserialize_json(
                data["s3Destination"]
            )
        )
    else:
        raise DeserializationError("AudienceDestination.s3_destination required")
    return out
