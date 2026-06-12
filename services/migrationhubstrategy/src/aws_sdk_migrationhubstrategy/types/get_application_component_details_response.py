"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#GetApplicationComponentDetailsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_migrationhubstrategy.types.application_component_detail
    import aws_sdk_migrationhubstrategy.types.associated_applications
    import aws_sdk_migrationhubstrategy.types.associated_server_i_ds
    import aws_sdk_migrationhubstrategy.types.boolean


class GetApplicationComponentDetailsResponse(TypedDict):
    application_component_detail: NotRequired[
        "aws_sdk_migrationhubstrategy.types.application_component_detail.ApplicationComponentDetail"
    ]
    """<p> Detailed information about an application component. </p>"""
    associated_applications: NotRequired[
        "aws_sdk_migrationhubstrategy.types.associated_applications.AssociatedApplications"
    ]
    """<p> The associated application group as defined in AWS Application Discovery Service. </p>"""
    more_application_resource: NotRequired[
        "aws_sdk_migrationhubstrategy.types.boolean.Boolean"
    ]
    """<p> Set to true if the application component belongs to more than one application group. </p>"""
    associated_server_ids: NotRequired[
        "aws_sdk_migrationhubstrategy.types.associated_server_i_ds.AssociatedServerIDs"
    ]
    """<p> A list of the IDs of the servers on which the application component is running. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetApplicationComponentDetailsResponse) -> dict:
    out: dict = {}
    if "application_component_detail" in value:
        import aws_sdk_migrationhubstrategy.types.application_component_detail

        out["applicationComponentDetail"] = (
            aws_sdk_migrationhubstrategy.types.application_component_detail.serialize_json(
                value["application_component_detail"]
            )
        )
    if "associated_applications" in value:
        import aws_sdk_migrationhubstrategy.types.associated_applications

        out["associatedApplications"] = (
            aws_sdk_migrationhubstrategy.types.associated_applications.serialize_json(
                value["associated_applications"]
            )
        )
    if "more_application_resource" in value:
        out["moreApplicationResource"] = value["more_application_resource"]
    if "associated_server_ids" in value:
        import aws_sdk_migrationhubstrategy.types.associated_server_i_ds

        out["associatedServerIds"] = (
            aws_sdk_migrationhubstrategy.types.associated_server_i_ds.serialize_json(
                value["associated_server_ids"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetApplicationComponentDetailsResponse:
    out: GetApplicationComponentDetailsResponse = {}  # type: ignore[typeddict-item]
    if "applicationComponentDetail" in data:
        import aws_sdk_migrationhubstrategy.types.application_component_detail

        out["application_component_detail"] = (
            aws_sdk_migrationhubstrategy.types.application_component_detail.deserialize_json(
                data["applicationComponentDetail"]
            )
        )
    if "associatedApplications" in data:
        import aws_sdk_migrationhubstrategy.types.associated_applications

        out["associated_applications"] = (
            aws_sdk_migrationhubstrategy.types.associated_applications.deserialize_json(
                data["associatedApplications"]
            )
        )
    if "moreApplicationResource" in data:
        out["more_application_resource"] = data["moreApplicationResource"]
    if "associatedServerIds" in data:
        import aws_sdk_migrationhubstrategy.types.associated_server_i_ds

        out["associated_server_ids"] = (
            aws_sdk_migrationhubstrategy.types.associated_server_i_ds.deserialize_json(
                data["associatedServerIds"]
            )
        )
    return out
