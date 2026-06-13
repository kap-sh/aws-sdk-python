"""Generated from Smithy shape ``com.amazonaws.gameliftstreams#RuntimeEnvironment``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_gameliftstreams.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_gameliftstreams.types.runtime_environment_type
    import aws_sdk_gameliftstreams.types.runtime_environment_version


class RuntimeEnvironment(TypedDict):
    type: (
        "aws_sdk_gameliftstreams.types.runtime_environment_type.RuntimeEnvironmentType"
    )
    """<p>The operating system and other drivers. For Proton, this also includes the Proton compatibility layer.</p>"""
    version: "aws_sdk_gameliftstreams.types.runtime_environment_version.RuntimeEnvironmentVersion"
    """<p>Versioned container environment for the application operating system.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RuntimeEnvironment) -> dict:
    out: dict = {}
    import aws_sdk_gameliftstreams.types.runtime_environment_type

    out["Type"] = aws_sdk_gameliftstreams.types.runtime_environment_type.serialize_json(
        value["type"]
    )
    out["Version"] = value["version"]
    return out


def deserialize_json(data: dict) -> RuntimeEnvironment:
    out: RuntimeEnvironment = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import aws_sdk_gameliftstreams.types.runtime_environment_type

        out["type"] = (
            aws_sdk_gameliftstreams.types.runtime_environment_type.deserialize_json(
                data["Type"]
            )
        )
    else:
        raise DeserializationError("RuntimeEnvironment.type required")
    if "Version" in data:
        out["version"] = data["Version"]
    else:
        raise DeserializationError("RuntimeEnvironment.version required")
    return out
