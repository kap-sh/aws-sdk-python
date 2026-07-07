"""Generated from Smithy shape ``com.amazonaws.directoryservice#UpdateNumberOfDomainControllersRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_directory_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_directory_service.types.desired_number_of_domain_controllers
    import aws_sdk_directory_service.types.directory_id


class UpdateNumberOfDomainControllersRequest(TypedDict, closed=True):
    directory_id: "aws_sdk_directory_service.types.directory_id.DirectoryId"
    """<p>Identifier of the directory to which the domain controllers will be added or removed.</p>"""
    desired_number: "aws_sdk_directory_service.types.desired_number_of_domain_controllers.DesiredNumberOfDomainControllers"
    """<p>The number of domain controllers desired in the directory.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateNumberOfDomainControllersRequest) -> dict:
    out: dict = {}
    out["DirectoryId"] = value["directory_id"]
    out["DesiredNumber"] = value["desired_number"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateNumberOfDomainControllersRequest:
    out: UpdateNumberOfDomainControllersRequest = {}  # type: ignore[typeddict-item]
    if "DirectoryId" in data:
        out["directory_id"] = data["DirectoryId"]
    else:
        raise DeserializationError(
            "UpdateNumberOfDomainControllersRequest.directory_id required"
        )
    if "DesiredNumber" in data:
        out["desired_number"] = data["DesiredNumber"]
    else:
        raise DeserializationError(
            "UpdateNumberOfDomainControllersRequest.desired_number required"
        )
    return out
