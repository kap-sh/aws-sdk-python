"""Generated from Smithy shape ``com.amazonaws.servicecatalogappregistry#CreateApplicationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog_appregistry.types.application


class CreateApplicationResponse(TypedDict, closed=True):
    application: NotRequired[
        "capo_service_catalog_appregistry.types.application.Application"
    ]
    """<p>Information about the application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateApplicationResponse) -> dict:
    out: dict = {}
    if "application" in value:
        import capo_service_catalog_appregistry.types.application

        out["application"] = (
            capo_service_catalog_appregistry.types.application.serialize_json(
                value["application"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateApplicationResponse:
    out: CreateApplicationResponse = {}  # type: ignore[typeddict-item]
    if "application" in data:
        import capo_service_catalog_appregistry.types.application

        out["application"] = (
            capo_service_catalog_appregistry.types.application.deserialize_json(
                data["application"]
            )
        )
    return out
