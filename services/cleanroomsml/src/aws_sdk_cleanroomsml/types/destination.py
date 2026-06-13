"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#Destination``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cleanroomsml.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanroomsml.types.s3_config_map


class Destination(TypedDict):
    s3_destination: "aws_sdk_cleanroomsml.types.s3_config_map.S3ConfigMap"


# --- restJson1 ser/de ---
def serialize_json(value: Destination) -> dict:
    out: dict = {}
    import aws_sdk_cleanroomsml.types.s3_config_map

    out["s3Destination"] = aws_sdk_cleanroomsml.types.s3_config_map.serialize_json(
        value["s3_destination"]
    )
    return out


def deserialize_json(data: dict) -> Destination:
    out: Destination = {}  # type: ignore[typeddict-item]
    if "s3Destination" in data:
        import aws_sdk_cleanroomsml.types.s3_config_map

        out["s3_destination"] = (
            aws_sdk_cleanroomsml.types.s3_config_map.deserialize_json(
                data["s3Destination"]
            )
        )
    else:
        raise DeserializationError("Destination.s3_destination required")
    return out
