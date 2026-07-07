"""Generated from Smithy shape ``com.amazonaws.greengrass#CreateCoreDefinitionVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_greengrass.types.__list_of_core
    import aws_sdk_greengrass.types.__string


class CreateCoreDefinitionVersionRequest(TypedDict, closed=True):
    amzn_client_token: NotRequired["aws_sdk_greengrass.types.__string.__string"]
    """A client token used to correlate requests and responses."""
    core_definition_id: "aws_sdk_greengrass.types.__string.__string"
    """The ID of the core definition."""
    cores: NotRequired["aws_sdk_greengrass.types.__list_of_core.__listOfCore"]
    """A list of cores in the core definition version."""


# --- restJson1 ser/de ---
def serialize_json(value: CreateCoreDefinitionVersionRequest) -> dict:
    out: dict = {}
    if "cores" in value:
        import aws_sdk_greengrass.types.__list_of_core

        out["Cores"] = aws_sdk_greengrass.types.__list_of_core.serialize_json(
            value["cores"]
        )
    return out


def deserialize_json(data: dict) -> CreateCoreDefinitionVersionRequest:
    out: CreateCoreDefinitionVersionRequest = {}  # type: ignore[typeddict-item]
    if "Cores" in data:
        import aws_sdk_greengrass.types.__list_of_core

        out["cores"] = aws_sdk_greengrass.types.__list_of_core.deserialize_json(
            data["Cores"]
        )
    return out
