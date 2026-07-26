"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#GetApplicationComponentDetailsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_migrationhubstrategy.types.application_component_detail
    import capo_migrationhubstrategy.types.associated_applications
    import capo_migrationhubstrategy.types.associated_server_i_ds
    import capo_migrationhubstrategy.types.boolean


class GetApplicationComponentDetailsResponse(TypedDict, closed=True):
    application_component_detail: NotRequired[
        "capo_migrationhubstrategy.types.application_component_detail.ApplicationComponentDetail"
    ]
    """<p> Detailed information about an application component. </p>"""
    associated_applications: NotRequired[
        "capo_migrationhubstrategy.types.associated_applications.AssociatedApplications"
    ]
    """<p> The associated application group as defined in AWS Application Discovery Service. </p>"""
    more_application_resource: NotRequired[
        "capo_migrationhubstrategy.types.boolean.Boolean"
    ]
    """<p> Set to true if the application component belongs to more than one application group. </p>"""
    associated_server_ids: NotRequired[
        "capo_migrationhubstrategy.types.associated_server_i_ds.AssociatedServerIDs"
    ]
    """<p> A list of the IDs of the servers on which the application component is running. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetApplicationComponentDetailsResponse) -> dict:
    out: dict = {}
    if "application_component_detail" in value:
        import capo_migrationhubstrategy.types.application_component_detail

        out["applicationComponentDetail"] = (
            capo_migrationhubstrategy.types.application_component_detail.serialize_json(
                value["application_component_detail"]
            )
        )
    if "associated_applications" in value:
        import capo_migrationhubstrategy.types.associated_applications

        out["associatedApplications"] = (
            capo_migrationhubstrategy.types.associated_applications.serialize_json(
                value["associated_applications"]
            )
        )
    if "more_application_resource" in value:
        out["moreApplicationResource"] = value["more_application_resource"]
    if "associated_server_ids" in value:
        import capo_migrationhubstrategy.types.associated_server_i_ds

        out["associatedServerIds"] = (
            capo_migrationhubstrategy.types.associated_server_i_ds.serialize_json(
                value["associated_server_ids"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetApplicationComponentDetailsResponse:
    out: GetApplicationComponentDetailsResponse = {}  # type: ignore[typeddict-item]
    if "applicationComponentDetail" in data:
        import capo_migrationhubstrategy.types.application_component_detail

        out["application_component_detail"] = (
            capo_migrationhubstrategy.types.application_component_detail.deserialize_json(
                data["applicationComponentDetail"]
            )
        )
    if "associatedApplications" in data:
        import capo_migrationhubstrategy.types.associated_applications

        out["associated_applications"] = (
            capo_migrationhubstrategy.types.associated_applications.deserialize_json(
                data["associatedApplications"]
            )
        )
    if "moreApplicationResource" in data:
        out["more_application_resource"] = data["moreApplicationResource"]
    if "associatedServerIds" in data:
        import capo_migrationhubstrategy.types.associated_server_i_ds

        out["associated_server_ids"] = (
            capo_migrationhubstrategy.types.associated_server_i_ds.deserialize_json(
                data["associatedServerIds"]
            )
        )
    return out
