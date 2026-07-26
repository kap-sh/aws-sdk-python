"""Generated from Smithy shape ``com.amazonaws.amp#ScrapeConfiguration``."""

from typing import TypeAlias

from typing_extensions import TypedDict

from capo_amp.errors import DeserializationError, SerializationError


class _ScrapeConfiguration_configurationBlob(TypedDict, closed=True):
    configurationBlob: "bytes"


ScrapeConfiguration: TypeAlias = _ScrapeConfiguration_configurationBlob


# --- restJson1 ser/de ---
def serialize_json(value: ScrapeConfiguration) -> dict:
    if "configurationBlob" in value:
        import capo_amp.types._prelude.blob

        return {
            "configurationBlob": capo_amp.types._prelude.blob.serialize_json(
                value["configurationBlob"]
            )
        }
    else:
        raise SerializationError("ScrapeConfiguration: no variant present")


def deserialize_json(data: dict) -> ScrapeConfiguration:
    if "configurationBlob" in data:
        import capo_amp.types._prelude.blob

        return {
            "configurationBlob": capo_amp.types._prelude.blob.deserialize_json(
                data["configurationBlob"]
            )
        }
    else:
        raise DeserializationError("ScrapeConfiguration: no recognized variant key")
