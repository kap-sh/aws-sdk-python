"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#UseCaseEntry``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_marketplace_discovery.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_marketplace_discovery.types.use_case


class UseCaseEntry(TypedDict):
    use_case: "aws_sdk_marketplace_discovery.types.use_case.UseCase"
    """<p>The use case details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UseCaseEntry) -> dict:
    out: dict = {}
    import aws_sdk_marketplace_discovery.types.use_case

    out["useCase"] = aws_sdk_marketplace_discovery.types.use_case.serialize_json(
        value["use_case"]
    )
    return out


def deserialize_json(data: dict) -> UseCaseEntry:
    out: UseCaseEntry = {}  # type: ignore[typeddict-item]
    if "useCase" in data:
        import aws_sdk_marketplace_discovery.types.use_case

        out["use_case"] = aws_sdk_marketplace_discovery.types.use_case.deserialize_json(
            data["useCase"]
        )
    else:
        raise DeserializationError("UseCaseEntry.use_case required")
    return out
