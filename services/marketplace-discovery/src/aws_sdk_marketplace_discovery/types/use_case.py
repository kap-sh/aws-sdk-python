"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#UseCase``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_marketplace_discovery.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_marketplace_discovery.types.non_empty_string


class UseCase(TypedDict, closed=True):
    description: "aws_sdk_marketplace_discovery.types.non_empty_string.NonEmptyString"
    """<p>A description of the use case.</p>"""
    display_name: "aws_sdk_marketplace_discovery.types.non_empty_string.NonEmptyString"
    """<p>The human-readable name of the use case.</p>"""
    value: "aws_sdk_marketplace_discovery.types.non_empty_string.NonEmptyString"
    """<p>The machine-readable identifier of the use case.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UseCase) -> dict:
    out: dict = {}
    out["description"] = value["description"]
    out["displayName"] = value["display_name"]
    out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> UseCase:
    out: UseCase = {}  # type: ignore[typeddict-item]
    if "description" in data:
        out["description"] = data["description"]
    else:
        raise DeserializationError("UseCase.description required")
    if "displayName" in data:
        out["display_name"] = data["displayName"]
    else:
        raise DeserializationError("UseCase.display_name required")
    if "value" in data:
        out["value"] = data["value"]
    else:
        raise DeserializationError("UseCase.value required")
    return out
