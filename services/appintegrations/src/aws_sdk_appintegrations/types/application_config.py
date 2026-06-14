"""Generated from Smithy shape ``com.amazonaws.appintegrations#ApplicationConfig``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_appintegrations.types.contact_handling

class ApplicationConfig(TypedDict):
    contact_handling: NotRequired["aws_sdk_appintegrations.types.contact_handling.ContactHandling"]
    """<p>The contact handling configuration for the application.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: ApplicationConfig) -> dict:
    out: dict = {}
    if "contact_handling" in value:
        import aws_sdk_appintegrations.types.contact_handling
        out["ContactHandling"] = aws_sdk_appintegrations.types.contact_handling.serialize_json(value["contact_handling"])
    return out


def deserialize_json(data: dict) -> ApplicationConfig:
    out: ApplicationConfig = {}  # type: ignore[typeddict-item]
    if "ContactHandling" in data:
        import aws_sdk_appintegrations.types.contact_handling
        out["contact_handling"] = aws_sdk_appintegrations.types.contact_handling.deserialize_json(data["ContactHandling"])
    return out