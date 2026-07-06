"""Generated from Smithy shape ``com.amazonaws.servicecatalogappregistry#DeleteApplicationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_service_catalog_appregistry.types.application_summary


class DeleteApplicationResponse(TypedDict, closed=True):
    application: NotRequired[
        "aws_sdk_service_catalog_appregistry.types.application_summary.ApplicationSummary"
    ]
    """<p>Information about the deleted application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteApplicationResponse) -> dict:
    out: dict = {}
    if "application" in value:
        import aws_sdk_service_catalog_appregistry.types.application_summary

        out["application"] = (
            aws_sdk_service_catalog_appregistry.types.application_summary.serialize_json(
                value["application"]
            )
        )
    return out


def deserialize_json(data: dict) -> DeleteApplicationResponse:
    out: DeleteApplicationResponse = {}  # type: ignore[typeddict-item]
    if "application" in data:
        import aws_sdk_service_catalog_appregistry.types.application_summary

        out["application"] = (
            aws_sdk_service_catalog_appregistry.types.application_summary.deserialize_json(
                data["application"]
            )
        )
    return out
