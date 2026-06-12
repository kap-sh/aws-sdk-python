"""Generated from Smithy shape ``com.amazonaws.servicecatalogappregistry#UpdateApplicationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_service_catalog_appregistry.types.application


class UpdateApplicationResponse(TypedDict):
    application: NotRequired[
        "aws_sdk_service_catalog_appregistry.types.application.Application"
    ]
    """<p>The updated information of the application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateApplicationResponse) -> dict:
    out: dict = {}
    if "application" in value:
        import aws_sdk_service_catalog_appregistry.types.application

        out["application"] = (
            aws_sdk_service_catalog_appregistry.types.application.serialize_json(
                value["application"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateApplicationResponse:
    out: UpdateApplicationResponse = {}  # type: ignore[typeddict-item]
    if "application" in data:
        import aws_sdk_service_catalog_appregistry.types.application

        out["application"] = (
            aws_sdk_service_catalog_appregistry.types.application.deserialize_json(
                data["application"]
            )
        )
    return out
