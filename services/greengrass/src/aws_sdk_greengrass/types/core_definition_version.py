"""Generated from Smithy shape ``com.amazonaws.greengrass#CoreDefinitionVersion``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_greengrass.types.__list_of_core


class CoreDefinitionVersion(TypedDict, closed=True):
    cores: NotRequired["aws_sdk_greengrass.types.__list_of_core.__listOfCore"]
    """A list of cores in the core definition version."""


# --- restJson1 ser/de ---
def serialize_json(value: CoreDefinitionVersion) -> dict:
    out: dict = {}
    if "cores" in value:
        import aws_sdk_greengrass.types.__list_of_core

        out["Cores"] = aws_sdk_greengrass.types.__list_of_core.serialize_json(
            value["cores"]
        )
    return out


def deserialize_json(data: dict) -> CoreDefinitionVersion:
    out: CoreDefinitionVersion = {}  # type: ignore[typeddict-item]
    if "Cores" in data:
        import aws_sdk_greengrass.types.__list_of_core

        out["cores"] = aws_sdk_greengrass.types.__list_of_core.deserialize_json(
            data["Cores"]
        )
    return out
