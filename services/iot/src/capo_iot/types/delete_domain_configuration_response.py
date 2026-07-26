"""Generated from Smithy shape ``com.amazonaws.iot#DeleteDomainConfigurationResponse``."""

from typing_extensions import TypedDict


class DeleteDomainConfigurationResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDomainConfigurationResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteDomainConfigurationResponse:
    out: DeleteDomainConfigurationResponse = {}  # type: ignore[typeddict-item]
    return out
